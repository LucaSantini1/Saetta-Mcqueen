# Istruzioni
# Definisci una classe base chiamata Piatto con attributi di istanza nome, prezzo e disponibile.
# Implementa metodi di istanza nella classe Piatto per accedere e modificare questi attributi.
# Aggiungi un metodo ordina che imposta l'attributo disponibile a False e un metodo disponi che lo imposta a True.
# Definisci una classe derivata chiamata Antipasto che eredita dalla classe Piatto.
# Aggiungi attributi di istanza specifici per Antipasto, come ingredienti e porzione.
# Definisci una classe derivata chiamata Primo che eredita dalla classe Piatto.
# Aggiungi attributi di istanza specifici per Primo, come tipo_pasta e sugo.
# Definisci una classe derivata chiamata Secondo che eredita dalla classe Piatto.
# Aggiungi attributi di istanza specifici per Secondo, come tipo_carne e cottura.
# Definisci una classe derivata chiamata Dolce che eredita dalla classe Piatto.
# Aggiungi attributi di istanza specifici per Dolce, come tipo_dolce e calorie.
# Implementa metodi di istanza nelle classi Antipasto, Primo, Secondo e Dolce per accedere e modificare i loro attributi specifici.
# Implementa una funzione di ricerca che permette di cercare piatti per nome o prezzo.
# Implementa una funzione calcola_conto che prende una lista di piatti ordinati e restituisce il totale del conto.
# Implementa una funzione stampa_menu che prende una lista di piatti e stampa le informazioni di tutti i piatti.
# Esempio di Utilizzo
# class Piatto:
#     ...
#     def __str__(self):
#         return f"{self.nome} - {self.prezzo}€ - {'Disponibile' if self.disponibile else 'Non disponibile'}"
#

class Piatto:
	def __init__(self, nome : str, prezzo : float):
		self.nome = nome
		self.prezzo = prezzo
		self.disponibile = True

	def get_nome(self):
		return self.nome

	def get_prezzo(self):
		return self.prezzo

	def is_disponibile(self):
		return self.disponibile

	def set_nome(self, nome : str):
		self.nome = nome

	def set_prezzo(self, prezzo : float):
		self.prezzo = prezzo

	def ordina(self):
		self.disponibile = False

	def disponi(self):
		return self.disponibile

	def __str__(self):
		return f"{self.nome} - {self.prezzo}€ - {'Disponibile' if self.disponibile else 'Non disponibile'}"

class Antipasto(Piatto):
	def __init__(self, nome: str, prezzo: float, ingredienti: list, porzione: str):
		super().__init__(nome, prezzo)
		self.ingredienti = ingredienti
		self.porzione = porzione

	def get_ingredienti(self):
		return self.ingredienti

	def get_porzione(self):
		return self.porzione

	def set_ingredienti(self, ingredienti: list):
		self.ingredienti = ingredienti

	def set_porzione(self, porzione: str):
		self.porzione = porzione

	def __str__(self):
		ris = f"Antipasto: {self.nome} - {self.prezzo}€ - "
		ris += "Disponibile" if self.disponibile else "Non disponibile"
		ris += f" - Ingredienti: {", ".join(self.ingredienti)} - Porzione: {self.porzione}"
		return ris

class Primo(Piatto):
	def __init__(self, nome: str, prezzo: float, tipo_pasta: str, sugo: str):
		super().__init__(nome, prezzo)
		self.tipo_pasta = tipo_pasta
		self.sugo = sugo

	def get_tipo_pasta(self):
		return self.tipo_pasta

	def get_sugo(self):
		return self.sugo

	def set_tipo_pasta(self, tipo_pasta: str):
		self.tipo_pasta = tipo_pasta

	def set_sugo(self, sugo: str):
		self.sugo = sugo

	def __str__(self):
		ris = f"Primo: {self.nome} - {self.prezzo}€ - "
		ris += "Disponibile" if self.disponibile else "Non disponibile"
		ris += f" - Tipo Pasta: {self.tipo_pasta} - Sugo: {self.sugo}"
		return ris

class Secondo(Piatto):
	def __init__(self, nome: str, prezzo: float, tipo_carne: str, cottura: str):
		super().__init__(nome, prezzo)
		self.tipo_carne = tipo_carne
		self.cottura = cottura

	def get_tipo_carne(self):
		return self.tipo_carne

	def get_cottura(self):
		return self.cottura

	def set_tipo_carne(self, tipo_carne: str):
		self.tipo_carne = tipo_carne

	def set_cottura(self, cottura: str):
		self.cottura = cottura

	def __str__(self):
		ris = f"Secondo: {self.nome} - {self.prezzo}€ - "
		ris += "Disponibile" if self.disponibile else "Non disponibile"
		ris += f" - Tipo Carne: {self.tipo_carne} - Cottura: {self.cottura}"
		return ris

class Dolce(Piatto):
	def __init__(self, nome: str, prezzo: float, tipo_dolce: str, calorie: int):
		super().__init__(nome, prezzo)
		self.tipo_dolce = tipo_dolce
		self.calorie = calorie

	def get_tipo_dolce(self):
		return self.tipo_dolce

	def get_calorie(self):
		return self.calorie

	def set_tipo_dolce(self, tipo_dolce: str):
		self.tipo_dolce = tipo_dolce

	def set_calorie(self, calorie: int):
		self.calorie = calorie

	def __str__(self):
		ris = f"Dolce: {self.nome} - {self.prezzo}€ - "
		ris += "Disponibile" if self.disponibile else "Non disponibile"
		ris += f" - Tipo Dolce: {self.tipo_dolce} - Calorie: {self.calorie}"
		return ris

def ricercaNome(menu : list, nome : str):
	ris = []

	for p in menu:
		if p.get_nome() == nome:
			ris.append(p)

	return ris

def ricercaPrezzo(menu : list, prezzo : float):
	ris = []

	for p in menu:
		if p.get_prezzo() < prezzo:
			ris.append(p)

	return ris

def calcola_conto(piatti : list):
	ris = 0

	for p in piatti:
		ris += p.get_prezzo()

	return ris

def stampa_menu(piatti : list):
	for p in piatti:
		print(p)


# Esempio di utilizzo
antipasto = Antipasto("Bruschetta", 5.0, ["Pane", "Pomodoro", "Basilico"], "Piccola")
primo = Primo("Spaghetti alla Carbonara", 12.0, "Spaghetti", "Carbonara")
secondo = Secondo("Bistecca alla Fiorentina", 25.0, "Manzo", "Media")
dolce = Dolce("Tiramisù", 6.0, "Tiramisù", 450)

piatti_ordinati = [antipasto, primo, secondo, dolce]
conto_totale = calcola_conto(piatti_ordinati)
print(f"Il conto totale è: {conto_totale}€")  # Output: Il conto totale è: 48.0€

print("\nMenu del Ristorante:")
stampa_menu(piatti_ordinati)
# Output Atteso
# Il conto totale è: 48.0€
#
# Menu del Ristorante:
# Antipasto: Bruschetta - 5.0€ - Disponibile - Ingredienti: Pane, Pomodoro, Basilico - Porzione: Piccola
# Primo: Spaghetti alla Carbonara - 12.0€ - Disponibile - Tipo Pasta: Spaghetti - Sugo: Carbonara
# Secondo: Bistecca alla Fiorentina - 25.0€ - Disponibile - Tipo Carne: Manzo - Cottura: Media
# Dolce: Tiramisù - 6.0€ - Disponibile - Tipo Dolce: Tiramisù - Calorie: 450