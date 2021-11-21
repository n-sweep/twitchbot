#/user/bin/env python3
# Twitch bot oauth handler

import asyncio
import aiohttp
import logging
import numpy as np


class OAuthHandler:
    def __init__(self, config):
        self.config = config
        self.loop = asyncio.get_event_loop()

    def validate(self):
        """
            Validate Access Token & log results
        """
        status, response = self.loop.run_until_complete(self.oauth_validate())

        logging.info('Validating token...')
        if status == 200:
            logging.info('Token valid.')
            return response
        elif status == 401: 
            logging.warning('Token invalid, attempting to refresh...')
            self.refresh()
            self.validate()
        else:
            logging.error('Something went wrong.')
            logging.error(f'Status: {status}')
            logging.error(str(response))
            return response

    def refresh(self):
        """
            Refresh Access Token and log results
        """
        status, response = self.loop.run_until_complete(self.oauth_refresh())

        if status == 200:
            self.config.update({
                'ACCESS_TOKEN': response['access_token'],
                'TOKEN_METADATA': response
                })
        else:
            logging.error('Something went wrong.')
            logging.error(f'Status: {status}')
            logging.error(str(response))

    async def oauth_validate(self):
        """
            OAuth call to twitch API to validate the existing access token
        """
        headers = {'Authorization': f'Bearer {self.config["ACCESS_TOKEN"]}'}
        async with aiohttp.ClientSession() as session:
            async with session.get('https://id.twitch.tv/oauth2/validate', headers=headers) as r:
                return (r.status, await r.json())

    async def oauth_refresh(self):
        """
            OAuth call to twitch API to refresh the access token
        """
        payload = {
            'grant_type': 'refresh_token',
            'refresh_token': self.config['TOKEN_METADATA']['refresh_token'],
            'client_id': self.config['CLIENT_ID'],
            'client_secret': self.config['CLIENT_SECRET']
        }
        async with aiohttp.ClientSession() as session:
            async with session.post('https://id.twitch.tv/oauth2/token', params=payload) as r:
                return (r.status, await r.json())


