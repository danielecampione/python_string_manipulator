import tkinter as tk
from tkinter import ttk, scrolledtext
from collections import Counter
import unicodedata
import re
from functools import reduce
from string import Template
import textwrap

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

def close_window():
    root.destroy()

def update_labels(*args):
    strInputString = inputString.get()
    if strInputString:
        labelUpperCase.config(text=f"In maiuscolo: {strInputString.upper()}")
        labelLowerCase.config(text=f"In minuscolo: {strInputString.lower()}")
        labelCapitalize.config(text=f"Capitalizzato: {strInputString.capitalize()}")
        labelTitle.config(text=f"Titolo: {strInputString.title()}")
        labelSwapCase.config(text=f"Swapcase: {strInputString.swapcase()}")
        labelStrip.config(text=f"Strip: {strInputString.strip()}")
        labelReplace.config(text=f"Replace 'a' con 'X': {strInputString.replace('a', 'X')}")
        labelSplit.config(text=f"Split: {strInputString.split()}")
        labelJoin.config(text=f"Join: {'-'.join(strInputString.split())}")
        labelCount.config(text=f"Count 'a': {strInputString.count('a')}")
        labelFind.config(text=f"Find 'mondo': {strInputString.find('mondo')}")
        labelStartswith.config(text=f"Startswith 'ciao': {strInputString.startswith('ciao')}")
        labelEndswith.config(text=f"Endswith 'mondo': {strInputString.endswith('mondo')}")
        labelIsalpha.config(text=f"Isalpha: {strInputString.isalpha()}")
        labelIsdigit.config(text=f"Isdigit: {strInputString.isdigit()}")
        labelIsalnum.config(text=f"Isalnum: {strInputString.isalnum()}")
        labelIsspace.config(text=f"Isspace: {strInputString.isspace()}")
        labelIslower.config(text=f"Islower: {strInputString.islower()}")
        labelIsupper.config(text=f"Isupper: {strInputString.isupper()}")
        labelIstitle.config(text=f"Istitle: {strInputString.istitle()}")
        labelZfill.config(text=f"Zfill (10): {strInputString.zfill(10)}")
        tabella = str.maketrans("ao", "ou")
        labelTranslate.config(text=f"Translate: {strInputString.translate(tabella)}")
        labelReSub.config(text=f"Re.sub: {re.sub(r'\d+', 'NUMERO', strInputString)}")
        labelFormat.config(text=f"Format: {'Ciao, {}'.format(strInputString)}")
        labelFString.config(text=f"F-string: {f'Ciao, {strInputString}'}")
        labelEncode.config(text=f"Encode (UTF-8): {strInputString.encode('utf-8')}")
        labelDecode.config(text=f"Decode (UTF-8): {strInputString.encode('utf-8').decode('utf-8')}")
        labelCounter.config(text=f"Counter: {Counter(strInputString)}")
        labelUnicodedata.config(text=f"Unicodedata: {unicodedata.name(strInputString[0]) if strInputString else 'Stringa vuota'}")
        labelTextwrap.config(text=f"Textwrap: {textwrap.fill(strInputString, width=20)}")
        labelTemplate.config(text=f"Template: {Template('Ciao, $nome!').substitute(nome=strInputString)}")
        labelReduce.config(text=f"Reduce: {reduce(lambda x, y: x + ' ' + y, strInputString.split())}")
    else:
        labelUpperCase.config(text="In maiuscolo: ")
        labelLowerCase.config(text="In minuscolo: ")
        labelCapitalize.config(text="Capitalizzato: ")
        labelTitle.config(text="Titolo: ")
        labelSwapCase.config(text="Swapcase: ")
        labelStrip.config(text="Strip: ")
        labelReplace.config(text="Replace 'a' con 'X': ")
        labelSplit.config(text="Split: ")
        labelJoin.config(text="Join: ")
        labelCount.config(text="Count 'a': ")
        labelFind.config(text="Find 'mondo': ")
        labelStartswith.config(text="Startswith 'ciao': ")
        labelEndswith.config(text="Endswith 'mondo': ")
        labelIsalpha.config(text="Isalpha: ")
        labelIsdigit.config(text="Isdigit: ")
        labelIsalnum.config(text="Isalnum: ")
        labelIsspace.config(text="Isspace: ")
        labelIslower.config(text="Islower: ")
        labelIsupper.config(text="Isupper: ")
        labelIstitle.config(text="Istitle: ")
        labelZfill.config(text="Zfill (10): ")
        labelTranslate.config(text="Translate: ")
        labelReSub.config(text="Re.sub: ")
        labelFormat.config(text="Format: ")
        labelFString.config(text="F-string: ")
        labelEncode.config(text="Encode (UTF-8): ")
        labelDecode.config(text="Decode (UTF-8): ")
        labelCounter.config(text="Counter: ")
        labelUnicodedata.config(text="Unicodedata: ")
        labelTextwrap.config(text="Textwrap: ")
        labelTemplate.config(text="Template: ")
        labelReduce.config(text="Reduce: ")

# Creazione della finestra principale
root = tk.Tk()
root.title("String Manipulator")

# Frame scrollabile
main_frame = ttk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

canvas = tk.Canvas(main_frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

second_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=second_frame, anchor="nw")

# Variabile per il testo in input
inputString = tk.StringVar()
inputString.trace_add('write', update_labels)

# Creazione di una barra testuale per inserire il nome
inputString_entry = ttk.Entry(second_frame, textvariable=inputString, font=("Helvetica", 16))
inputString_entry.pack(padx=20, pady=10)

# Creazione delle etichette per i risultati
labelUpperCase = ttk.Label(second_frame, text="In maiuscolo: ", font=("Helvetica", 10))
labelUpperCase.pack(padx=20, pady=5, anchor="w")

labelLowerCase = ttk.Label(second_frame, text="In minuscolo: ", font=("Helvetica", 10))
labelLowerCase.pack(padx=20, pady=5, anchor="w")

labelCapitalize = ttk.Label(second_frame, text="Capitalizzato: ", font=("Helvetica", 10))
labelCapitalize.pack(padx=20, pady=5, anchor="w")

labelTitle = ttk.Label(second_frame, text="Titolo: ", font=("Helvetica", 10))
labelTitle.pack(padx=20, pady=5, anchor="w")

labelSwapCase = ttk.Label(second_frame, text="Swapcase: ", font=("Helvetica", 10))
labelSwapCase.pack(padx=20, pady=5, anchor="w")

labelStrip = ttk.Label(second_frame, text="Strip: ", font=("Helvetica", 10))
labelStrip.pack(padx=20, pady=5, anchor="w")

labelReplace = ttk.Label(second_frame, text="Replace 'a' con 'X': ", font=("Helvetica", 10))
labelReplace.pack(padx=20, pady=5, anchor="w")

labelSplit = ttk.Label(second_frame, text="Split: ", font=("Helvetica", 10))
labelSplit.pack(padx=20, pady=5, anchor="w")

labelJoin = ttk.Label(second_frame, text="Join: ", font=("Helvetica", 10))
labelJoin.pack(padx=20, pady=5, anchor="w")

labelCount = ttk.Label(second_frame, text="Count 'a': ", font=("Helvetica", 10))
labelCount.pack(padx=20, pady=5, anchor="w")

labelFind = ttk.Label(second_frame, text="Find 'mondo': ", font=("Helvetica", 10))
labelFind.pack(padx=20, pady=5, anchor="w")

labelStartswith = ttk.Label(second_frame, text="Startswith 'ciao': ", font=("Helvetica", 10))
labelStartswith.pack(padx=20, pady=5, anchor="w")

labelEndswith = ttk.Label(second_frame, text="Endswith 'mondo': ", font=("Helvetica", 10))
labelEndswith.pack(padx=20, pady=5, anchor="w")

labelIsalpha = ttk.Label(second_frame, text="Isalpha: ", font=("Helvetica", 10))
labelIsalpha.pack(padx=20, pady=5, anchor="w")

labelIsdigit = ttk.Label(second_frame, text="Isdigit: ", font=("Helvetica", 10))
labelIsdigit.pack(padx=20, pady=5, anchor="w")

labelIsalnum = ttk.Label(second_frame, text="Isalnum: ", font=("Helvetica", 10))
labelIsalnum.pack(padx=20, pady=5, anchor="w")

labelIsspace = ttk.Label(second_frame, text="Isspace: ", font=("Helvetica", 10))
labelIsspace.pack(padx=20, pady=5, anchor="w")

labelIslower = ttk.Label(second_frame, text="Islower: ", font=("Helvetica", 10))
labelIslower.pack(padx=20, pady=5, anchor="w")

labelIsupper = ttk.Label(second_frame, text="Isupper: ", font=("Helvetica", 10))
labelIsupper.pack(padx=20, pady=5, anchor="w")

labelIstitle = ttk.Label(second_frame, text="Istitle: ", font=("Helvetica", 10))
labelIstitle.pack(padx=20, pady=5, anchor="w")

labelZfill = ttk.Label(second_frame, text="Zfill (10): ", font=("Helvetica", 10))
labelZfill.pack(padx=20, pady=5, anchor="w")

labelTranslate = ttk.Label(second_frame, text="Translate: ", font=("Helvetica", 10))
labelTranslate.pack(padx=20, pady=5, anchor="w")

labelReSub = ttk.Label(second_frame, text="Re.sub: ", font=("Helvetica", 10))
labelReSub.pack(padx=20, pady=5, anchor="w")

labelFormat = ttk.Label(second_frame, text="Format: ", font=("Helvetica", 10))
labelFormat.pack(padx=20, pady=5, anchor="w")

labelFString = ttk.Label(second_frame, text="F-string: ", font=("Helvetica", 10))
labelFString.pack(padx=20, pady=5, anchor="w")

labelEncode = ttk.Label(second_frame, text="Encode (UTF-8): ", font=("Helvetica", 10))
labelEncode.pack(padx=20, pady=5, anchor="w")

labelDecode = ttk.Label(second_frame, text="Decode (UTF-8): ", font=("Helvetica", 10))
labelDecode.pack(padx=20, pady=5, anchor="w")

labelCounter = ttk.Label(second_frame, text="Counter: ", font=("Helvetica", 10))
labelCounter.pack(padx=20, pady=5, anchor="w")

labelUnicodedata = ttk.Label(second_frame, text="Unicodedata: ", font=("Helvetica", 10))
labelUnicodedata.pack(padx=20, pady=5, anchor="w")

labelTextwrap = ttk.Label(second_frame, text="Textwrap: ", font=("Helvetica", 10))
labelTextwrap.pack(padx=20, pady=5, anchor="w")

labelTemplate = ttk.Label(second_frame, text="Template: ", font=("Helvetica", 10))
labelTemplate.pack(padx=20, pady=5, anchor="w")

labelReduce = ttk.Label(second_frame, text="Reduce: ", font=("Helvetica", 10))
labelReduce.pack(padx=20, pady=5, anchor="w")

# Creazione del pulsante "Chiudi"
close_button = ttk.Button(second_frame, text="Chiudi", command=close_window)
close_button.pack(pady=10)

# Posizionamento della finestra al centro del desktop
center_window(root)

# Avvio del loop principale della finestra
root.mainloop()