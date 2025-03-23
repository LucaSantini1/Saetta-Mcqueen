# Definisci una classe base chiamata MaterialeBiblioteca con attributi di istanza titolo, anno_pubblicazione e disponibile.
# Implementa metodi di istanza nella classe MaterialeBiblioteca per accedere e modificare questi attributi.
# Aggiungi un metodo prestito che imposta l'attributo disponibile a False e un metodo restituzione che lo imposta a True.
# Definisci una classe derivata chiamata Libro che eredita dalla classe MaterialeBiblioteca.
# Aggiungi attributi di istanza specifici per Libro, come autore e numero_pagine.
# Definisci una classe derivata chiamata Rivista che eredita dalla classe MaterialeBiblioteca.
# Aggiungi attributi di istanza specifici per Rivista, come numero_edizione e mese_pubblicazione.
# Definisci una classe derivata chiamata DVD che eredita dalla classe MaterialeBiblioteca.
# Aggiungi attributi di istanza specifici per DVD, come regista e durata.
# Implementa metodi di istanza nelle classi Libro, Rivista e DVD per accedere e modificare i loro attributi specifici.
# Aggiungi un metodo di ricerca nella classe MaterialeBiblioteca che permette di cercare materiali per titolo.

class MaterialeBiblioteca:
	def __init__(self, titolo : str, anno_pubblicazione : int):
		self.titolo = titolo
		self.anno_pubblicazione = anno_pubblicazione
		self.disponibile = True

	def get_titolo(self):
		return self.titolo

	def get_anno_pubblicazione(self):
		return self.anno_pubblicazione

	def is_disponibile(self):
		return self.disponibile

	def set_titolo(self, titolo : str):
		self.titolo = titolo

	def set_anno_pubblicazione(self, anno_pubblicazione : int):
		self.anno_pubblicazione = anno_pubblicazione

	def prestito(self):
		self.disponibile = False

	def restituzione(self):
		self.disponibile = True

	@classmethod
	def ricerca(cls, materiali : list, titolo : str):
		for m in materiali:
			if titolo in m.get_titolo():
				return m
		return MaterialeBiblioteca("Nessun risultato trovato!", -1)
class Libro(MaterialeBiblioteca):
	def __init__(self, titolo : str, anno_pubblicazione : int, autore : str, numero_pagine : int):
		super().__init__(titolo, anno_pubblicazione)
		self.autore = autore
		self.numero_pagine = numero_pagine

	def get_autore(self):
		return self.autore

	def get_numero_pagine(self):
		return self.numero_pagine

	def set_autore(self, autore : str):
		self.autore = autore

	def set_numero_pagine(self, numero_pagine : int):
		self.numero_pagine = numero_pagine

class Rivista(MaterialeBiblioteca):
	def __init__(self, titolo : str, anno_pubblicazione : int, numero_edizione : int, mese_pubblicazione : str):
		super().__init__(titolo, anno_pubblicazione)
		self.numero_edizione = numero_edizione
		self.mese_pubblicazione = mese_pubblicazione

	def get_numero_edizione(self):
		return self.numero_edizione

	def get_mese_edizione(self):
		return self.mese_pubblicazione

	def set_numero_edizione(self, numero_edizione : int):
		self.numero_edizione = numero_edizione

	def set_mese_pubblicazione(self, mese_pubblicazione : str):
		self.mese_pubblicazione = mese_pubblicazione

class DVD(MaterialeBiblioteca):
	def __init__(self, titolo : str, anno_pubblicazione : int, regista : str, durata : int):
		super().__init__(titolo, anno_pubblicazione)
		self.regista = regista
		self.durata = durata

	def get_regista(self):
		return self.regista

	def get_durata(self):
		return self.durata

	def set_regista(self, regista : str):
		self.regista = regista

	def set_durata(self, durata : int):
		self.durata = durata


# Esempio di utilizzo
libro = Libro("Il Signore degli Anelli", 1954, "J.R.R. Tolkien", 1178)
print(libro.get_titolo())  # Output: Il Signore degli Anelli
print(libro.get_autore())  # Output: J.R.R. Tolkien
libro.prestito()
print(libro.is_disponibile())  # Output: False
libro.restituzione()
print(libro.is_disponibile())  # Output: True

rivista = Rivista("National Geographic", 2023, 5, "Maggio")
print(rivista.get_titolo())  # Output: National Geographic
print(rivista.get_numero_edizione())  # Output: 5

dvd = DVD("Inception", 2010, "Christopher Nolan", 148)
print(dvd.get_titolo())  # Output: Inception
print(dvd.get_regista())  # Output: Christopher Nolan

materiali = [libro, rivista, dvd]
risultato = MaterialeBiblioteca.ricerca(materiali, titolo="Inception")
print(risultato.get_titolo())  # Output: Inception