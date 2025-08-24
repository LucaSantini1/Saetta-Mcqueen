from datetime import datetime
from typing import List

class ElementoMenu:
	def __init__(self, codice: str, nome: str, prezzo: float, tempo_preparazione: int, allergeni: List[str], disponibile : bool):
		self._codice = codice
		self._nome = nome
		self._prezzo = prezzo
		self._tempo_preparazione = tempo_preparazione
		self._allergeni = allergeni
		self._disponibile = disponibile

	def get_codice(self) -> str:
		return self._codice
	
	def get_nome(self) -> str:
		return self._nome

	def get_prezzo(self) -> float:
		return self._prezzo
	
	def get_tempo_preparazione(self) -> int:
		return self._tempo_preparazione
	
	def get_allergeni(self) -> List[str]:
		return self._allergeni
	
	def is_disponibile(self) -> bool:
		return self._disponibile
	
	def set_disponibile(self, stato : bool) -> None:
		self._disponibile = stato

	def to_string(self) -> str:
		return f'{self._codice}: {self._nome} ({self._prezzo}€) pronto in {self._tempo_preparazione} minuti'

class PrimoPiatto(ElementoMenu):
	def __init__(self, codice: str, nome: str, prezzo: float, tempo_preparazione: int, allergeni: list, disponibile : bool):
		super().__init__(codice, nome, prezzo, tempo_preparazione, allergeni, disponibile)
		self._vegetariano = False
		self._tipo_pasta = ''

	def get_tipo_pasta(self) -> str:
		return self._tipo_pasta
	
	def set_tipo_pasta(self, tipo : str) -> None:
		self._tipo_pasta = tipo
	
	def is_vegetariano(self) -> bool:
		return self._vegetariano
	
	def set_vegetariano(self, vegetariano : bool) -> None:
		self._vegetariano = vegetariano
	
class SecondoPiatto(ElementoMenu):
	def __init__(self, codice: str, nome: str, prezzo: float, tempo_preparazione: int, allergeni: list, disponibile : bool):
		super().__init__(codice, nome, prezzo, tempo_preparazione, allergeni, disponibile)
		self._cottura_default : str = ''

	def get_cottura_default(self) -> str:
		return self._cottura_default

	def set_cottura_default(self, cottura : str) -> None:
		self._cottura_default = cottura

	def to_string(self) -> str:
		return f'{super().to_string()} cottura {self._cottura_default}'

class Ordine:
	def __init__(self, numero_ordine: str, data_ora: datetime, stato: str, elementi: List[ElementoMenu]):
		self._numero_ordine = numero_ordine
		self._data_ora = data_ora
		self._stato = stato
		self._elementi = elementi

	def get_numero_ordine(self) -> str:
		return self._numero_ordine
	
	def get_data_ora(self) -> datetime:
		return self._data_ora
	
	def get_stato(self) -> str:
		return self._stato
	
	def set_stato(self, stato : str) -> None:
		if stato.lower() in ["in_attesa", "in_preparazione", "pronto", "servito"]:
			self._stato = stato.lower()

	def aggiungi_elemento(self, elemento : ElementoMenu) -> None:
		if elemento not in self._elementi:
			self._elementi.append(elemento)
	
	def rimuovi_elemento(self, elemento : ElementoMenu) -> None:
		self._elementi.remove(elemento)
	
	def calcola_totale(self) -> float:
		totale = 0

		for e in self._elementi:
			totale += e.get_prezzo()

		return totale

class Tavolo:
	def __init__(self, numero: int, posti: int, stato: str):
		self._numero = numero
		self._posti = posti
		self.set_stato(stato)
		self._ordini = []

	def get_numero(self) -> int:
		return self._numero
	
	def get_posti(self) -> int:
		return self._posti
	
	def is_libero(self) -> bool:
		return self._stato.lower() == 'libero'
	
	def set_stato(self, stato : str) -> None:
		if stato.lower() in ["libero", "occupato"]:
			self._stato = stato.lower()

	def aggiungi_ordine(self, ordine : Ordine) -> None:
		if ordine not in self._ordini:
			self._ordini.append(ordine)

	def get_ordini_attivi(self) -> List[Ordine]:
		ris = []

		for ordine in self._ordini:
			if ordine.get_stato().lower() != 'servito':
				ris.append(ordine)

		return ris

def main():
	# Creazione elementi del menu
	primo = PrimoPiatto("P1", "Spaghetti Carbonara", 12.0, 15, ["uova", "glutine"], True)
	primo.set_tipo_pasta("spaghetti")
	primo.set_vegetariano(False)
	# print(primo.to_string())

	secondo = SecondoPiatto("S1", "Bistecca", 18.0, 20, [], True)
	secondo.set_cottura_default("media")
	# print(secondo.to_string())

	# Creazione tavolo e ordine
	tavolo = Tavolo(1, 4, "libero")
	ordine = Ordine("ORD1", datetime.now(), "in_attesa", [])

	# Aggiunta elementi all'ordine
	ordine.aggiungi_elemento(primo)
	ordine.aggiungi_elemento(secondo)

	# Associazione ordine al tavolo
	tavolo.aggiungi_ordine(ordine)
	tavolo.set_stato("occupato")

	# Calcoli
	print(f"Totale ordine: {ordine.calcola_totale()}€")  # Output: Totale ordine: 30.0€

	# Gestione stato ordine
	ordine.set_stato("in_preparazione")
	print(f"Stato ordine: {ordine.get_stato()}")  # Output: Stato ordine: in_preparazione

	# Informazioni tavolo
	print(f"Tavolo numero: {tavolo.get_numero()}")
	print(f"Stato tavolo: {'libero' if tavolo.is_libero() else 'occupato'}")
	print(f"Ordini attivi: {len(tavolo.get_ordini_attivi())}")

if __name__ == '__main__':
	main()