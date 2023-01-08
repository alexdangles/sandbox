#!/bin/sh
pyinstaller --onefile --noconsole --noconfirm  app.py
cp app.json dist