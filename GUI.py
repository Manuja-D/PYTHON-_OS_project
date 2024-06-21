import tkinter as tk
from tkinter import ttk

#A simple window
window = tk.Tk()
window.title('demo')
window.geometry('400x300')

#gui

window.mainloop()

note_entry = tk.Text(window)
note_entry.pack()

import sqlite3

def save():
    note = note_entry.get("1.0",tk.END)
    conn = sqlite3.conect("notes.db")
    cursor = conn.cursor()
    