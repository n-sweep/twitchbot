#!/usr/bin/env python
# A Twitch bot cog!

import twitchio
from twitchio.ext import commands


class AdminCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

def prepare(bot):
    bot.add_cog(AdminCog(bot))
