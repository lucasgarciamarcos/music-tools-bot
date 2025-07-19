import discord
import os
from source_client import YTDLSource
from discord.ext import commands
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações do bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

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
async def play(context, url):
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
    
    # Para qualquer música atual
    if voice_client.is_playing():
        voice_client.stop()
    
    try:
        await context.send("Carregando...")
        
        # Baixa e prepara o áudio
        player = await YTDLSource.from_url(url, loop=bot.loop)
        
        # Reproduz a música
        voice_client.play(player)
        
        await context.send(f"Playing: **{player.title}**")
        
    except Exception as e:
        await context.send(f"Erro: {str(e)}")

@bot.command(name='tocar')
async def tocar(context, *, query):
    if not context.author.voice:
        await context.send ('Você precisa estar em um canal de voz')
        return

    channel = context.author.voice.channel
    voice_client = context.voice_client

    if voice_client is None:
        voice_client = await channel.connect()
    elif voice_client.channel != channel:
        await voice_client.move_to(channel)

    if voice_client.is_playing():
        voice_client.stop()

    try:
        await context.send("Buscando o fado, só um minuto...")

        search_query = f'ytsearch:{query.strip()}'
        player = await YTDLSource.from_url(search_query, loop=bot.loop)

        voice_client.play(player)
        await context.send(f"Coloquei pra tocar essa pedrada: **{player.title}**")

    except Exception as e:
        await context.send(f"Deu ruim!: {str(e)}")

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