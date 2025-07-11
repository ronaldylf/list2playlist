import time
from dotenv import load_dotenv
from services import *

load_dotenv(override=True) # load .env variables

PLAYLIST_ID = os.environ['PLAYLIST_ID']

SONGS_FILE = "songs_list.txt"
REVERSE = True # reverse songs order

def main():
    """Função principal que orquestra todo o processo."""
    try:
        with open(SONGS_FILE, "r", encoding="utf-8") as f:
            songs = f.read().split('\n')
            if (REVERSE): songs.reverse()

    except FileNotFoundError:
        print(f"ERRO: Arquivo '{SONGS_FILE}' não encontrado. Crie o arquivo e adicione as músicas.")
        return

    print("Iniciando autenticação...")
    youtube = get_authenticated_service()
    print("Autenticação bem-sucedida!\n")

    for song in songs:
        print(f"Processando música: '{song}'")
        video_id = search_video(youtube, song)

        if video_id:
            add_video_to_playlist(youtube, video_id, PLAYLIST_ID)
        
        # Pausa de 1 segundo para não sobrecarregar a API do YouTube
        time.sleep(1)
        print("-" * 40)

    print("Processo finalizado!")

if __name__ == "__main__":
    main()