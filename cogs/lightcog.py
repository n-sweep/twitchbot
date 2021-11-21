#!/usr/bin/env python3
# A cog to interface with TP Link Kasa smart devices

import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

import logging
import asyncio
from time import sleep

from kasa import Discover
from twitchio.ext import commands


class LightCog():
    def __init__(self):
        asyncio.run(self.get_devices())
        self.l0 = self.devs['office light 1']['dev']
        self.l1 = self.devs['office light A']['dev']

    async def get_devices(self):
        output = {}
        devices = await Discover.discover()
        for addr, dev in devices.items():
            await dev.update()
            output[dev.alias] = {'addr': addr, 'dev': dev}
        
        self.devs = output

    @commands.command(name='light')
    async def light(self, ctx):
        await self.l0.turn_off()
        await asyncio.sleep(1)
        await self.l0.turn_on()


def prepare(bot):
    bot.add_cog(LightCog(bot))

