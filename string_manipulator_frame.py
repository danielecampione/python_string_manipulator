import tkinter as tk
from tkinter import ttk, scrolledtext
from collections import Counter
import unicodedata
import re
from functools import reduce
from string import Template
import textwrap


# Classe per la gestione della manipolazione delle stringhe
class StringManipulator:
    @staticmethod
    def upper(text):
        return text.upper()

    @staticmethod
    def lower(text):
        return text.lower()

    @staticmethod
    def capitalize(text):
        return text.capitalize()

    @staticmethod
    def title(text):
        return text.title()

    @staticmethod
    def swapcase(text):
        return text.swapcase()

    @staticmethod
    def strip(text):
        return text.strip()

    @staticmethod
    def replace(text, old='a', new='X'):
        return text.replace(old, new)

    @staticmethod
    def split(text):
        return str(text.split())

    @staticmethod
    def join(text, separator='-'):
        return separator.join(text.split())

    @staticmethod
    def count(text, substring='a'):
        return str(text.count(substring))

    @staticmethod
    def find(text, substring='mondo'):
        return str(text.find(substring))

    @staticmethod
    def startswith(text, prefix='ciao'):
        return str(text.startswith(prefix))

    @staticmethod
    def endswith(text, suffix='mondo'):
        return str(text.endswith(suffix))

    @staticmethod
    def isalpha(text):
        return str(text.isalpha())

    @staticmethod
    def isdigit(text):
        return str(text.isdigit())

    @staticmethod
    def isalnum(text):
        return str(text.isalnum())

    @staticmethod
    def isspace(text):
        return str(text.isspace())

    @staticmethod
    def islower(text):
        return str(text.islower())

    @staticmethod
    def isupper(text):
        return str(text.isupper())

    @staticmethod
    def istitle(text):
        return str(text.istitle())

    @staticmethod
    def zfill(text, width=10):
        return text.zfill(width)

    @staticmethod
    def translate(text, table=None):
        if table is None:
            table = str.maketrans("ao", "ou")
        return text.translate(table)

    @staticmethod
    def re_sub(text, pattern=r'\d+', repl='NUMERO'):
        return re.sub(pattern, repl, text)

    @staticmethod
    def format(text, template='Ciao, {}'):
        return template.format(text)

    @staticmethod
    def f_string(text, template='Ciao, {}'):
        return f'Ciao, {text}'

    @staticmethod
    def encode(text, encoding='utf-8'):
        return text.encode(encoding)

    @staticmethod
    def decode(text, encoding='utf-8'):
        return text.encode(encoding).decode(encoding)

    @staticmethod
    def counter(text):
        return str(Counter(text))

    @staticmethod
    def unicodedata(text):
        return unicodedata.name(text[0]) if text else 'Stringa vuota'

    @staticmethod
    def textwrap(text, width=20):
        return textwrap.fill(text, width=width)

    @staticmethod
    def template(text, template_str='Ciao, $nome!'):
        return Template(template_str).substitute(nome=text)

    @staticmethod
    def reduce(text):
        return reduce(lambda x, y: x + ' ' + y, text.split())


# Classe per l'interfaccia grafica
class StringManipulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("String Manipulator")
        self.root.geometry("800x600")

        # Variabile per il testo in input
        self.input_string = tk.StringVar()
        self.input_string.trace_add('write', self.update_labels)

        # Creazione dell'interfaccia
        self.create_interface()

    def create_interface(self):
        """Crea l'interfaccia grafica."""
        # Frame scrollabile
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.main_frame)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.second_frame = ttk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.second_frame, anchor="nw")

        # Input
        self.input_entry = ttk.Entry(self.second_frame, textvariable=self.input_string, font=("Helvetica", 16))
        self.input_entry.pack(padx=20, pady=10)

        # Creazione delle caselle di testo per i risultati
        self.all_entries = []
        self.create_label_and_entry("In maiuscolo:", StringManipulator.upper)
        self.create_label_and_entry("In minuscolo:", StringManipulator.lower)
        self.create_label_and_entry("Capitalizzato:", StringManipulator.capitalize)
        self.create_label_and_entry("Titolo:", StringManipulator.title)
        self.create_label_and_entry("Swapcase:", StringManipulator.swapcase)
        self.create_label_and_entry("Strip:", StringManipulator.strip)
        self.create_label_and_entry("Replace 'a' con 'X':", lambda x: StringManipulator.replace(x, 'a', 'X'))
        self.create_label_and_entry("Split:", StringManipulator.split)
        self.create_label_and_entry("Join:", StringManipulator.join)
        self.create_label_and_entry("Count 'a':", lambda x: StringManipulator.count(x, 'a'))
        self.create_label_and_entry("Find 'mondo':", lambda x: StringManipulator.find(x, 'mondo'))
        self.create_label_and_entry("Startswith 'ciao':", lambda x: StringManipulator.startswith(x, 'ciao'))
        self.create_label_and_entry("Endswith 'mondo':", lambda x: StringManipulator.endswith(x, 'mondo'))
        self.create_label_and_entry("Isalpha:", StringManipulator.isalpha)
        self.create_label_and_entry("Isdigit:", StringManipulator.isdigit)
        self.create_label_and_entry("Isalnum:", StringManipulator.isalnum)
        self.create_label_and_entry("Isspace:", StringManipulator.isspace)
        self.create_label_and_entry("Islower:", StringManipulator.islower)
        self.create_label_and_entry("Isupper:", StringManipulator.isupper)
        self.create_label_and_entry("Istitle:", StringManipulator.istitle)
        self.create_label_and_entry("Zfill (10):", lambda x: StringManipulator.zfill(x, 10))
        self.create_label_and_entry("Translate:", StringManipulator.translate)
        self.create_label_and_entry("Re.sub:", StringManipulator.re_sub)
        self.create_label_and_entry("Format:", StringManipulator.format)
        self.create_label_and_entry("F-string:", StringManipulator.f_string)
        self.create_label_and_entry("Encode (UTF-8):", StringManipulator.encode)
        self.create_label_and_entry("Decode (UTF-8):", StringManipulator.decode)
        self.create_label_and_entry("Counter:", StringManipulator.counter)
        self.create_label_and_entry("Unicodedata:", StringManipulator.unicodedata)

        # Textwrap (ScrolledText)
        self.create_scrolled_text("Textwrap:", StringManipulator.textwrap)

        self.create_label_and_entry("Template:", StringManipulator.template)
        self.create_label_and_entry("Reduce:", StringManipulator.reduce)

        # Pulsante Chiudi
        close_button = ttk.Button(self.second_frame, text="Chiudi", command=self.root.destroy)
        close_button.pack(pady=10)

    def create_label_and_entry(self, label_text, operation):
        """Crea un'etichetta e una casella di testo per un'operazione."""
        label = ttk.Label(self.second_frame, text=label_text, font=("Helvetica", 10))
        label.pack(padx=20, pady=5, anchor="w")
        entry = ttk.Entry(self.second_frame, font=("Helvetica", 10), width=50)
        entry.pack(padx=20, pady=5, anchor="w")
        self.all_entries.append((entry, operation))

    def create_scrolled_text(self, label_text, operation):
        """Crea una ScrolledText per operazioni multi-linea."""
        label = ttk.Label(self.second_frame, text=label_text, font=("Helvetica", 10))
        label.pack(padx=20, pady=5, anchor="w")
        text = scrolledtext.ScrolledText(self.second_frame, font=("Helvetica", 10), width=50, height=4)
        text.pack(padx=20, pady=5, anchor="w")
        self.all_entries.append((text, operation))

    def update_labels(self, *args):
        """Aggiorna tutte le caselle di testo in base all'input."""
        input_text = self.input_string.get()
        for widget, operation in self.all_entries:
            if isinstance(widget, ttk.Entry):
                widget.delete(0, tk.END)
                widget.insert(0, operation(input_text))
            elif isinstance(widget, scrolledtext.ScrolledText):
                widget.delete("1.0", tk.END)
                widget.insert(tk.END, operation(input_text))


# Avvio dell'applicazione
if __name__ == "__main__":
    root = tk.Tk()
    app = StringManipulatorApp(root)
    root.mainloop()