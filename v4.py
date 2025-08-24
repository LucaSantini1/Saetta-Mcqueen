from datetime import datetime

class Animale:
	def __init__(self, codiceIdentificativo: str, nome: str, eta: int, peso : float):
		self.codiceIdentificativo = codiceIdentificativo
		self.nome = nome
		self.eta = eta
		self.peso = peso
		self.habitat_corrente = None
		self.storico_visite = []

	def aggiungi_visita(self, visita : "VisitaVeterinaria"):
		if visita not in self.storico_visite:
			self.storico_visite.append(visita)

class Mammifero(Animale):
	def __init__(self, codiceIdentificativo: str, nome: str, eta: int, peso : float, tipoPelliccia : str, temperaturaCorpo : float, periodoGestazione : int):
		super().__init__(codiceIdentificativo, nome, eta, peso)
		self.tipoPelliccia = tipoPelliccia
		self.temperaturaCorpo = temperaturaCorpo
		self.periodoGestazione = periodoGestazione

class Rettile(Animale):
	def __init__(self, codiceIdentificativo: str, nome: str, eta: int, peso : float, velenoso : bool):
		super().__init__(codiceIdentificativo, nome, eta, peso)
		self.velenoso = velenoso

class Veterinario:
	def __init__(self, matricola : str, nome : str, cognome : str, specializzazione : str, anniEsperienza : int):
		self.matricola = matricola
		self.nome = nome
		self.cognome = cognome
		self.specializzazione = specializzazione
		self.anniEsperienza = anniEsperienza

	def effettua_visita(self, animale : Animale, diagnosi : str, trattamento : str):
		return VisitaVeterinaria(datetime.now(), diagnosi, trattamento, self, animale)

class Habitat:
	def __init__(self, codiceArea : str, nome : str, dimensione : float):
		self.codiceArea = codiceArea
		self.nome = nome
		self.dimensione = dimensione
		self.animali = []

	def aggiungi_animale(self, animale : Animale):
		for a in self.animali:
			if type(a) != type(animale):
				return

		if animale not in self.animali:
			self.animali.append(animale)

	def rimuovi_animale(self, animale : Animale):
		self.animali.remove(animale)

	def get_animali(self):
		return self.animali
	
	def get_eta_media(self):
		ris = 0
		for a in self.animali:
			ris += a.eta
		if len(self.animali) > 0:
			return ris / len(self.animali)
		else:
			return -1

class VisitaVeterinaria:
	def __init__(self, data : datetime, diagnosi : str, trattamentoProposto : str, veterinario : Veterinario, animale : Animale):
		self.data = data
		self.diagnosi = diagnosi
		self.trattamentoProposto = trattamentoProposto
		self.veterinario = veterinario
		self.animale = animale
		self.animale.aggiungi_visita(self)

class SistemaGestioneZoo:
	def __init__(self):
		self.animali = []
		self.habitats = []
		self.veterinari = []
		self.visite = []

	def aggiungi_animale(self, animale : Animale):
		if animale not in self.animali:
			self.animali.append(animale)

	def rimuovi_animale(self, animale : Animale):
		if animale.habitat_corrente is not None:
			animale.habitat_corrente.rimuovi_animale(animale)
		self.animali.remove(animale)

	def assegna_habitat(self, animale : Animale, habitat : Habitat):
		if habitat not in self.habitats:
			self.habitats.append(habitat)

		# Non abbiamo l'animale nel sistema
		if animale not in self.animali:
			return False
		
		# controllo che non sia in altri habitat
		for h in self.habitats:
			if h != habitat:
				if animale in h.animali:
					return False

		# Assegno habitat e animale se compatibili
		if habitat in self.get_habitat_compatibili(animale):
			if animale.habitat_corrente is None:
				animale.habitat_corrente = habitat
			else:
				animale.habitat_corrente.rimuovi_animale(animale)

			habitat.aggiungi_animale(animale)
		
			return True
		
		return False
	
	def registra_visita(self, visita : VisitaVeterinaria):
		if visita not in self.visite:
			self.visite.append(visita)

	def get_animali_habitat(self, habitat : Habitat):
		if habitat in self.habitats:
			return habitat.animali
		return []
	
	def get_storico_visite(self, animale : Animale):
		return animale.storico_visite
	
	def get_habitat_compatibili(self, animale : Animale):
		ris = []

		for h in self.habitats:
			compatibile = True

			# Controllo se ci sono animali di tipo diverso 
			# -> Habitat non compatibile
			# -> compatibile = False
			for a in h.animali:
				if type(a) != type(animale):
					compatibile = False

			if compatibile:
				ris.append(h)

		return ris
	
	def calcola_eta_media_per_habitat(self):
		ris = {}

		for h in self.habitats:
			ris[h.nome] = h.get_eta_media()

		return ris

def main():
	# Creazione del sistema
	zoo = SistemaGestioneZoo()

	# Creazione degli habitat
	savana = Habitat("H001", "Savana Africana", 1000.0)
	rettilario = Habitat("H002", "Rettilario", 500.0)
	zoo.habitats.extend([savana, rettilario])

	# Creazione dei veterinari
	vet1 = Veterinario("V001", "Mario", "Rossi", "Mammiferi", 10)
	vet2 = Veterinario("V002", "Laura", "Bianchi", "Rettili", 8)
	zoo.veterinari.extend([vet1, vet2])

	# Creazione degli animali
	leone = Mammifero("M001", "Simba", 5, 180.0, "Folta", 38.5, 110)
	serpente = Rettile("R001", "Kaa", 3, 5.0, True)
	giraffa = Mammifero("M002", "Melman", 7, 800.0, "Maculata", 38.0, 450)

	# Aggiunta degli animali al sistema
	for animale in [leone, serpente, giraffa]:
		zoo.aggiungi_animale(animale)

	# Assegnazione degli habitat
	zoo.assegna_habitat(leone, savana)
	zoo.assegna_habitat(giraffa, savana)
	success = zoo.assegna_habitat(serpente, savana)
	print("\nTentativo di mettere serpente in savana:", "Riuscito" if success else "Fallito")
	zoo.assegna_habitat(serpente, rettilario)

	# Effettuazione delle visite veterinarie
	visita1 = vet1.effettua_visita(leone, "Controllo di routine", "Somministrazione vaccino annuale")
	zoo.registra_visita(visita1)

	visita2 = vet2.effettua_visita(serpente, "Infezione batterica", "Antibiotico per 7 giorni")
	zoo.registra_visita(visita2)

	# Stampa delle informazioni
	print("\n=== Stato dello Zoo ===")

	print("\nAnimali nella Savana:")
	for animale in zoo.get_animali_habitat(savana):
		print(f"- {animale.nome} ({animale.codiceIdentificativo})")

	print("\nAnimali nel Rettilario:")
	for animale in zoo.get_animali_habitat(rettilario):
		print(f"- {animale.nome} ({animale.codiceIdentificativo})")

	print("\nEtà media per habitat:")
	for habitat, eta_media in zoo.calcola_eta_media_per_habitat().items():
		print(f"- {habitat}: {eta_media:.1f} anni")

	print("\nStorico visite di Simba:")
	for visita in zoo.get_storico_visite(leone):
		print(f"- Data: {visita.data}")
		print(f"  Veterinario: {visita.veterinario.nome} {visita.veterinario.cognome}")
		print(f"  Diagnosi: {visita.diagnosi}")
		print(f"  Trattamento: {visita.trattamentoProposto}")

if __name__ == "__main__":
	main()

# Tentativo di mettere serpente in savana: Fallito

# === Stato dello Zoo ===

# Animali nella Savana:
# - Simba (M001)
# - Melman (M002)

# Animali nel Rettilario:
# - Kaa (R001)

# Età media per habitat:
# - Savana Africana: 6.0 anni
# - Rettilario: 3.0 anni

# Storico visite di Simba:
# - Data: 2025-02-11 15:27:06.489484
#   Veterinario: Mario Rossi
#   Diagnosi: Controllo di routine
#   Trattamento: Somministrazione vaccino annuale
