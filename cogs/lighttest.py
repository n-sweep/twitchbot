#!/usr/bin/env python3
# Testing python-kasa

import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

from time import sleep
import asyncio
from time import sleep
from kasa import Discover


class LightCog():
    def __init__(self):
        asyncio.run(self.get_devices())
        self.ol0 = self.devs['office light 1']['dev']
        self.ol1 = self.devs['office light A']['dev']

    async def get_devices(self):
        output = {}
        devices = await Discover.discover()
        for addr, dev in devices.items():
            await dev.update()
            output[dev.alias] = {'addr': addr, 'dev': dev}
        
        self.devs = output


if __name__ == '__main__':
    lc = LightCog()
    asyncio.run(lc.ol0.turn_off())
    sleep(1)
    asyncio.run(lc.ol0.turn_on())
