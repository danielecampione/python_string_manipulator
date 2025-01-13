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
        entryUpperCase.delete(0, tk.END)
        entryUpperCase.insert(0, strInputString.upper())
        entryLowerCase.delete(0, tk.END)
        entryLowerCase.insert(0, strInputString.lower())
        entryCapitalize.delete(0, tk.END)
        entryCapitalize.insert(0, strInputString.capitalize())
        entryTitle.delete(0, tk.END)
        entryTitle.insert(0, strInputString.title())
        entrySwapCase.delete(0, tk.END)
        entrySwapCase.insert(0, strInputString.swapcase())
        entryStrip.delete(0, tk.END)
        entryStrip.insert(0, strInputString.strip())
        entryReplace.delete(0, tk.END)
        entryReplace.insert(0, strInputString.replace('a', 'X'))
        entrySplit.delete(0, tk.END)
        entrySplit.insert(0, str(strInputString.split()))
        entryJoin.delete(0, tk.END)
        entryJoin.insert(0, '-'.join(strInputString.split()))
        entryCount.delete(0, tk.END)
        entryCount.insert(0, str(strInputString.count('a')))
        entryFind.delete(0, tk.END)
        entryFind.insert(0, str(strInputString.find('mondo')))
        entryStartswith.delete(0, tk.END)
        entryStartswith.insert(0, str(strInputString.startswith('ciao')))
        entryEndswith.delete(0, tk.END)
        entryEndswith.insert(0, str(strInputString.endswith('mondo')))
        entryIsalpha.delete(0, tk.END)
        entryIsalpha.insert(0, str(strInputString.isalpha()))
        entryIsdigit.delete(0, tk.END)
        entryIsdigit.insert(0, str(strInputString.isdigit()))
        entryIsalnum.delete(0, tk.END)
        entryIsalnum.insert(0, str(strInputString.isalnum()))
        entryIsspace.delete(0, tk.END)
        entryIsspace.insert(0, str(strInputString.isspace()))
        entryIslower.delete(0, tk.END)
        entryIslower.insert(0, str(strInputString.islower()))
        entryIsupper.delete(0, tk.END)
        entryIsupper.insert(0, str(strInputString.isupper()))
        entryIstitle.delete(0, tk.END)
        entryIstitle.insert(0, str(strInputString.istitle()))
        entryZfill.delete(0, tk.END)
        entryZfill.insert(0, strInputString.zfill(10))
        tabella = str.maketrans("ao", "ou")
        entryTranslate.delete(0, tk.END)
        entryTranslate.insert(0, strInputString.translate(tabella))
        entryReSub.delete(0, tk.END)
        entryReSub.insert(0, re.sub(r'\d+', 'NUMERO', strInputString))
        entryFormat.delete(0, tk.END)
        entryFormat.insert(0, 'Ciao, {}'.format(strInputString))
        entryFString.delete(0, tk.END)
        entryFString.insert(0, f'Ciao, {strInputString}')
        entryEncode.delete(0, tk.END)
        entryEncode.insert(0, strInputString.encode('utf-8'))
        entryDecode.delete(0, tk.END)
        entryDecode.insert(0, strInputString.encode('utf-8').decode('utf-8'))
        entryCounter.delete(0, tk.END)
        entryCounter.insert(0, str(Counter(strInputString)))
        entryUnicodedata.delete(0, tk.END)
        entryUnicodedata.insert(0, unicodedata.name(strInputString[0]) if strInputString else 'Stringa vuota')
        textTextwrap.delete("1.0", tk.END)
        textTextwrap.insert(tk.END, textwrap.fill(strInputString, width=20))
        entryTemplate.delete(0, tk.END)
        entryTemplate.insert(0, Template('Ciao, $nome!').substitute(nome=strInputString))
        entryReduce.delete(0, tk.END)
        entryReduce.insert(0, reduce(lambda x, y: x + ' ' + y, strInputString.split()))
    else:
        for entry in all_entries:
            entry.delete(0, tk.END)
        textTextwrap.delete("1.0", tk.END)

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

# Creazione delle etichette e delle caselle di testo per i risultati
all_entries = []

def create_label_and_entry(frame, label_text):
    label = ttk.Label(frame, text=label_text, font=("Helvetica", 10))
    label.pack(padx=20, pady=5, anchor="w")
    entry = ttk.Entry(frame, font=("Helvetica", 10), width=50)
    entry.pack(padx=20, pady=5, anchor="w")
    all_entries.append(entry)
    return entry

entryUpperCase = create_label_and_entry(second_frame, "In maiuscolo:")
entryLowerCase = create_label_and_entry(second_frame, "In minuscolo:")
entryCapitalize = create_label_and_entry(second_frame, "Capitalizzato:")
entryTitle = create_label_and_entry(second_frame, "Titolo:")
entrySwapCase = create_label_and_entry(second_frame, "Swapcase:")
entryStrip = create_label_and_entry(second_frame, "Strip:")
entryReplace = create_label_and_entry(second_frame, "Replace 'a' con 'X':")
entrySplit = create_label_and_entry(second_frame, "Split:")
entryJoin = create_label_and_entry(second_frame, "Join:")
entryCount = create_label_and_entry(second_frame, "Count 'a':")
entryFind = create_label_and_entry(second_frame, "Find 'mondo':")
entryStartswith = create_label_and_entry(second_frame, "Startswith 'ciao':")
entryEndswith = create_label_and_entry(second_frame, "Endswith 'mondo':")
entryIsalpha = create_label_and_entry(second_frame, "Isalpha:")
entryIsdigit = create_label_and_entry(second_frame, "Isdigit:")
entryIsalnum = create_label_and_entry(second_frame, "Isalnum:")
entryIsspace = create_label_and_entry(second_frame, "Isspace:")
entryIslower = create_label_and_entry(second_frame, "Islower:")
entryIsupper = create_label_and_entry(second_frame, "Isupper:")
entryIstitle = create_label_and_entry(second_frame, "Istitle:")
entryZfill = create_label_and_entry(second_frame, "Zfill (10):")
entryTranslate = create_label_and_entry(second_frame, "Translate:")
entryReSub = create_label_and_entry(second_frame, "Re.sub:")
entryFormat = create_label_and_entry(second_frame, "Format:")
entryFString = create_label_and_entry(second_frame, "F-string:")
entryEncode = create_label_and_entry(second_frame, "Encode (UTF-8):")
entryDecode = create_label_and_entry(second_frame, "Decode (UTF-8):")
entryCounter = create_label_and_entry(second_frame, "Counter:")
entryUnicodedata = create_label_and_entry(second_frame, "Unicodedata:")

# Creazione di una ScrolledText per Textwrap
labelTextwrap = ttk.Label(second_frame, text="Textwrap:", font=("Helvetica", 10))
labelTextwrap.pack(padx=20, pady=5, anchor="w")
textTextwrap = scrolledtext.ScrolledText(second_frame, font=("Helvetica", 10), width=50, height=4)
textTextwrap.pack(padx=20, pady=5, anchor="w")

entryTemplate = create_label_and_entry(second_frame, "Template:")
entryReduce = create_label_and_entry(second_frame, "Reduce:")

# Creazione del pulsante "Chiudi"
close_button = ttk.Button(second_frame, text="Chiudi", command=close_window)
close_button.pack(pady=10)

# Posizionamento della finestra al centro del desktop
center_window(root)

# Avvio del loop principale della finestra
root.mainloop()