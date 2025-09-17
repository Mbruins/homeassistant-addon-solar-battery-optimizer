#!/usr/bin/env bash
set -e

CONFIG_PATH=/data/options.json
python3 -u /app/main.py --config $CONFIG_PATH
