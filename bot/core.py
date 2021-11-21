import sys
import json
import asyncio
import logging
from twitchio.ext import commands
from conf.handler import ConfigHandler
from auth.handler import OAuthHandler


class Bot(commands.Bot):

    def __init__(self, config_fp):
        self.loop = asyncio.get_event_loop()
        self.config = ConfigHandler(config_fp)

        # validate token
        self.auth = OAuthHandler(self.config)
        self.auth.validate()

        logging.info('Initializing Bot...')
        super().__init__(
            token=self.config.get('ACCESS_TOKEN'),
            nick=self.config.get('BOT_NICK'),
            prefix=self.config.get('PREFIX'),
            initial_channels=['#' + self.config.get('BROADCASTER_NAME')],
            loop=self.loop
        )

        self.load_cogs()

    def load_cogs(self):
        for c in self.config.get('COGS'): # ['maincog', 'admincog']
            ext = 'cogs.' + c
            self.load_module(ext)


if __name__ == '__main__':
    bot = Bot('conf/config.json')
    bot.run()
