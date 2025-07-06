import os
import sys
import zipfile
import shutil
import subprocess
from pathlib import Path

# Auto-elevazione a admin su Windows
def is_admin():
    import ctypes
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if os.name == "nt" and not is_admin():
    import ctypes
    # Rilancio lo script come admin e termino quello attuale
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

print("""
 .----------------.  .----------------.  .----------------.  .----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| | ____   ____  | || |  ________    | || |     ____     | || | _____  _____ | || | ____  _____  | || |   _____      | || |     ____     | || |      __      | || |  ________    | || |  _________   | || |  _______     | |
| ||_  _| |_  _| | || | |_   ___ `.  | || |   .'    `.   | || ||_   _||_   _|| || ||_   \|_   _| | || |  |_   _|     | || |   .'    `.   | || |     /  \     | || | |_   ___ `.  | || | |_   ___  |  | || | |_   __ \    | |
| |  \ \   / /   | || |   | |   `. \ | || |  /  .--.  \  | || |  | | /\ | |  | || |  |   \ | |   | || |    | |       | || |  /  .--.  \  | || |    / /\ \    | || |   | |   `. \ | || |   | |_  \_|  | || |   | |__) |   | |
| |   \ \ / /    | || |   | |    | | | || |  | |    | |  | || |  | |/  \| |  | || |  | |\ \| |   | || |    | |   _   | || |  | |    | |  | || |   / ____ \   | || |   | |    | | | || |   |  _|  _   | || |   |  __ /    | |
| |    \ ' /     | || |  _| |___.' / | || |  \  `--'  /  | || |  |   /\   |  | || | _| |_\   |_  | || |   _| |__/ |  | || |  \  `--'  /  | || | _/ /    \ \_ | || |  _| |___.' / | || |  _| |___/ |  | || |  _| |  \ \_  | |
| |     \_/      | || | |________.'  | || |   `.____.'   | || |  |__/  \__|  | || ||_____|\____| | || |  |________|  | || |   `.____.'   | || ||____|  |____|| || | |________.'  | || | |_________|  | || | |____| |___| | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
""")

print("[0] pip\n[1] pip3\n[2] Alternative")
print("[INFO] FFmpeg non verrà installato automaticamente, segui un tutorial per installarlo, così potrai assicurarti che tutto vada alla perfezione")
c = input(">>>: ")

# Pacchetti da installare
packages = "yt-dlp colorama requests"

if c == "0":
    os.system(f"pip install {packages}")
elif c == "1":
    os.system(f"pip3 install {packages}")
elif c == "2":
    os.system(f"py -m pip install {packages}")

# Verifica che requests e colorama siano installati
try:
    import requests
    from colorama import init, Fore, Style
except ImportError:
    print("[ERROR] Moduli mancanti. Per favore installali manualmente con 'pip install requests colorama'")
    sys.exit(1)

# Inizializza colorama per i colori su Windows
init(autoreset=True)

print(f"{Fore.GREEN}Fatto!")
