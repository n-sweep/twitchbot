#!/usr/bin/env python
# A Twitch Bot

import os
import asyncio
from bot.core import Bot
from auth.endpoint import Endpoint

d = os.path.dirname(os.path.realpath(__file__))
fp = os.path.join(d, 'conf/config.json')


def main():
    loop = asyncio.get_event_loop()
    ept = Endpoint(fp)
    bot = Bot(fp)
    loop.create_task(ept.run())
    bot.run()


if __name__ == '__main__':
    main()
