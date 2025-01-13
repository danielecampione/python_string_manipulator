import tkinter as tk
from tkinter import ttk, scrolledtext
from collections import Counter
import unicodedata
import re
from functools import reduce
from string import Template
import textwrap
import logging

# Configurazione del logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Classe per la manipolazione delle stringhe
class StringManipulator:
    """Classe per la manipolazione delle stringhe."""
    @staticmethod
    def upper(text):
        """Converte il testo in maiuscolo."""
        return text.upper()

    @staticmethod
    def lower(text):
        """Converte il testo in minuscolo."""
        return text.lower()

    @staticmethod
    def capitalize(text):
        """Capitalizza la prima lettera del testo."""
        return text.capitalize()

    @staticmethod
    def title(text):
        """Converte il testo in titolo (ogni parola con la prima lettera maiuscola)."""
        return text.title()

    @staticmethod
    def swapcase(text):
        """Inverte maiuscole e minuscole nel testo."""
        return text.swapcase()

    @staticmethod
    def strip(text):
        """Rimuove spazi bianchi all'inizio e alla fine del testo."""
        return text.strip()

    @staticmethod
    def replace(text, old='a', new='X'):
        """Sostituisce tutte le occorrenze di `old` con `new` nel testo."""
        return text.replace(old, new)

    @staticmethod
    def split(text):
        """Divide il testo in una lista di parole."""
        return str(text.split())

    @staticmethod
    def join(text, separator='-'):
        """Unisce le parole del testo utilizzando il separatore specificato."""
        return separator.join(text.split())

    @staticmethod
    def count(text, substring='a'):
        """Conta le occorrenze di `substring` nel testo."""
        return str(text.count(substring))

    @staticmethod
    def find(text, substring='mondo'):
        """Trova la posizione della prima occorrenza di `substring` nel testo."""
        return str(text.find(substring))

    @staticmethod
    def startswith(text, prefix='ciao'):
        """Verifica se il testo inizia con `prefix`."""
        return str(text.startswith(prefix))

    @staticmethod
    def endswith(text, suffix='mondo'):
        """Verifica se il testo termina con `suffix`."""
        return str(text.endswith(suffix))

    @staticmethod
    def isalpha(text):
        """Verifica se tutti i caratteri del testo sono alfabetici."""
        return str(text.isalpha())

    @staticmethod
    def isdigit(text):
        """Verifica se tutti i caratteri del testo sono numerici."""
        return str(text.isdigit())

    @staticmethod
    def isalnum(text):
        """Verifica se tutti i caratteri del testo sono alfanumerici."""
        return str(text.isalnum())

    @staticmethod
    def isspace(text):
        """Verifica se tutti i caratteri del testo sono spazi bianchi."""
        return str(text.isspace())

    @staticmethod
    def islower(text):
        """Verifica se tutti i caratteri del testo sono minuscoli."""
        return str(text.islower())

    @staticmethod
    def isupper(text):
        """Verifica se tutti i caratteri del testo sono maiuscoli."""
        return str(text.isupper())

    @staticmethod
    def istitle(text):
        """Verifica se il testo è in formato titolo."""
        return str(text.istitle())

    @staticmethod
    def zfill(text, width=10):
        """Riempie il testo con zeri a sinistra fino a raggiungere la larghezza specificata."""
        return text.zfill(width)

    @staticmethod
    def translate(text, table=None):
        """Traduce il testo utilizzando una tabella di traduzione."""
        if table is None:
            table = str.maketrans("ao", "ou")
        return text.translate(table)

    @staticmethod
    def re_sub(text, pattern=r'\d+', repl='NUMERO'):
        """Sostituisce tutte le occorrenze di `pattern` con `repl` nel testo."""
        return re.sub(pattern, repl, text)

    @staticmethod
    def format(text, template='Ciao, {}'):
        """Formatta il testo utilizzando il template specificato."""
        return template.format(text)

    @staticmethod
    def f_string(text, template='Ciao, {}'):
        """Formatta il testo utilizzando una f-string."""
        return f'Ciao, {text}'

    @staticmethod
    def encode(text, encoding='utf-8'):
        """Codifica il testo in bytes utilizzando l'encoding specificato."""
        return text.encode(encoding)

    @staticmethod
    def decode(text, encoding='utf-8'):
        """Decodifica il testo da bytes a stringa utilizzando l'encoding specificato."""
        return text.encode(encoding).decode(encoding)

    @staticmethod
    def counter(text):
        """Conta le occorrenze di ciascun carattere nel testo."""
        return str(Counter(text))

    @staticmethod
    def unicodedata(text):
        """Restituisce il nome Unicode del primo carattere del testo."""
        return unicodedata.name(text[0]) if text else 'Stringa vuota'

    @staticmethod
    def textwrap(text, width=20):
        """Avvolge il testo in più righe con la larghezza specificata."""
        return textwrap.fill(text, width=width)

    @staticmethod
    def template(text, template_str='Ciao, $nome!'):
        """Formatta il testo utilizzando un template con segnaposto."""
        return Template(template_str).substitute(nome=text)

    @staticmethod
    def reduce(text):
        """Riduce il testo unendo le parole con uno spazio."""
        return reduce(lambda x, y: x + ' ' + y, text.split())


# Classe per l'interfaccia grafica
class StringManipulatorApp:
    """Classe per l'interfaccia grafica dell'applicazione."""
    def __init__(self, root, string_manipulator):
        self.logger = logging.getLogger(__name__)
        self.root = root
        self.string_manipulator = string_manipulator
        self.input_string = tk.StringVar()
        self.input_string.trace_add('write', self.update_labels)
        self.create_interface()
        self.logger.info("Applicazione avviata.")

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
        self.create_label_and_entry("In maiuscolo:", self.string_manipulator.upper)
        self.create_label_and_entry("In minuscolo:", self.string_manipulator.lower)
        self.create_label_and_entry("Capitalizzato:", self.string_manipulator.capitalize)
        self.create_label_and_entry("Titolo:", self.string_manipulator.title)
        self.create_label_and_entry("Swapcase:", self.string_manipulator.swapcase)
        self.create_label_and_entry("Strip:", self.string_manipulator.strip)
        self.create_label_and_entry("Replace 'a' con 'X':", lambda x: self.string_manipulator.replace(x, 'a', 'X'))
        self.create_label_and_entry("Split:", self.string_manipulator.split)
        self.create_label_and_entry("Join:", self.string_manipulator.join)
        self.create_label_and_entry("Count 'a':", lambda x: self.string_manipulator.count(x, 'a'))
        self.create_label_and_entry("Find 'mondo':", lambda x: self.string_manipulator.find(x, 'mondo'))
        self.create_label_and_entry("Startswith 'ciao':", lambda x: self.string_manipulator.startswith(x, 'ciao'))
        self.create_label_and_entry("Endswith 'mondo':", lambda x: self.string_manipulator.endswith(x, 'mondo'))
        self.create_label_and_entry("Isalpha:", self.string_manipulator.isalpha)
        self.create_label_and_entry("Isdigit:", self.string_manipulator.isdigit)
        self.create_label_and_entry("Isalnum:", self.string_manipulator.isalnum)
        self.create_label_and_entry("Isspace:", self.string_manipulator.isspace)
        self.create_label_and_entry("Islower:", self.string_manipulator.islower)
        self.create_label_and_entry("Isupper:", self.string_manipulator.isupper)
        self.create_label_and_entry("Istitle:", self.string_manipulator.istitle)
        self.create_label_and_entry("Zfill (10):", lambda x: self.string_manipulator.zfill(x, 10))
        self.create_label_and_entry("Translate:", self.string_manipulator.translate)
        self.create_label_and_entry("Re.sub:", self.string_manipulator.re_sub)
        self.create_label_and_entry("Format:", self.string_manipulator.format)
        self.create_label_and_entry("F-string:", self.string_manipulator.f_string)
        self.create_label_and_entry("Encode (UTF-8):", self.string_manipulator.encode)
        self.create_label_and_entry("Decode (UTF-8):", self.string_manipulator.decode)
        self.create_label_and_entry("Counter:", self.string_manipulator.counter)
        self.create_label_and_entry("Unicodedata:", self.string_manipulator.unicodedata)

        # Textwrap (ScrolledText)
        self.create_scrolled_text("Textwrap:", self.string_manipulator.textwrap)

        self.create_label_and_entry("Template:", self.string_manipulator.template)
        self.create_label_and_entry("Reduce:", self.string_manipulator.reduce)

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
        self.logger.info("Risultati aggiornati")


# Avvio dell'applicazione
if __name__ == "__main__":
    root = tk.Tk()
    string_manipulator = StringManipulator()
    app = StringManipulatorApp(root, string_manipulator)
    root.mainloop()