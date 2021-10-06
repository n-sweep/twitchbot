#!/usr/bin/env python
# A Twitch Bot

import os
from bot.core import Bot

def main():
    bot = Bot('conf/config.json')
    bot.run()

if __name__ == '__main__':
    main()
