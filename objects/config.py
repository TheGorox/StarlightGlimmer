import json
import logging
import os
import sys

log = logging.getLogger(__name__)


def clamp(n, lowest, highest):
    return max(lowest, min(highest, n))


class Config:
    def __init__(self):
        if not os.path.isfile('config/config.json'):
            if not os.path.isfile('config/config.json.example'):
                log.critical("config/config.json could not be found! Please get the example copy from GitHub and "
                             "rename it to config.json!")
                sys.exit(1)
            else:
                log.critical("config/config.json could not be found! (Did you rename config/config.json.example to "
                             "config/config.json yet?)")
                sys.exit(1)

        self.config_file = "config/config.json"
        with open(self.config_file, "r+") as j:
            data = json.load(j)

        self.token = data.get('token', None)
        self.prefix = data.get('prefix', "g!")
        self.name = data.get('name', 'Starlight Glimmer')
        self.invite = data.get('invite', "https://discordapp.com/oauth2/authorize?&client_id=405480380930588682&scope"
                                         "=bot&permissions=35840")
        self.pz_api_key = data.get('pixelzone_api_key', None)

        self.preview_h = clamp(data.get('preview_height', 240), 0, 896)
        self.preview_w = clamp(data.get('preview_width', 400), 0, 896)
        self.max_templates_per_guild = clamp(data.get('max_templates_per_guild'), 1,
                                             data.get('max_templates_per_guild'))
        self.max_template_name_length = clamp(data.get('max_template_name_length'), 1, 64)

        self.logging_channel_id = data.get('logging_channel_id', None)
        self.debug = data.get('debug', False)
        self.channel_log_guild_renames = data.get('channel_log_guild_renames', False)
        self.channel_log_guild_joins = data.get('channel_log_guild_joins', False)
        self.channel_log_guild_kicks = data.get('channel_log_guild_kicks', False)

        if self.token is None:
            log.critical("No bot token was specified!")
            sys.exit(1)
