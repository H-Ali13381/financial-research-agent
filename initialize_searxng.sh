#!/bin/bash
sudo -H -u searxng -i bash -c '
cd /usr/local/searxng/searxng-src &&
export SEARXNG_SETTINGS_PATH="/etc/searxng/settings.yml" &&
python searx/webapp.py
'