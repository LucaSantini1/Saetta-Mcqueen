from typing import List

class Membro:
	def __init__(self, nome : str, cognome : str):
		self.__nome = nome
		self.__cognome = cognome
		self.__allenatore : Allenatore = None
		self.__corsi : List[Corso] = []
		self.__scheda_allenamento : SchedaAllenamento = None

	def set_allenatore(self, allenatore : "Allenatore"):
		if self.__allenatore is not None:
			self.__allenatore = allenatore
			allenatore.aggiungi_membro(self)
			return True
		return False

	def iscrivi_corso(self, corso : "Corso"):
		if corso not in self.__corsi:
			self.__corsi.append(corso)
			corso.aggiungi_membro(self)
			return True
		return False

	def set_scheda_allenamento(self, scheda : "SchedaAllenamento"):
		if self.__scheda_allenamento is None:
			self.__scheda_allenamento = scheda
			return True
		return False

	def __str__(self):
		return f"Membro: {self.__nome} {self.__cognome}"
	
class Allenatore:
	def __init__(self, nome : str, cognome : str, specializzazione : str):
		self.__nome = nome
		self.__cognome = cognome
		self.__specializzazione = specializzazione
		self.__membri : List[Membro] = []
		self.__corsi : List[Corso] = []

	def aggiungi_membro(self, membro : "Membro"):
		if membro not in self.__membri:
			self.__membri.append(membro)
			return True
		return False

	def aggiungi_corso(self, corso : "Corso"):
		if corso not in self.__corsi:
			self.__corsi.append(corso)
			return True
		return False

	def __str__(self):
		return f"Allenatore: {self.__nome} {self.__cognome}, Specializzazione: {self.__specializzazione}"

class Corso:
	def __init__(self, nome : str, durata : str, allenatore : "Allenatore"):
		self.__nome = nome
		self.__durata = durata
		self.__allenatore = allenatore
		self.__membri : List[Membro] = []
		allenatore.aggiungi_corso(self)

	def aggiungi_membro(self, membro : "Membro"):
		if membro not in self.__membri:
			self.__membri.append(membro)
			return True
		return False

	def __str__(self):
		return f"Corso: {self.__nome}, Durata: {self.__durata}, Allenatore: {self.__allenatore}"

class SchedaAllenamento:
	def __init__(self, membro : "Membro", esercizi : List[str]):
		self.__membro = membro
		self.__esercizi = esercizi
		membro.set_scheda_allenamento(self)

	def __str__(self):
		return f"Scheda di Allenamento per {self.__membro}: {self.__esercizi}"

def main():
	# Creazione degli allenatori
	allenatore1 = Allenatore("Giovanni", "Rossi", "Fitness")
	allenatore2 = Allenatore("Luca", "Bianchi", "Yoga")

	# Creazione dei membri
	membro1 = Membro("Anna", "Verdi")
	membro2 = Membro("Marco", "Neri")

	# Assegnazione degli allenatori ai membri
	membro1.set_allenatore(allenatore1)
	membro2.set_allenatore(allenatore2)

	# Creazione dei corsi
	corso1 = Corso("Pilates", "3 mesi", allenatore1)
	corso2 = Corso("HIIT", "6 mesi", allenatore1)
	corso3 = Corso("Yoga Avanzato", "4 mesi", allenatore2)

	# Iscrizione dei membri ai corsi
	membro1.iscrivi_corso(corso1)
	membro1.iscrivi_corso(corso2)
	membro2.iscrivi_corso(corso3)

	# Creazione delle schede di allenamento
	scheda1 = SchedaAllenamento(membro1, ["Esercizio 1: Squat", "Esercizio 2: Push-up"])
	scheda2 = SchedaAllenamento(membro2, ["Esercizio 1: Plank", "Esercizio 2: Burpee"])

	# Assegnazione delle schede di allenamento ai membri
	membro1.set_scheda_allenamento(scheda1)
	membro2.set_scheda_allenamento(scheda2)

	# Stampa delle informazioni
	print(membro1)
	print(membro2)

	print(scheda1)
	print(scheda2)

	# Stampa delle informazioni
	print(allenatore1)
	print(allenatore2)

	print(corso1)
	print(corso2)
	print(corso3)

if __name__ == "__main__":
	main()