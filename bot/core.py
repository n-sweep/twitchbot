#!/usr/bin/env python
# Twitch bot guts

import os
import sys
import json
import twitchio
from threading import local
# from twitchio import webhook
from random import choice, randint
from asyncio import sleep
from twitchio.ext import commands
from twitchio.errors import AuthenticationError

sys.path.insert(0, os.path.abspath('..'))

from utils import Timer, Periodic


light_colors = {
    'red': 1,
    'orange': 25,
    'yellow': 50,
    'green': 125,
    'blue': 220,
    'purple': 300
}

class Bot(commands.Bot):

    config = None
    light_timer = None
    discord_timer = None
    session_msgs = 0
    party_switch = False
    secrets = []

    def __init__(self, config_fp):
        # Set config filepath & load config
        self.conf_fp = config_fp
        self.load_config()

        # Pass in credentials
        super().__init__(
            token=self.config.get('ACCESS_TOKEN'),
            nick=self.config.get('BOT_NICK'),
            prefix=self.config.get('PREFIX'),
            initial_channels=['#' + self.config.get('BROADCASTER_NAME')]
        )

        self.load_cogs()
        self.discord_timer = Periodic(1200, self.discord_periodic)


    def load_cogs(self):
        for c in self.config.get('COGS'): # ['maincog', 'admincog']
            ext = 'cogs.' + c
            self.load_module(ext)

    def load_config(self):
        'Loads our json config file based on filepath given on bot instantiation'
        with open(self.conf_fp, 'r+') as f:
            self.config = json.load(f)

    # async def close(self):
    #     print('closing...')
    #     await super().close()
    
    async def discord_periodic(self):
        if self.session_msgs < 10:
            return
        link = self.config.get('DISCORD_LINK')
        txt = f"Our Discord server is open for business! {link}"
        ws = self._ws
        await ws.send_privmsg('#' + self.config.get('BROADCASTER_NAME'),txt)
        self.session_msgs = 0

    @commands.command(name='today')
    async def today(self, ctx, *args):
        'Will return or set the value of the [today] config attribute'
        if len(args):
            if ctx.author.id == self.config.get('BROADCASTER_ID'):
                # If an admin had provided arguments with this command, update the command value to reflect the new arguemnts.
                with open(self.conf_fp, 'r+') as f:
                    conf = json.load(f)
                    conf['TODAY'] = ' '.join(args)
                    f.seek(0)
                    json.dump(conf, f, indent=4)
                    f.truncate()
                self.load_config()
                await ctx.send("Command [!today] set successfully!")
            else:
                await ctx.send(f"Sorry @{ctx.author.name}, only an admin can reset the value of this command.")
        else:
            await ctx.send(self.config.get('TODAY'))
    
    @commands.command(name='music', aliases=['tunes'])
    async def music(self, ctx, *args):
        'Will return or set the value of the [music] config attribute'
        if len(args):
            if ctx.author.id == self.config.get('BROADCASTER_ID'):
                # If an admin had provided arguments with this command, update the command value to reflect the new arguemnts.
                with open(self.conf_fp, 'r+') as f:
                    conf = json.load(f)
                    conf['MUSIC'] = ' '.join(args)
                    f.seek(0)
                    json.dump(conf, f, indent=4)
                    f.truncate()
                self.load_config()
                await ctx.send("Command [!music] set successfully!")
            else:
                await ctx.send(f"Sorry @{ctx.author.name}, only an admin can reset the value of this command.")
        else:
            await ctx.send(self.config.get('MUSIC'))

