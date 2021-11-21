#!/usr/bin/env python3
# A Twitch Bot

import os
import logging
from datetime import datetime
from bot.core import Bot

t = datetime.today()
d = os.path.dirname(os.path.realpath(__file__))
config_fp = os.path.join(d, 'conf/config.json')
log_fp = os.path.join(d,'logs/test.log')
#log_fp = os.path.join(d, f'logs/{t.year}_{t.month}_{t.day}.log')

def main():
    logging.basicConfig(filename=log_fp, level=logging.INFO, filemode='a')

    bot = Bot(config_fp)
    bot.run()


if __name__ == '__main__':
    main()

