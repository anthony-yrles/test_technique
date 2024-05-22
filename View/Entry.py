import tkinter as tk
from tkinter import Entry, StringVar


class CustomEntry:
    def __init__(self, parent, default_text, x, y, show=None):
        self.default_text = default_text
        self.frame = tk.Frame(parent, bg='white', bd=0, padx=0, pady=0, relief="flat")
        self.frame.place(x=x, y=y)
        self.entry_var = StringVar()
        self.entry = Entry(self.frame, textvariable=self.entry_var, width=20, font=("Arial", 20), insertbackground="red", bg="#0045ab", fg="white", relief="flat")
        self.entry.insert(0, default_text)
        self.entry.bind('<FocusIn>', self.on_entry_click)
        
        # Check if the text need to be hidden
        if show:
            self.entry.config(show=show)
            
        self.entry.pack()

    def on_entry_click(self, event):
        if self.entry.get() == self.default_text:
            self.entry.delete(0, tk.END)
            self.entry.config(fg='white') 

    def get_value(self):
        return self.entry_var.get()
    
    def get_frame(self):
        return self.frame

    def destroy_entry(self):
        self.entry.destroy()
        self.frame.destroy()