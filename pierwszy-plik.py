import tkinter as tk
import platform
from datetime import datetime

def update_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    time_label.config(text=current_time)
    root.after(1000, update_time)


# Kilka linijek w jednej zmiennej - informacje o systemie
system_info = f"""
System: {platform.system()}
Wersja: {platform.release()}
Architektura: {platform.machine()}
Python: {platform.python_version()}
"""

root = tk.Tk()
root.title("Zegar i system")

# Tekst z opisem
info_label = tk.Label(root, text="Opis mojej aplikacji")
info_label.pack(pady=20)

# Tekst z opisem systemu
system_label = tk.Label(root, text=system_info)
system_label.pack(pady=20)

# Tekst z zegarem
time_label = tk.Label(root)
time_label.pack(pady=20)

# Włączenie funkcji liczącej czas
update_time()

root.mainloop()