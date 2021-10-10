#!/usr/bin/env python3
# A process for validating and refreshing twitch tokens

import os
import json
import asyncio
from oauth import validate_access_token, refresh_token

d = os.path.dirname(os.path.realpath(__file__))
fp = os.path.join(d, '../conf/config.json')


async def commit_refresh(metadata):
    with open(fp, 'r+') as f:
        config = json.load(f)
        config['ACCESS_TOKEN'] = metadata['access_token']
        config['TOKEN_METADATA'] = metadata
        f.seek(0)
        json.dump(config, f, indent=4)
        f.truncate()
    print('Token Refreshed')


async def validate():
    v = await validate_access_token()
    if v.status == 401:
        print('invalid, refreshing...')
        r = await refresh_token()
        if r is int:
            print('error', r)
        else:
            await commit_refresh(r)
    else:
        print('current token is valid')


async def main():
    await validate()


if __name__ == '__main__':
    asyncio.run(main())
