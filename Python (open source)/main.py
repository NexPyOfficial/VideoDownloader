import os
import sys
import subprocess
from yt_dlp import YoutubeDL
import tkinter as tk
from tkinter import messagebox, filedialog
from colorama import init, Fore, Style

# Inizializza colorama (necessario su Windows)
init(autoreset=True)

# === Funzioni comuni ===
def apri_cartella_output(tipo):
    output_dir = os.path.join(os.getcwd(), "Output", tipo)
    os.makedirs(output_dir, exist_ok=True)
    if os.name == "nt":
        os.startfile(output_dir)
    elif sys.platform == "darwin":
        subprocess.call(["open", output_dir])
    else:
        subprocess.call(["xdg-open", output_dir])

def scarica_video(url, tipo, risoluzione=None, playlist=False):
    output_dir = os.path.join(os.getcwd(), "Output", tipo)
    os.makedirs(output_dir, exist_ok=True)

    if tipo == "YouTube":
        quality_map = {
            "480": "bestvideo[height<=480][ext=mp4]+bestaudio[ext=m4a]/best[height<=480][ext=mp4]",
            "720": "bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[height<=720][ext=mp4]",
            "1080": "bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080][ext=mp4]",
        }
        formato = quality_map.get(risoluzione, quality_map["720"])
    else:  # TikTok
        formato = "bestvideo+bestaudio/best"

    opzioni = {
        'format': formato,
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
        'noplaylist': not playlist,
        'quiet': False,
    }

    # Se TikTok, aggiungi i cookies
    if tipo == "TikTok":
        cookies_path = os.path.join(os.getcwd(), "Settings", "cookie.txt")
        if os.path.isfile(cookies_path):
            opzioni['cookiefile'] = cookies_path
        else:
            raise FileNotFoundError(f"Il file cookie.txt non è stato trovato in /Settings. Percorso atteso: {cookies_path}")

    with YoutubeDL(opzioni) as ydl:
        ydl.download([url])

# === GUI ===
def avvia_download_gui(url, tipo, risoluzione, playlist):
    if not url:
        messagebox.showerror("Errore", "URL mancante.")
        return
    try:
        scarica_video(url, tipo, risoluzione, playlist)
        messagebox.showinfo("Successo", "Download completato con successo.")
        apri_cartella_output(tipo)
    except Exception as e:
        messagebox.showerror("Errore", f"Errore durante il download:\n{e}")

def apri_gui():
    root = tk.Tk()
    root.title("Video Downloader")

    tk.Label(root, text="Scegli sorgente:").pack(pady=5)
    tipo_var = tk.StringVar(value="YouTube")
    tk.Radiobutton(root, text="YouTube", variable=tipo_var, value="YouTube").pack()
    tk.Radiobutton(root, text="TikTok", variable=tipo_var, value="TikTok").pack()

    tk.Label(root, text="Inserisci URL:").pack(pady=5)
    url_entry = tk.Entry(root, width=50)
    url_entry.pack()

    qualita_var = tk.StringVar(value="720")
    qualita_frame = tk.Frame(root)
    qualita_frame.pack()

    tk.Label(qualita_frame, text="Qualità (solo per YouTube):").pack()
    for q in [("480p", "480"), ("720p", "720"), ("1080p", "1080")]:
        tk.Radiobutton(qualita_frame, text=q[0], variable=qualita_var, value=q[1]).pack(anchor="w")

    playlist_var = tk.BooleanVar()
    tk.Checkbutton(root, text="Scarica come playlist (se applicabile)", variable=playlist_var).pack(pady=5)

    def avvia():
        avvia_download_gui(
            url=url_entry.get().strip(),
            tipo=tipo_var.get(),
            risoluzione=qualita_var.get(),
            playlist=playlist_var.get()
        )

    tk.Button(root, text="Scarica", command=avvia, bg="green", fg="white").pack(pady=10)
    root.mainloop()

# === Console ===
def scegli_risoluzione():
    print(f"\n{Style.BRIGHT}{Fore.CYAN}Seleziona la qualità da scaricare (solo YouTube):")
    print(f"{Fore.YELLOW}[1] 480p (più leggero)")
    print(f"{Fore.YELLOW}[2] 720p (buona qualità)")
    print(f"{Fore.YELLOW}[3] 1080p (richiede FFmpeg)")
    scelta = input(">>>: ").strip()
    return {"1": "480", "2": "720", "3": "1080"}.get(scelta, "720")

def console_download():
    print(f"\n{Style.BRIGHT}{Fore.CYAN}Sorgente video:")
    print(f"{Fore.YELLOW}[1] YouTube")
    print(f"{Fore.YELLOW}[2] TikTok")
    tipo_scelto = input(">>>: ").strip()
    tipo = "YouTube" if tipo_scelto == "1" else "TikTok"

    url = input(f"{Fore.YELLOW}Inserisci il link: ").strip()
    if not url:
        print(f"{Fore.RED}❌ URL non valido.")
        return

    playlist = False
    if tipo == "YouTube":
        playlist = input(f"{Fore.YELLOW}Vuoi scaricare una playlist? (s/n): ").lower().strip() == "s"
        risoluzione = scegli_risoluzione()
    else:
        risoluzione = None

    try:
        print(f"\n{Fore.BLUE}⏬ Download in corso...\n")
        scarica_video(url, tipo, risoluzione, playlist)
        print(f"\n{Fore.GREEN}✅ Download completato con successo.")
        apri_cartella_output(tipo)
    except Exception as e:
        print(f"\n{Fore.RED}❌ Errore durante il download: {e}")

# === Main ===
def main():
    print(f"\n{Style.BRIGHT}{Fore.CYAN}=== Video Downloader ===")
    print(f"{Fore.YELLOW}[1] Modalità console")
    print(f"{Fore.YELLOW}[2] Modalità GUI")
    scelta = input(">>>: ").strip()

    if scelta == "2":
        apri_gui()
    else:
        console_download()

if __name__ == "__main__":
    main()
