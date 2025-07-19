import requests
import base64
import re

class SpotifySimple:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = self.get_token()
    
    def get_token(self):
        """Obter token de acesso"""
        # Formato exigido: "client_id:client_secret"
        credentials = f"{self.client_id}:{self.client_secret}"
        
        # Codificar em Base64 (exigido pela API)
        credentials_bytes = credentials.encode("utf-8")
        credentials_base64 = base64.b64encode(credentials_bytes).decode("utf-8")
        
        # Fazer requisição
        headers = {"Authorization": f"Basic {credentials_base64}"}
        data = {"grant_type": "client_credentials"}
        
        response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)
        return response.json()["access_token"]
        
    def get_tracks_from_link(self, spotify_link):
        """Extrair músicas de qualquer link do Spotify - sempre retorna array"""
        headers = {"Authorization": f"Bearer {self.token}"}
        
        if "/track/" in spotify_link:
            # 1 música
            track_id = re.search(r"track/([a-zA-Z0-9]+)", spotify_link).group(1)
            url = f"https://api.spotify.com/v1/tracks/{track_id}"
            response = requests.get(url, headers=headers)
            track = response.json()
            
            return [{"music": track["name"], "artist": track["artists"][0]["name"]}]
        
        elif "/playlist/" in spotify_link:
            # Várias músicas (playlist)
            playlist_id = re.search(r"playlist/([a-zA-Z0-9]+)", spotify_link).group(1)
            url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
            response = requests.get(url, headers=headers)
            items = response.json()["items"]
            
            return [{"music": item["track"]["name"], "artist": item["track"]["artists"][0]["name"]} 
                   for item in items if item["track"]]
        
        elif "/album/" in spotify_link:
            # Várias músicas (álbum)
            album_id = re.search(r"album/([a-zA-Z0-9]+)", spotify_link).group(1)
            url = f"https://api.spotify.com/v1/albums/{album_id}/tracks"
            response = requests.get(url, headers=headers)
            items = response.json()["items"]
            
            return [{"music": track["name"], "artist": track["artists"][0]["name"]} 
                   for track in items]
        
        # Link inválido
        return []