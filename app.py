import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from dotenv import load_dotenv
from supabase import create_client, Client

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24) # Chave secreta para gerenciar sessões

# Configuração do cliente Supabase
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# --- ROTAS PÚBLICAS ---
@app.route('/')
def index():
    """Página inicial que exibe os links de um usuário específico."""
    # Neste exemplo simples, vamos exibir os links de um usuário fixo.
    # Numa aplicação real, você poderia ter /<username>
    user_id_demo = "82ab08a4-61f3-4d31-88b6-093a561954ad" # Substitua pelo ID de um usuário de teste
    try:
        response = supabase.table('links').select('*').eq('user_id', user_id_demo).execute()
        links = response.data
        return render_template('index.html', links=links)
    except Exception as e:
        flash(f"Erro ao carregar links: {e}", "danger")
        return render_template('index.html', links=[])


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Página de login."""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            data = supabase.auth.sign_in_with_password({"email": email, "password": password})
            session['user'] = data.user.id
            return redirect(url_for('dashboard'))
        except Exception as e:
            flash(f"Erro no login: {e}", 'danger')
            return redirect(url_for('login'))
    return render_template('login.html')

# --- ROTAS PRIVADAS (Requerem Login) ---

@app.route('/dashboard')
def dashboard():
    """Painel de gerenciamento de links do usuário."""
    user_id = session.get('user')
    if not user_id:
        return redirect(url_for('login'))

    try:
        response = supabase.table('links').select('*').eq('user_id', user_id).execute()
        links = response.data
        return render_template('dashboard.html', links=links)
    except Exception as e:
        flash(f"Erro ao carregar seus links: {e}", "danger")
        return render_template('dashboard.html', links=[])


@app.route('/add_link', methods=['POST'])
def add_link():
    """Adiciona um novo link."""
    user_id = session.get('user')
    if not user_id:
        return redirect(url_for('login'))

    title = request.form.get('title')
    url = request.form.get('url')

    if title and url:
        try:
            supabase.table('links').insert({
                'title': title,
                'url': url,
                'user_id': user_id
            }).execute()
            flash("Link adicionado com sucesso!", "success")
        except Exception as e:
            flash(f"Erro ao adicionar link: {e}", "danger")

    return redirect(url_for('dashboard'))

@app.route('/delete_link/<int:link_id>', methods=['POST'])
def delete_link(link_id):
    """Deleta um link."""
    user_id = session.get('user')
    if not user_id:
        return redirect(url_for('login'))

    try:
        # Garante que o usuário só pode deletar os próprios links
        supabase.table('links').delete().match({'id': link_id, 'user_id': user_id}).execute()
        flash("Link removido com sucesso!", "success")
    except Exception as e:
        flash(f"Erro ao remover link: {e}", "danger")

    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    """Realiza o logout do usuário."""
    session.pop('user', None)
    flash("Você foi desconectado.", "info")
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)