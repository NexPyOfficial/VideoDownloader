# 🎬 YouTube Video Downloader (YT-DLP + Termcolor)

Un semplice script Python da terminale per scaricare video, audio o entrambi da YouTube in pochi secondi.  
✅ Compatibile con Windows (testato), macOS e Linux.

---

## 🚀 Funzionalità

- ✅ Scarica solo video (senza audio)  
- ✅ Scarica solo audio (MP3)  
- ✅ Scarica video + audio (qualità massima)  
- ✅ Salva i file nella cartella `Output`  
- ✅ Apre automaticamente la cartella al termine (Windows)  
- ✅ Interfaccia a colori nel terminale  

---

## 🧰 Requisiti

- Python 3.7+  
- pip  
- yt-dlp  
- termcolor  
- **FFmpeg** (obbligatorio per unire video/audio e convertire in MP3)  

---

## ⚙️ Installazione delle dipendenze Python

Apri il terminale e digita:

```bash
pip install yt-dlp termcolor

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

🧱 Come installare FFmpeg su Windows (passaggi completi)
⚠️ FFmpeg è obbligatorio per:

Unire video e audio (opzione 3)

Convertire audio in MP3 (opzione 2)

Passaggi dettagliati:
Apri il browser e cerca “FFmpeg Windows download” oppure vai a:
https://www.gyan.dev/ffmpeg/builds/

Scarica il file ffmpeg-release-essentials.zip.

Estrai l’archivio in una cartella semplice, ad esempio:

C:\ffmpeg
Verifica che all’interno ci sia la cartella bin con il file ffmpeg.exe, es:

C:\ffmpeg\bin\ffmpeg.exe
Aggiungi C:\ffmpeg\bin al PATH di sistema:

Premi Win + S e cerca “variabili d’ambiente”

Clicca su “Modifica le variabili d’ambiente del sistema”

Clicca su Variabili d’ambiente...

Seleziona la variabile Path sotto Variabili di sistema, clicca su Modifica

Clicca su Nuovo e inserisci:

C:\ffmpeg\bin
Conferma tutto con OK.

Chiudi e riapri il terminale.

Verifica l’installazione con:

ffmpeg -version
Se appare la versione, FFmpeg è installato correttamente!

▶️ Utilizzo dello script
Esegui lo script Python:

python main.py
Ti verrà chiesto:

L’URL del video YouTube da scaricare

Che tipo di download vuoi fare:

1: Solo video (senza audio)

2: Solo audio (MP3)

3: Video + Audio (massima qualità)

📁 I file saranno salvati nella cartella Output. Su Windows, la cartella si apre automaticamente al termine.
