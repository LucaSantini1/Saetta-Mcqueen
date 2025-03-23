# Definisci la classe Libro con attributi privati _titolo, _autore e _pagine.
# Implementa i metodi getter e setter per ciascuno di questi attributi.
# Assicurati che il titolo e l'autore non possano essere stringhe vuote.
# Assicurati che il numero di pagine sia un numero positivo.

class Libro:
	def __init__(self, titolo : str, autore : str, numero_pagine : int):
		self._titolo = titolo
		self._autore = autore
		self._numero_pagine = numero_pagine

	@property
	def titolo(self):
		return self._titolo

	@property
	def autore(self):
		return self._autore

	@property
	def numero_pagine(self):
		return self._numero_pagine

	@titolo.setter
	def titolo(self, titolo):
		self._titolo = titolo

	@autore.setter
	def autore(self, autore):
		self._autore = autore

	@numero_pagine.setter
	def numero_pagine(self, numero_pagine):
		self._numero_pagine = numero_pagine


# Esempio di utilizzo
libro = Libro("Il Signore degli Anelli", "J.R.R. Tolkien", 1200)
print(libro.titolo)  # Chiama automaticamente il getter
libro.titolo = "Lo Hobbit"  # Chiama automaticamente il setter
print(libro.titolo)
