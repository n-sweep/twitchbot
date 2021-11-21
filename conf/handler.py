#/usr/bin/env python3
# A JSON configuration handler
# for twitch.tv chatbot

import json


class ConfigHandler(dict):
    def __init__(self, fp):
        self.config = None
        self.fp = fp
        self.load_config()

    def load_config(self):
        """ Load config json into class attribute """
        with open(self.fp, 'r+') as f:
            for k, v in json.load(f).items():
                self[k] = v

    def save_config(self):
        """ Save current config to json """
        with open(self.fp, 'r+') as f:
            f.seek(0)
            json.dump(self, f, indent=4)
            f.truncate()
    
    def update(self, d):
        for k, v in d.items():
            self[k] = v
            self.save_config()


