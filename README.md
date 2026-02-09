# 🌐 Fronteira Viva

O **Fronteira Viva** é um portal web de turismo focado na cidade de **Ponta Porã/MS**. O projeto foi desenhado especificamente para atender **idosos** e **turistas de compras**, unindo acessibilidade com informações práticas de utilidade pública.

O site reúne cultura, história local, roteiros acessíveis e dados em tempo real para facilitar a experiência de quem visita a fronteira.

---

## ✨ Funcionalidades Principais

- 🏛️ **Cultura e História:** Roteiros turísticos, pontos históricos, linha do tempo e eventos culturais.
- 🛍️ **Turismo de Compras:** Informações em tempo real sobre a **fila da Receita Federal** e **cotação do dólar**.
- ♿ **Acessibilidade:** Botões de ajuste de fonte, alto contraste e suporte a áudio.
- 🗺️ **Mapa Interativo:** Localização visual dos pontos culturais.
- 📝 **Avaliações:** Feedback dos usuários sobre os roteiros visitados.
- 🔐 **Painel Administrativo:** Gestão de conteúdo, atualização de câmbio e monitoramento da fila.

---

## 🛠️ Tecnologias Utilizadas

O projeto utiliza uma stack robusta e escalável:

- **Backend:** [Django](https://www.djangoproject.com/) (Python)
- **Banco de Dados:** [MySQL](https://www.mysql.com/)
- **Frontend:** HTML5, CSS3 e JavaScript
- **Estilização:** Design responsivo e focado em acessibilidade

---

## ⚙️ Pré-requisitos

Certifique-se de ter instalado em sua máquina:
* Python 3.x
* MySQL Server
* Pip (gerenciador de pacotes do Python)

---

## 💻 Instalação e Configuração

Siga os passos abaixo para rodar o projeto localmente:

### 1. Clonar o repositório
```bash
git clone [https://github.com/seuusuario/fronteiraviva.git](https://github.com/seuusuario/fronteiraviva.git)
cd fronteiraviva

### Criar o ambiente
python -m venv venv

#Ativar (Windows)
venv\Scripts\activate

# Ativar (Linux/Mac)
source venv/bin/activate

### Instalar Dependências
- **pip install -r requirements.txt

### Migrações e Superusuário

python manage.py makemigrations
python manage.py migrate

# Criar conta de administrador
python manage.py createsuperuser

### ▶️ Como Rodar
Com o ambiente configurado, inicie o servidor:

python manage.py runserver

## Interface Administrativa

### O que eu melhorei para você:
1.  **Hierarquia:** Usei títulos (`##`) e subtítulos (`###`) para o usuário não se perder.
2.  **Visual:** Adicionei emojis temáticos que deixam o README mais profissional e amigável.
3.  **Clareza técnica:** Separei a configuração do banco de dados em um bloco de código Python específico.
4.  **Escaneabilidade:** O uso de listas (`*` ou `-`) ajuda o leitor a bater o olho e entender o que o projeto faz em segundos.

**Dica de mestre:** Se você tiver um print da tela principal, coloque uma imagem logo após o título principal usando `![Home Page](./caminho/para/sua/imagem.png)`. Isso valoriza muito o repositório!

Gostaria que eu criasse uma seção de **"Como Contribuir"** ou uma licença para o seu projeto?
