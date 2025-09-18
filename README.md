# Meu Linktree Pessoal com Flask e Supabase

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.2+-black?style=for-the-badge&logo=flask)
![Supabase](https://img.shields.io/badge/Supabase-green?style=for-the-badge&logo=supabase)

Um projeto de portfólio que implementa um agregador de links pessoais, similar a um "Linktree", utilizando Python com o microframework Flask para o backend e Supabase para banco de dados PostgreSQL e autenticação.

---

###  демонстрация
**É muito importante que você tire um print da tela do seu projeto funcionando e coloque aqui.** Para fazer isso:
1. Tire um print da página principal com os links.
2. Salve a imagem (ex: `demo.png`) em uma pasta `assets` ou na raiz do projeto.
3. Suba a imagem para o GitHub.
4. Mude a linha abaixo para o caminho correto: `![Demo do Projeto](demo.png)`

![Demo do Projeto](https://via.placeholder.com/700x400.png?text=Coloque+aqui+um+print+do+seu+projeto!)

---

### 🚀 Tecnologias Utilizadas

* **Backend:** Python 3, Flask
* **Banco de Dados & Autenticação:** Supabase (PostgreSQL)
* **Frontend:** HTML, CSS com Bootstrap 5
* **Gerenciamento de Dependências:** `pip`, `requirements.txt`
* **Variáveis de Ambiente:** `python-dotenv`

---

### ✨ Funcionalidades

* **Página de Links Pública:** Uma página principal que exibe todos os links cadastrados por um usuário.
* **Autenticação de Usuário:** Sistema de login para acesso a um painel administrativo.
* **Dashboard de Gerenciamento:**
    * Visualização de todos os links cadastrados.
    * Adição de novos links (título e URL).
    * Remoção de links existentes.
* **Sessões de Usuário:** O estado de login é mantido através de sessões seguras do Flask.

---

### ⚙️ Como Executar o Projeto Localmente

Siga os passos abaixo para rodar o projeto na sua máquina.

**1. Clone o Repositório**
```bash
git clone [https://github.com/gabriel-silvo/flask-linktree.git](https://github.com/gabriel-silvo/flask-linktree.git)
cd flask-linktree
```

**2. Crie e Ative o Ambiente Virtual**
```bash
# Criar o ambiente
python -m venv venv

# Ativar no Windows
.\venv\Scripts\activate

# Ativar no macOS/Linux
source venv/bin/activate
```

**3. Instale as Dependências**
```bash
pip install -r requirements.txt
```

**4. Configure as Variáveis de Ambiente**
* Crie uma conta gratuita no [Supabase](https://supabase.com) e crie um novo projeto.
* Crie a tabela `links` conforme a estrutura descrita no projeto.
* Obtenha a `URL` e a chave `anon (public)` nas configurações de API do seu projeto Supabase.
* Crie um arquivo chamado `.env` na raiz do projeto e adicione suas credenciais:
    ```
    SUPABASE_URL="SUA_URL_DO_PROJETO_SUPABASE"
    SUPABASE_KEY="SUA_CHAVE_ANON_PUBLIC_DO_SUPABASE"
    ```

**5. Crie um Usuário de Teste**
* No painel do Supabase, vá em `Authentication` > `Users` e crie um usuário para testes.
* Copie o `UID` desse usuário e cole-o na variável `user_id_demo` dentro do arquivo `app.py`.

**6. Execute a Aplicação**
```bash
flask run
```
Acesse `http://127.0.0.1:5000` no seu navegador para ver a página de links e `http://127.0.0.1:5000/login` para acessar o painel.

---

### 🔮 Próximos Passos e Melhorias

Este é um projeto base com grande potencial de expansão. Algumas ideias para futuras implementações:

- [ ] Implementar uma página de cadastro de novos usuários.
- [ ] Permitir que o usuário faça upload de uma foto de perfil e personalize o tema da página.
- [ ] Adicionar um contador de cliques para cada link.
- [ ] Permitir a reordenação dos links no dashboard.
- [ ] Realizar o deploy da aplicação em um serviço como Vercel ou Railway.