#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Thank you @LazyDeveloperr 

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "BewafaAngelPriya",
        bot_token=5857332380:AAHkdVTkvQ2K1GbQZ2etJW_q_j4gX4mvxbI
        api_id=28829019
        api_hash=f5d533a4fd03c579f020f0da3ba37c1e
        plugins=plugins
    )
    Config.AUTH_USERS.add(1484670284)
    app.run()
