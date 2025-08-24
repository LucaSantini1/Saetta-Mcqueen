from enum import Enum
from typing import List, Dict

class Direzione(Enum):
	UP = "UP"
	DOWN = "DOWN"
	LEFT = "LEFT"
	RIGHT = "RIGHT"

class ClassePersonaggio(Enum):
	GUERRIERO = "GUERRIERO"
	MAGO = "MAGO"
	LADRO = "LADRO"

class Oggetto:
	def __init__(self, nome : str, descrizione : str):
		self.nome = nome
		self.descrizione = descrizione
		self.raccoglibile = True
		self.posizione : "Stanza | Personaggio" = None

class Personaggio:
	def __init__(self, nome : str, classe : ClassePersonaggio):
		self.nome = nome
		self.classe = classe
		self.livello = 1
		self.vita = 100
		self.stanza = None
		self.oggetti : List[Oggetto] = []

	def muovi(self, direzione : Direzione):
		# controllo se sono in una stanza
		if self.stanza is not None:
			altra_stanza = self.stanza.stanze_collegate[direzione]
			# esiste una stanza collegata nella direzione che voglio
			if altra_stanza is not None:
				self.stanza = altra_stanza
				return True
		return False

class Giocatore:
	def __init__(self, username : str, email : str):
		self.username = username
		self.email = email
		self.personaggi : Dict[ClassePersonaggio, List[Personaggio]] = {}

		# creo GUERRIERO : [], LADRO : [], MAGO : []
		for c in ClassePersonaggio:
			self.personaggi[c] = []

	def crea_personaggio(self, nome : str, classe : ClassePersonaggio):
		p = Personaggio(nome, classe)
		self.personaggi[classe].append(p)
		return p
	
	def get_personaggi_classe(self, classe : ClassePersonaggio):
		return self.personaggi[classe]

class Stanza:
	def __init__(self, nome : str, descrizione : str):
		self.nome = nome
		self.descrizione = descrizione
		self.oggetti : List[Oggetto] = []
		self.stanze_collegate : Dict[Direzione, "Stanza"] = {}

		# creo UP : None, DOWN : None, LEFT : None, RIGHT : None
		for d in Direzione:
			self.stanze_collegate[d] = None

	def collega_stanza(self, direzione : Direzione, stanza : "Stanza"):
		if self.stanze_collegate[direzione] is None:
			self.stanze_collegate[direzione] = stanza
			return True
		return False

# s = Stanza("S1", "S1")
# print(s.stanze_collegate)