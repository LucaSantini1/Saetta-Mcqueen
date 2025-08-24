from typing import List, Dict
from enum import Enum
from datetime import datetime

class TipoTransazione(Enum):
	ENTRATA = "ENTRATA"
	USCITA = "USCITA"

class CategoriaSpesa(Enum):
	CIBO = "CIBO"
	TRASPORTI = "TRASPORTI"
	CASA = "CASA"
	SVAGO = "SVAGO"
	SALUTE = "SALUTE"
	ALTRO = "ALTRO"

class Transazione:
	id = 1
	def __init__(self, data : datetime, importo : float, descrizione : str):
		self.id_transazione = f'TX_{Transazione.id}'
		Transazione.id += 1
		self.data = data
		self.importo = importo
		self.descrizione = descrizione
		self.tipo : TipoTransazione = TipoTransazione.USCITA
		self.categoria : CategoriaSpesa = CategoriaSpesa.ALTRO
	
	def get_importo(self):
		return self.importo
	
	def get_data(self):
		return self.data

	def get_tipo(self):
		return self.tipo
	
	def get_categoria(self):
		return self.categoria
	
	def set_tipo(self, tipo : TipoTransazione):
		self.tipo = tipo
	
	def set_categoria(self, categoria : CategoriaSpesa):
		self.categoria = categoria

class ContoBancario:
	# saldo_iniziale : float = 0 -> saldo_iniziale diventa opzionale, se non lo metti vale 0
	def __init__(self, id_conto : str, nome_conto : str, saldo_iniziale : float = 0):
		self.id_conto = id_conto
		self.nome_conto = nome_conto
		self.saldo_attuale = saldo_iniziale
		self.transazioni : List[Transazione] = []

	def saldo_disponibile(self) -> float :
		return self.saldo_attuale

	def media_spese_totali(self) -> float :
		totale = 0
		count = 0

		for t in self.transazioni:
			if t.get_tipo() == TipoTransazione.USCITA:
				totale += t.get_importo() * -1
				count += 1

		if count == 0:
			return 0
		
		return totale / count

	def report_mensile(self) -> List[Transazione] :
		ris : List[Transazione] = []
		
		for t in self.transazioni:
			data = t.get_data()
			if data.month == datetime.now().month and data.year == datetime.now().year:
				ris.append(t)

		return ris

	def aggiungi_transazione(self, transazione: Transazione) -> None :
		if transazione not in self.transazioni:
			self.transazioni.append(transazione)
			self.saldo_attuale += transazione.get_importo()

class Utente:
	def __init__(self, id_utente : str, nome_utente : str, email : str):
		self.id_utente = id_utente
		self.nome_utente = nome_utente
		self.email = email
		self.conti : List[ContoBancario] = []

	def registra_transazione(self, conto: ContoBancario, importo: float, categoria: CategoriaSpesa, descrizione: str) -> Transazione :
		if conto in self.conti:
			ris = Transazione(datetime.now(), importo, descrizione)
			if importo > 0:
				ris.set_tipo(TipoTransazione.ENTRATA)
			else:
				ris.set_tipo(TipoTransazione.USCITA)
			ris.set_categoria(categoria)
			conto.aggiungi_transazione(ris)
			return ris
		return None

	def totale_spese_mensili(self) -> float :
		totale = 0
		
		for c in self.conti:
			transazioni_mensili = c.report_mensile()
			
			for t in transazioni_mensili:
				if t.get_tipo() == TipoTransazione.USCITA:
					totale += t.get_importo() * -1

		return totale

	def spese_per_categoria(self) -> Dict[CategoriaSpesa, float] :
		ris = {}

		for categoria in CategoriaSpesa:
			ris[categoria] = 0

		for c in self.conti:				
			for t in c.transazioni:
				if t.get_tipo() == TipoTransazione.USCITA:
					ris[t.get_categoria()] += t.get_importo() * -1

		return ris

	def categoria_piu_costosa(self) -> CategoriaSpesa :
		ris = CategoriaSpesa.ALTRO
		spesa = 0

		spese = self.spese_per_categoria()
		for categoria in spese:
			if spese[categoria] > spesa:
				spesa = spese[categoria]
				ris = categoria

		return ris


def main() -> None:
	# Creazione di un utente
	utente: Utente = Utente(id_utente="U1", nome_utente="Mario Rossi", email="mario.rossi@email.com")

	# Creazione di due conti bancari
	conto_principale: ContoBancario = ContoBancario(id_conto="C1", nome_conto="Conto Principale", saldo_iniziale=1000.0)
	conto_risparmi: ContoBancario = ContoBancario(id_conto="C2", nome_conto="Conto Risparmi", saldo_iniziale=5000.0)

	# Aggiunta dei conti all'utente
	utente.conti.extend([conto_principale, conto_risparmi])

	# Registrazione di alcune transazioni
	utente.registra_transazione(
		conto=conto_principale, importo=-50.0, categoria=CategoriaSpesa.CIBO, descrizione="Spesa settimanale"
	)

	utente.registra_transazione(
		conto=conto_principale, importo=-30.0, categoria=CategoriaSpesa.TRASPORTI, descrizione="Benzina"
	)

	utente.registra_transazione(
		conto=conto_principale, importo=1000.0, categoria=CategoriaSpesa.ALTRO, descrizione="Stipendio"
	)

	utente.registra_transazione(
		conto=conto_risparmi, importo=-200.0, categoria=CategoriaSpesa.SVAGO, descrizione="Weekend fuori città"
	)

	# Visualizzazione dei risultati
	print(f"\nUtente: {utente.nome_utente}")
	print(f"Email: {utente.email}")

	for conto in utente.conti:
		print(f"\nConto: {conto.nome_conto}")
		print(f"Saldo disponibile: €{conto.saldo_disponibile():.2f}")
		print(f"Media spese totali: €{conto.media_spese_totali():.2f}")

	print("\nStatistiche spese:")
	spese: Dict[CategoriaSpesa, float] = utente.spese_per_categoria()
	for categoria, importo in spese.items():
		if importo > 0:
			print(f"{categoria.value}: €{importo:.2f}")

	categoria_max: CategoriaSpesa = utente.categoria_piu_costosa()
	print(f"\nCategoria più costosa: {categoria_max.value}")
	print(f"Totale spese mensili: €{utente.totale_spese_mensili():.2f}")
if __name__ == "__main__":
	main()
