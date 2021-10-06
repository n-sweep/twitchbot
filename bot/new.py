import json
from twitchio.ext import commands

class Bot(commands.Bot):

    def __init__(self, conf_fp):
        with open(conf_fp) as f:
            self.config = json.load(f)
        super().__init__(
            token=self.config.get('ACCESS_TOKEN'),
            nick=self.config.get('BOT_NICK'),
            prefix=self.config.get('PREFIX'),
            initial_channels=['#' + self.config.get('BROADCASTER_NAME')]
        )

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')

    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f'Hello {ctx.author.name}!')

bot = Bot('config.json')
bot.run()
