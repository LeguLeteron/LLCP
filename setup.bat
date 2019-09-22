rd /s /q build
rd /s /q dist

pyinstaller -i icon.ico -n llcp --onefile main.py