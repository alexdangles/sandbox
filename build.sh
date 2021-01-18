#!/bin/bash
pyinstaller -wy --add-data 'config.json;.' app.py