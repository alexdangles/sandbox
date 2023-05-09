:: one file
:: pyinstaller -i app.ico -Fy --noconsole --add-data app.json;. app.py

:: no cosole
pyinstaller -i app.ico -y --noconsole --add-data app.db;. --add-data app.json;. app.py