# List to Playlist 🎵

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Google APIs](https://img.shields.io/badge/Google%20APIs-4285F4?style=for-the-badge&logo=google&logoColor=white)
![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=youtube&logoColor=white)

Cansado de recriar playlists manualmente? Este projeto automatiza a criação de playlists no YouTube a partir de uma simples lista de músicas em um arquivo de texto. Ideal para quem está migrando de serviços de streaming e não quer perder suas músicas favoritas.

## 📖 Sobre o Projeto

A ideia nasceu de uma necessidade pessoal: migrar mais de 500 músicas do Spotify para o YouTube Music sem o trabalho manual exaustivo. A solução foi desenvolver um script em Python que lê uma lista de músicas e as adiciona automaticamente a uma playlist na sua conta do YouTube, usando a API oficial do Google.

## ✨ Funcionalidades

* **Automação Completa:** Adiciona as músicas sem intervenção manual.
* **Eficiente:** Adiciona dezenas de músicas em poucos minutos.
* **Reutilizável:** Facilmente configurável para qualquer lista de músicas e conta do YouTube.

## 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem principal do script.
* **Google API Python Client:** Para interagir de forma segura com a API do YouTube Data v3.
* **Google OAuth 2.0:** Para autenticação e autorização de acesso à sua conta do YouTube.

## 🚀 Como Começar

Para rodar este projeto, você precisará ter o Python instalado e configurar o acesso à API do YouTube.

### Pré-requisitos

1.  **Python 3.x** instalado.
2.  **Credenciais da API do YouTube:**
    * Acesse o [Google Cloud Console](https://console.cloud.google.com/).
    * Crie um novo projeto.
    * Ative a **API YouTube Data v3**.
    * Crie uma tela de consentimento OAuth (**OAuth consent screen**), configurando-a para **Uso Externo** e adicionando seu e-mail como usuário de teste.
    * Crie as credenciais do tipo **ID do cliente OAuth** para um **Aplicativo para computador**.
    * Faça o download do arquivo JSON com as credenciais e renomeie-o para `client_secret.json`, colocando-o na raiz do projeto.

### Instalação

1.  Clone o repositório:
    ```bash
    git clone https://github.com/ronaldylf/list2playlist.git
    ```
2.  Navegue até o diretório do projeto:
    ```bash
    cd list2playlist
    ```
3.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## ▶️ Como Usar

### Etapa 1: Configurando

1.  **Copie da URL o ID da sua Playlist**. 
    Cada URL no youtube ou youtube music se parece com isso:
    `https://www.youtube.com/playlist?list=PLWLuRm60qAIis1rWDvhDvuwYc5wo3I6kL`

    Então, o ID será o parâmetro que vem depois de `?list=`, sendo nesse caso `PLWLuRm60qAIis1rWDvhDvuwYc5wo3I6kL`.

2.  **Crie um arquivo `.env`** na raiz do projeto. Este arquivo guardará o ID da sua playlist.

3.  Dentro do arquivo `.env`, adicione a seguinte linha, substituindo pelo ID que você copiou:
    ```
    PLAYLIST_ID = [ID DA SUA PLAYLIST]
    ```
    Exemplo:
    ```
    PLAYLIST_ID = PLWLuRm60qAIis1rWDvhDvuwYc5wo3I6kL
    ```

### Etapa 2: Primeira Execução

1.  **Crie sua lista de músicas:**
    Crie um arquivo chamado `songs_list.txt` na raiz do projeto. Adicione uma música por linha, seguindo o formato: `Nome da Música - Nome do Artista` ou `Nome do Artista - Nome da Música`.

2.  **Execute o script pela primeira vez:**
    ```bash
    python main.py
    ```

3.  **Autorização:**
    Uma aba do seu navegador será aberta para que você autorize o acesso à sua conta do Google. Após a autorização, o script irá:
    * Salvar um arquivo `token.pickle` para manter você logado nas próximas execuções.
    * Adicionar o primeiro lote de músicas.

### Etapa 3: Continuando a Migração

1.  **Execute o script novamente** nos dias seguintes:
    ```bash
    python main.py
    ```
2.  Agora, o script irá ler o `PLAYLIST_ID` do arquivo `.env` e continuará adicionando as músicas restantes à playlist que já existe, em vez de criar uma nova. Repita esse passo até que todas as suas músicas sejam migradas.

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.