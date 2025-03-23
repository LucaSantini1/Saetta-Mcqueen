from datetime import datetime

class Animale:
    def __init__(self, codiceIdentificativo: str, nome: str, eta: int, peso: float):
        self.codiceIdentificativo = codiceIdentificativo
        self.nome = nome
        self.eta = eta
        self.peso = peso
        self.visite = []
        self.habitat = None

    def aggiungi_visita(self, visita):
        self.visite.append(visita)
        visita.assegna_animale(self)

    def assegna_habitat(self, h):
        self.habitat = h

class Habitat:
    def __init__(self, codiceArea: str, nome: str, dimensione: float):
        self.codiceArea = codiceArea
        self.nome = nome
        self.dimensione = dimensione
        self.animali = []

    def aggiungi_animale(self, animale: Animale):
        self.animali.append(animale)

    def rimuovi_animale(self, animale: Animale):
        self.animali.remove(animale)

    def get_animali(self):
        return self.animali

    def get_eta_media(self):
        media = 0
        if len(self.animali) > 0:
            # sum([a.eta for a in self.animali]) / len(self.animali)
            for a in self.animali:
                media += a.eta
            media /= len(self.animali)
        return media

class Mammifero(Animale):

    def __init__(self, codiceIdentificativo : str, nome : str, eta : int, peso : float, tipoPelliccia: str, temperaturaCorpo : float, periodoGestazione: int):
        super().__init__(codiceIdentificativo, nome, eta, peso)
        self.tipoPelliccia = tipoPelliccia
        self.temperaturaCorpo = temperaturaCorpo
        self.periodoGestazione = periodoGestazione

class Rettile(Animale):

    def __init__(self, codiceIdentificativo : str, nome : str, eta : int, peso : float, velenoso: bool):
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
        visita = VisitaVeterinaria(datetime.now(), diagnosi, trattamento)
        animale.aggiungi_visita(visita)
        visita.assegna_veterinario(self)
        return visita

class VisitaVeterinaria:
    def __init__(self, data: datetime, diagnosi: str, trattamentoProposto: str):
        self.data = data
        self.diagnosi = diagnosi
        self.trattamentoProposto = trattamentoProposto
        self.animale = None
        self.veterinario = None

    def assegna_animale(self, a : Animale):
        self.animale = a

    def assegna_veterinario(self, v : Veterinario):
        self.veterinario = v

class SistemaGestioneZoo:
    def __init__(self):
        self.habitats = []
        self.visite = []
        self.animali = []
        self.veterinari = []

    def aggiungi_animale(self, animale: Animale):
        self.animali.append(animale)

    def rimuovi_animale(self, animale: Animale):
        self.animali.remove(animale)

    def assegna_habitat(self, animale: Animale, habitat: Habitat):
        if habitat not in self.habitats:
            self.habitats.append(habitat)

        for h in self.habitats:
            if h == habitat:
                for a in h.get_animali():
                    if type(animale) != type(a):
                        return False

                h.aggiungi_animale(animale)
                self.animali.append(animale)
                animale.assegna_habitat(h)
                return True

    def registra_visita(self, visita: VisitaVeterinaria):
        self.visite.append(visita)

    def get_animali_habitat(self, habitat: Habitat):
        for h in self.habitats:
            if h == habitat:
                return h.get_animali()
        return None

    def get_storico_visite(self, animale: Animale):
        ris = []

        for v in self.visite:
            if v.animale == animale:
                ris.append(v)

        return ris

    def get_habitat_compatibili(self, animale: Animale):
        ris = []

        for h in self.habitats:
            aggiungi = True

            for a in h.animali:
                if type(a) != type(animale):
                    aggiungi = False

            if aggiungi:
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
