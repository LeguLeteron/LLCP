rd /s /q build
rd /s /q dist

pyinstaller -i icon.ico -n LeguLeteron --onefile main.py
pause