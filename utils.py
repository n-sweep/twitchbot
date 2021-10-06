#!/usr/bin/env python
# Utility library

import asyncio


class Timer:
    """
    An Async-safe timer for suspending actions.
    """
    def __init__(self, timeout=0, callback=None):
        self._timeout = timeout
        self._callback = callback
        self._task = asyncio.ensure_future(self._job())
    
    async def _job(self):
        await asyncio.sleep(self._timeout)
        await self._callback()
    
    def cancel(self):
        try:
            self._task.cancel()
        except Exception as e:
            print(e)


class Periodic:
    """
    An Async-safe timer for performing actions at set intervals.
    """
    def __init__(self, timeout, callback):
        self._timeout = timeout
        self._callback = callback
        self._task = asyncio.ensure_future(self._job())
    
    async def _job(self):
        while True:
            await self._callback()
            await asyncio.sleep(self._timeout)
    
    def cancel(self):
        try:
            self._task.cancel()
        except Exception as e:
            print(e)
