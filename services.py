import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from googleapiclient.errors import HttpError

# API Constants
CLIENT_SECRETS_FILE = "client_secret.json"
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"

def get_authenticated_service():
    """Realiza a autenticação via OAuth 2.0 e retorna um objeto de serviço da API."""
    credentials = None
    # O arquivo token.pickle armazena os tokens de acesso e de atualização do usuário.
    # Ele é criado automaticamente na primeira vez que o fluxo de autorização é concluído.
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            credentials = pickle.load(token)

    # Se não houver credenciais (válidas), o usuário precisará fazer login.
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
            # Abre um servidor local para o fluxo de autorização
            credentials = flow.run_local_server(port=0)
        
        # Salva as credenciais para as próximas execuções
        with open("token.pickle", "wb") as token:
            pickle.dump(credentials, token)

    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)


def search_video(youtube, query):
    """Busca um vídeo no YouTube e retorna o ID do primeiro resultado."""
    try:
        search_response = youtube.search().list(
            q=query,
            part="snippet",
            maxResults=1,
            type="video"
        ).execute()

        if not search_response.get("items"):
            print(f"  -> Nenhum resultado encontrado para '{query}'")
            return None
        
        video_id = search_response["items"][0]["id"]["videoId"]
        video_title = search_response["items"][0]["snippet"]["title"]
        print(f"  -> Vídeo encontrado: '{video_title}' (ID: {video_id})")
        return video_id

    except HttpError as e:
        print(f"  -> Erro na busca: {e}")
        return None

def add_video_to_playlist(youtube, video_id, playlist_id):
    """Adiciona um vídeo a uma playlist específica."""
    try:
        request = youtube.playlistItems().insert(
            part="snippet",
            body={
                "snippet": {
                    "playlistId": playlist_id,
                    "resourceId": {
                        "kind": "youtube#video",
                        "videoId": video_id
                    }
                }
            }
        )
        response = request.execute()
        print(f"  -> Vídeo adicionado com sucesso à playlist! (Item ID: {response['id']})")
        return response
    except HttpError as e:
        # Erro 409 (Conflict) geralmente significa que o vídeo já está na playlist.
        if e.resp.status == 409:
            print(f"  -> AVISO: O vídeo já está na playlist.")
        else:
            print(f"  -> ERRO ao adicionar à playlist: {e}")
        return None
