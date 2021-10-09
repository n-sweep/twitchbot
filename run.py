#!/usr/bin/env python
# A Twitch Bot

import os
from bot.core import Bot

def main():
    d = os.path.dirname(os.path.realpath(__file__))
    fp = os.path.join(d, 'conf/config.json')
    print(fp)
    bot = Bot(fp)
    bot.run()

if __name__ == '__main__':
    main()
