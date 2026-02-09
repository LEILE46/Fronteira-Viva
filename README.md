# 🌐 Fronteira Viva

**Fronteira Viva** é um portal web de turismo em **Ponta Porã**, voltado para **idosos** e **turistas de compras**.  
O site reúne informações sobre **cultura e história local**, roteiros acessíveis, eventos culturais, além de dados em tempo real como **fila da Receita Federal** e **cotação do dólar**.

O projeto foi desenvolvido com **Django**, **MySQL**, **HTML**, **CSS** e **JavaScript**, sendo **responsivo** e **acessível**.

---

## ⚙️ Pré-requisitos

Antes de rodar o projeto, você precisa ter instalado:

- Python 3.x  
- pip  
- MySQL  
- Git (opcional)  

---

## 💻 Instalação

1. **Clonar o repositório:**  
```bash
git clone https://github.com/seuusuario/fronteiraviva.git
cd fronteiraviva
Criar e ativar ambiente virtual:

python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
Instalar dependências:

pip install -r requirements.txt
Configurar banco de dados MySQL:

Crie um banco chamado fronteiraviva

Atualize settings.py com seu usuário e senha:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fronteiraviva',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
Rodar migrações:

python manage.py makemigrations
python manage.py migrate
Criar superusuário (administrador):

python manage.py createsuperuser
#▶️ Como rodar
python manage.py runserver
Acesse no navegador: http://127.0.0.1:8000/

Faça login para acessar funcionalidades administrativas.

# 🖥️ Tela Principal
- A página inicial contém:

- Cabeçalho: logo, nome do site, botões de acessibilidade (fonte, contraste, áudio) e login

- Seção Cultura e História: roteiros, pontos históricos, linha do tempo e eventos

- Seção Informações de Compras: fila da Receita Federal e cotação do dólar

- Mapa Interativo: pontos culturais

- Avaliações: avaliação de roteiros

- Admin: atualização de fila, câmbio e cadastro de conteúdo
