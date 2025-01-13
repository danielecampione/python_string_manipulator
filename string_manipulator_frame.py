import tkinter as tk
from tkinter import ttk

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

def close_window():
    root.destroy()

def update_label_uppercase(*args):
    strInputString = inputString.get()
    if strInputString:
        labelUpperCase.config(text=f"In maiuscolo: {strInputString.upper()}")
    else:
        labelUpperCase.config(text="In maiuscolo: ")

def update_label_lowercase(*args):
    strInputString = inputString.get()
    if strInputString:
        labelLowerCase.config(text=f"In minuscolo: {strInputString.lower()}")
    else:
        labelLowerCase.config(text="In minuscolo: ")

def update_label_capitalize(*args):
    strInputString = inputString.get()
    if strInputString:
        labelCapitalize.config(text=f"Capitalizzato: {strInputString.capitalize()}")
    else:
        labelCapitalize.config(text="Capitalizzato: ")

def update_label_title(*args):
    strInputString = inputString.get()
    if strInputString:
        labelTitle.config(text=f"Titolo: {strInputString.title()}")
    else:
        labelTitle.config(text="Titolo: ")

# Creazione della finestra principale
root = tk.Tk()
root.title("String manipulator")

# Variabile per il testo in input
inputString = tk.StringVar()
inputString.trace_add('write', update_label_uppercase)
inputString.trace_add('write', update_label_lowercase)
inputString.trace_add('write', update_label_capitalize)
inputString.trace_add('write', update_label_title)

# Creazione di una barra testuale per inserire il nome
inputString_entry = ttk.Entry(root, textvariable=inputString, font=("Helvetica", 16))
inputString_entry.pack(padx=20, pady=10)

# Creazione di un'etichetta con il messaggio "In maiuscolo: "
labelUpperCase = ttk.Label(root, text="In maiuscolo: ", font=("Helvetica", 10))
labelUpperCase.pack(padx=20, pady=20)

# Creazione di un'etichetta con il messaggio "In minuscolo: "
labelLowerCase = ttk.Label(root, text="In minuscolo: ", font=("Helvetica", 10))
labelLowerCase.pack(padx=20, pady=20)

# Creazione di un'etichetta con il messaggio "In minuscolo: "
labelCapitalize = ttk.Label(root, text="Capitalizzato: ", font=("Helvetica", 10))
labelCapitalize.pack(padx=20, pady=20)

# Creazione di un'etichetta con il messaggio "In minuscolo: "
labelTitle = ttk.Label(root, text="Titolo: ", font=("Helvetica", 10))
labelTitle.pack(padx=20, pady=20)

# Creazione del pulsante "Chiudi"
close_button = ttk.Button(root, text="Chiudi", command=close_window)
close_button.pack(pady=10)

# Posizionamento della finestra al centro del desktop
center_window(root)

# Creazione dello stile
style = ttk.Style()

# Avvio del loop principale della finestra
root.mainloop()
