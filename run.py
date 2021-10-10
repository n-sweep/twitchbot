#!/usr/bin/env python
# A Twitch Bot

import os
from bot.core import Bot

d = os.path.dirname(os.path.realpath(__file__))
fp = os.path.join(d, 'conf/config.json')


def main():
    bot = Bot(fp)
    bot.run()


if __name__ == '__main__':
    main()
