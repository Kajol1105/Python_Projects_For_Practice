import pyperclip
import keyboard
import threading
import time
import tkinter as tk
from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw

clipboard_history = []
last_text = ""

# 📋 Clipboard Tracker
def track_clipboard():
    global last_text
    while True:
        text = pyperclip.paste()
        if text != last_text and text.strip() != "":
            clipboard_history.append(text)
            last_text = text
            print("Copied:", text)
        time.sleep(1)

# 🖥️ Popup UI
def show_popup():
    window = tk.Tk()
    window.title("ClipStack")
    window.geometry("400x300")

    listbox = tk.Listbox(window, font=("Arial", 12))
    listbox.pack(fill=tk.BOTH, expand=True)

    for item in reversed(clipboard_history[-20:]):
        listbox.insert(tk.END, item[:50])

    def on_select(event):
        selected = listbox.get(listbox.curselection())
        pyperclip.copy(selected)
        window.destroy()

    listbox.bind("<<ListboxSelect>>", on_select)

    window.mainloop()

# ⌨️ Shortcut Listener
def start_keyboard_listener():
    keyboard.add_hotkey('ctrl+shift+v', show_popup)
    keyboard.wait()

# 🟢 System Tray Icon
def create_image():
    img = Image.new('RGB', (64, 64), color='black')
    d = ImageDraw.Draw(img)
    d.rectangle((16, 16, 48, 48), fill='white')
    return img

def on_exit(icon, item):
    icon.stop()

def setup_tray():
    icon = Icon("ClipStack", create_image(), menu=Menu(
        MenuItem("Exit", on_exit)
    ))
    icon.run()

# 🧵 Run everything in threads
threading.Thread(target=track_clipboard, daemon=True).start()
threading.Thread(target=start_keyboard_listener, daemon=True).start()

# Start tray (main thread)
setup_tray()
