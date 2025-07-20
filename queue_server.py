from collections import deque
from source_client import YTDLSource

class QueueServer:
    def __init__(self, bot, context):
        """Inicializa o servidor de fila com o bot e o contexto"""
        self.queue = deque()
        self.is_playing = False
        self.bot = bot
        self.context = context

    async def add_queue(self, url):
        """Adiciona uma música à fila"""
        self.queue.append(url)
        if not self.is_playing:
            await self.next()
        else:
            await self.context.send(f"Coloquei seu item na fila.")

    def after_playing(self, error):
        """Toca a próxima música na fila após a atual terminar"""
        if error:
            print(f'Player error: {error}')
            return

        self.is_playing = False
        self.bot.loop.create_task(self.next())

    async def next(self):
        """Inicia a reprodução da música atual na fila"""
        
        # Por segurança, verifica se a fila não está vazia
        if not self.queue:
            return
        
        if self.is_playing:
            self.context.voice_client.stop()

        # Trata o proximo item da fila
        url = self.queue.popleft()

        try:
            # Baixa e prepara o áudio
            player = await YTDLSource.from_url(url, loop=self.bot.loop)

            # Reproduz a música
            self.is_playing = True
            self.context.voice_client.play(player, after=self.after_playing)
            await self.context.send(f"Playing: **{player.title}**")

        except Exception as e:
            self.is_playing = False
            await self.context.send(f"Erro: {str(e)}")
            
            # Tenta iniciar a próxima música na fila
            await self.next()