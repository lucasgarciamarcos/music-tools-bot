# Discord Music Bot

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Discord.py-5865F2?style=for-the-badge&logo=discord&logoColor=white" />
  <img src="https://img.shields.io/badge/Spotify-1ED760?style=for-the-badge&logo=spotify&logoColor=white" />
  <img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" />
</p>

Um bot de música para Discord simples e fácil de usar, com suporte para YouTube e Spotify, ideal para demonstrar suas habilidades em desenvolvimento de bots e integração de APIs em seu portfólio.

## ✨ Recursos

- Reproduz músicas do YouTube (links e buscas)
- Reproduz músicas, playlists e álbuns do Spotify
- Sistema de fila de reprodução
- Comandos simples e intuitivos

## 🛠️ Tecnologias Utilizadas

- **[Python](https://www.python.org/)**: A linguagem de programação principal do projeto.
- **[Discord.py](https://discordpy.readthedocs.io/en/stable/)**: Uma biblioteca Python para criar bots para o Discord.
- **[Spotify Web API](https://developer.spotify.com/documentation/web-api/)**: Para buscar informações sobre músicas, álbuns e playlists.
- **[yt-dlp](https://github.com/yt-dlp/yt-dlp)**: Para extrair o áudio de vídeos do YouTube.
- **[FFmpeg](https://ffmpeg.org/)**: Para processamento de áudio.

## 🚀 Começando

Siga estas instruções para configurar e executar o bot em seu próprio servidor.

### Pré-requisitos

- [Python 3.8+](https://www.python.org/downloads/)
- [FFmpeg](https://ffmpeg.org/download.html) - É necessário que o `ffmpeg.exe` esteja na mesma pasta do `main.py` ou no PATH do seu sistema.
- Uma conta no Discord e um token de bot. Você pode criar um [aqui](https://discord.com/developers/applications).
- Credenciais da API do Spotify (Client ID e Client Secret). Você pode criá-las [aqui](https://developer.spotify.com/dashboard/).

### Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
   venv\scripts\Activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente:**
   Crie um arquivo chamado `.env` na raiz do projeto e adicione as seguintes informações:

   ```
   DISCORD_TOKEN=SEU_TOKEN_DO_DISCORD
   SPOTIFY_CLIENT_ID=SEU_CLIENT_ID_DO_SPOTIFY
   SPOTIFY_CLIENT_SECRET=SEU_CLIENT_SECRET_DO_SPOTIFY
   ```

### Executando o Bot

Para iniciar o bot, execute o seguinte comando:

```bash
python main.py
```

## 🤖 Comandos

Aqui estão os comandos disponíveis para interagir com o bot:

| Comando | Descrição | Exemplo |
|---|---|---|
| `$play <URL ou nome da música>` | Adiciona uma música à fila e começa a tocar. | `$play https://www.youtube.com/watch?v=dQw4w9WgXcQ` |
| | | `$play Never Gonna Give You Up` |
| | | `$play https://open.spotify.com/track/4cOdK2wGLETOMhOcdqokrA` |
| `$stop` | Para a reprodução e desconecta o bot do canal de voz. | `$stop` |
| `$skip` | Pula a música que está tocando no momento. | `$skip` |
| `$kasino` | Toca um clássico da música eletrônica nacional. | `$kasino` |

## 📝 Lista de Tarefas (To-Do)

- [ ] Adicionar comando para ver a fila de reprodução
- [ ] Adicionar comando para remover uma música da fila
- [ ] Adicionar comando para pausar e resumir a reprodução
- [ ] Adicionar suporte para mais plataformas (SoundCloud, etc.)
- [ ] Melhorar o tratamento de erros

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## 📄 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.