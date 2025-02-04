import tkinter as tk
from tkinter import scrolledtext
import subprocess
import threading

def run_snort():
    """Execute Snort and capture output in real time."""
    process = subprocess.Popen(
        ['snort', '-A', 'console', '-q', '-c', '/etc/snort/snort.conf', '-i', 'eth0'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    for line in process.stdout:
        log_text.insert(tk.END, line)
        log_text.see(tk.END)

# Interface utilisateur
root = tk.Tk()
root.title("Snort IDS Interface")
root.geometry("600x400")

log_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20)
log_text.pack(pady=10)

start_button = tk.Button(root, text="Lancer Snort", command=lambda: threading.Thread(target=run_snort, daemon=True).start())
start_button.pack()

root.mainloop()
