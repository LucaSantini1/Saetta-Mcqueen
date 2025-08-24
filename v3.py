from datetime import date
from typing import List

class Libro:
	def __init__(self, titolo : str, data_pubblicazione : date, autore : "Autore"):
		self._titolo = titolo
		self._data_pubblicazione = data_pubblicazione
		self._autore = autore
		autore.scrivi_libro(self)
		self._utente = None
		self._data_prestito = None

	def isDisponibile(self):
		return self._data_prestito is None
	
	def assegna_utente(self, utente : "Utente", data : date):
		self._utente = utente
		self._data_prestito = data

	def restituisci(self, data : date):
		self._data_prestito = None
		self._utente = None

	def get_titolo(self):
		return self._titolo

	def __str__(self):
		return f'{self._titolo} ({self._autore})'

class Utente:
	def __init__(self, nome : str, cognome : str):
		self._nome = nome
		self._cognome = cognome
		self._libri = []

	def prendi_libro(self, libro : Libro):
		if libro not in self._libri:
			self._libri.append(libro)
			return True
		return False
	
	def __str__(self):
		return f'{self._nome} {self._cognome}'

class Autore:
	def __init__(self, nome : str, cognome : str):
		self._nome = nome
		self._cognome = cognome
		self._libri = []

	def autore_di(self, libro : Libro) -> bool:
		return libro in self._libri
	
	def scrivi_libro(self, libro : Libro) -> bool:
		if libro not in self._libri:
			self._libri.append(libro)
			return True
		return False
	
	def __str__(self):
		return f'{self._nome} {self._cognome}'

class Biblioteca:
	def __init__(self):
		self._libri = []
		self._utenti = []
		self._autori = []

	def aggiungi_libro(self, libro : Libro) -> bool:
		if libro not in self._libri:
			self._libri.append(libro)
			return True
		return False

	def aggiungi_utente(self, utente : Utente) -> bool:
		if utente not in self._utenti:
			self._utenti.append(utente)
			return True
		return False

	def presta_libro(self, libro : Libro, utente : Utente, data : date) -> bool:
		if libro.isDisponibile():
			libro.assegna_utente(utente, data)
			utente.prendi_libro(libro)

	def restituisci_libro(self, libro : Libro, data : date):
		libro.restituisci(data)

	def libri_disponibili(self) -> List[Libro]:
		ris = []
		for libro in self._libri:
			if libro.isDisponibile():
				ris.append(libro)
		return ris
	
	def cerca_libri_per_autore(self, autore : Autore):
		ris = []
		for libro in self._libri:
			if autore.autore_di(libro):
				ris.append(libro)
		return ris
	
	def cerca_libro_per_titolo(self, titolo : str):
		ris = []
		for libro in self._libri:
			if titolo.lower() in libro.get_titolo().lower():
				ris.append(libro)
		return ris
	
	def ottieni_libri(self):
		return self._libri
	
	def ottieni_utenti(self):
		return self._utenti

def main():
	# Creazione biblioteca
	biblioteca = Biblioteca()

	# Creazione autori
	autore1 = Autore("Alessandro", "Manzoni")
	autore2 = Autore("Italo", "Calvino")

	# Creazione libri
	libro1 = Libro("I Promessi Sposi", date(1827, 1, 1), autore1)
	libro2 = Libro("Il barone rampante", date(1957, 1, 1), autore2)
	biblioteca.aggiungi_libro(libro1)
	biblioteca.aggiungi_libro(libro2)

	# Creazione utenti
	utente1 = Utente("Mario", "Rossi")
	utente2 = Utente("Laura", "Bianchi")
	biblioteca.aggiungi_utente(utente1)
	biblioteca.aggiungi_utente(utente2)

	# Test operazioni
	print("Libri disponibili:", [str(l) for l in biblioteca.libri_disponibili()])

	# Prestito libro
	biblioteca.presta_libro(libro1, utente1, date.today())
	print(f"\nLibro '{libro1}' prestato a {utente1}")

	# Verifica disponibilità
	print("\nLibri disponibili dopo il prestito:",
		[str(l) for l in biblioteca.libri_disponibili()])

	# Ricerca per autore
	print(f"\nLibri di {autore1}:",
		[str(l) for l in biblioteca.cerca_libri_per_autore(autore1)])

	# Restituzione libro
	biblioteca.restituisci_libro(libro1, date.today())
	print(f"\nLibro '{libro1}' restituito")

	print("\nLibri disponibili dopo la restituzione:",
		[str(l) for l in biblioteca.libri_disponibili()])

	# Ricerca libro per titolo
	libri_trovati = biblioteca.cerca_libro_per_titolo("Promessi")
	print(f"\nLibri trovati con titolo contenente 'Promessi':", [str(l) for l in libri_trovati])

	# Ottieni tutti i libri
	print("\nTutti i libri in biblioteca:", [str(l) for l in biblioteca.ottieni_libri()])

	# Ottieni tutti gli utenti
	print("\nTutti gli utenti in biblioteca:", [str(u) for u in biblioteca.ottieni_utenti()])

if __name__ == "__main__":
	main()

# Libri disponibili: ['I Promessi Sposi (Alessandro Manzoni)', 'Il barone rampante (Italo Calvino)']
# Libro 'I Promessi Sposi (Alessandro Manzoni)' prestato a Mario Rossi
# Libri disponibili dopo il prestito: ['Il barone rampante (Italo Calvino)']
# Libri di Alessandro Manzoni: ['I Promessi Sposi (Alessandro Manzoni)']
# Libro 'I Promessi Sposi (Alessandro Manzoni)' restituito
# Libri disponibili dopo la restituzione: ['I Promessi Sposi (Alessandro Manzoni)', 'Il barone rampante (Italo Calvino)']
# Libri trovati con titolo contenente 'Promessi': ['I Promessi Sposi (Alessandro Manzoni)']
# Tutti i libri in biblioteca: ['I Promessi Sposi (Alessandro Manzoni)', 'Il barone rampante (Italo Calvino)']
# Tutti gli utenti in biblioteca: ['Mario Rossi', 'Laura Bianchi']