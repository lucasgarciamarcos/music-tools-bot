import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from utils import validate_input
from queue_server import QueueServer
from spotify_search import SpotifySimple

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações do bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

# Dicionário para armazenar QueueServer por servidor
queues = {}

def get_queue_server(guild_id, bot, context):
    """Obtém ou cria uma QueueServer para o servidor"""
    if guild_id not in queues:
        queues[guild_id] = QueueServer(bot, context)
    return queues[guild_id]

@bot.event
async def on_ready():
    print(f'{bot.user} está online')

@bot.command(name='kasino')
async def kasino(context):
    # URL exclusivo kasino
    KASINO = "https://youtu.be/LCDaw0QmQQc?si=s9E1Z9QNThLdL9qc"
    await play(context, KASINO)
    await context.send("SABADASSO")

@bot.command(name='play')
async def play(context, *, url):
    # Verifica se o usuário está em um canal de voz
    if not context.author.voice:
        await context.send("Você precisa estar em um canal de voz")
        return
    
    # Conecta ao canal de voz do usuário
    channel = context.author.voice.channel
    voice_client = context.voice_client
    
    if voice_client is None:
        voice_client = await channel.connect()
    elif voice_client.channel != channel:
        await voice_client.move_to(channel)
    
    try:
        # Valida a entrada
        url = url.strip()
        search_type = validate_input(url)

        if search_type == 'spotify':
            # Se for Spotify, converte para YouTube
            spotify = SpotifySimple(os.getenv('SPOTIFY_CLIENT_ID'), os.getenv('SPOTIFY_CLIENT_SECRET'))

            # Qualquer link - sempre retorna array
            tracks = spotify.get_tracks_from_link(url)

            for track in tracks:
                # Trata Playlist ou Album
                url = f"ytsearch:{track['music']} - {track['artist']}"
                actual_queue = get_queue_server(context.guild.id, bot, context)
                await actual_queue.add_queue(url)

        elif search_type == 'query':
            # Se for texto faz uma busca no YouTube
            url = f'ytsearch1:{url}'
            print(f"Buscando no yt: {url}")
        
            # Instancia da fila
            actual_queue = get_queue_server(context.guild.id, bot, context)
            await actual_queue.add_queue(url)
    except Exception as e:
        await context.send(f"Erro: {str(e)}")

@bot.command(name='stop')
async def stop(context):
    voice_client = context.voice_client

    # Se o bot estiver tocando ele é parado e desconectado.
    if voice_client and voice_client.is_connected():
        if voice_client.is_playing():
            voice_client.stop()
        await voice_client.disconnect()
        await context.send('Acabou a festa, então o bot saiu do canal')
    else:
        await context.send('O bot não está em um canal de voz')

if __name__ == "__main__":
    TOKEN = os.getenv('DISCORD_TOKEN')
    
    if not TOKEN:
        print("Token do Discord não encontrado")
        exit(1)
    
    bot.run(TOKEN)