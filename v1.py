
# Creare una gerarchia di classi che rappresenti diversi tipi di dispositivi elettronici in un sistema di gestione di un
# negozio di elettronica. Utilizzare l'ereditarietà per definire una classe base Dispositivo e classi derivate Smartphone,
# Laptop e Tablet che ereditano dalla classe base. Implementare metodi specifici per ogni tipo di dispositivo e aggiungere
# funzionalità avanzate come la gestione delle vendite, la ricerca di dispositivi, il calcolo del costo totale di acquisto
# e la stampa dell'inventario.

# Fase 1
#   Implementazione:
#   Definisci una classe base chiamata Dispositivo con attributi di istanza marca, modello, prezzo e disponibile.
#   Implementa metodi di istanza nella classe Dispositivo per accedere e modificare questi attributi.
#   Aggiungi un metodo vendi che imposta l'attributo disponibile a False e un metodo rifornisci che lo imposta a True.
#   Definisci le classi derivate Smartphone, Laptop e Tablet che ereditano dalla classe Dispositivo.
#   Aggiungi attributi di istanza specifici per ogni classe derivata.

# Fase 2
#   Implementazione:
#   Implementa metodi getter e setter per gli attributi delle classi Dispositivo, Smartphone, Laptop e Tablet.
#   Implementa il polimorfismo creando un metodo descrizione nella classe base Dispositivo e sovrascrivilo nelle classi
#   derivate per fornire una descrizione specifica di ogni tipo di dispositivo.

# Fase 3
#   Implementazione:
#   Aggiungi un attributo di classe numero_dispositivi nella classe Dispositivo che tiene traccia del numero totale di dispositivi creati.
#   Implementa un metodo di classe conta_dispositivi che restituisce il valore di numero_dispositivi.
#   Aggiungi un metodo statico calcola_sconto che calcola uno sconto sul prezzo di un dispositivo dato un valore percentuale.

# Fase 4
#   Aggiungere funzionalità avanzate per la gestione dell'inventario in una nuova classe Inventario.
#   Implementazione:
#   Implementa un metodo per cercare dispositivi con prezzo inferiore a un valore specificato.
#   Implementa un metodo per cercare solo dispositivi disponibili.


class Dispositivo:
	numero_dispositivi = 0

	def __init__(self, marca : str, modello : str, prezzo : float):
		self.marca = marca
		self.modello = modello
		self.prezzo = prezzo
		self.disponibile = True
		Dispositivo.numero_dispositivi += 1

	def vendi(self):
		self.disponibile = False

	def rifornisci(self):
		self.disponibile = True

	def get_marca(self):
		return self.marca

	def get_modello(self):
		return self.modello

	def get_prezzo(self):
		return self.prezzo

	def isDisponibile(self):
		return self.disponibile

	def set_marca(self, marca):
		self.marca = marca

	def set_modello(self, modello):
		self.modello = modello

	def set_prezzo(self, prezzo):
		self.prezzo = prezzo

	def set_disponibile(self, disponibile):
		self.disponibile = disponibile

	def descrizione(self):
		return f"Dispositivo {self.marca} - {self.modello} - {self.prezzo} - {self.disponibile}"

	@classmethod
	def conta_dispositivi(cls):
		return cls.numero_dispositivi

	@staticmethod
	def calcola_sconto(prezzo, percentuale):
		return prezzo * (100.0 - percentuale) / 100.0

class Smartphone(Dispositivo):
	def __init__(self, marca : str, modello : str, prezzo : float, memoria : float):
		super().__init__(marca, modello, prezzo)
		self.memoria = memoria

	def get_memoria(self):
		return self.memoria

	def set_memoria(self, memoria):
		self.memoria = memoria

	def descrizione(self):
		return f"Smartphone {self.marca} {self.modello} con {self.memoria}GB di memoria"

class Laptop(Dispositivo):
	def __init__(self, marca : str, modello : str, prezzo : float, RAM : int):
		super().__init__(marca, modello, prezzo)
		self.RAM = RAM

	def get_RAM(self):
		return self.RAM

	def set_RAM(self, RAM):
		self.RAM = RAM

	def descrizione(self):
		return f"Laptop {self.marca} {self.modello} con {self.RAM}GB di RAM"

class Tablet(Dispositivo):
	def __init__(self, marca : str, modello : str, prezzo : float, pollici : float):
		super().__init__(marca, modello, prezzo)
		self.pollici = pollici

	def get_pollici(self):
		return self.pollici

	def set_pollici(self, pollici):
		self.pollici = pollici

	def descrizione(self):
		return f"Tablet {self.marca} {self.modello} con schermo da {self.pollici} pollici"

class Inventario:
	def __init__(self):
		self.dispositivi = []

	def aggiungi_dispositivo(self, dispositivo : Dispositivo):
		self.dispositivi.append(dispositivo)

	def rimuovi_dispositivo(self, dispositivo : Dispositivo):
		self.dispositivi.remove(dispositivo)

	def cerca_per_prezzo(self, prezzo):
		# return [d for d in self.dispositivi if d.get_prezzo() < prezzo]

		ris = []

		for d in self.dispositivi:
			if d.get_prezzo() < prezzo:
				ris.append(d)

		return ris

	def cerca_disponibili(self):
		# return [d for d in self.dispositivi if d.isDisponibile]

		ris = []

		for d in self.dispositivi:
			if d.isDisponibile():
				ris.append(d)

		return ris

	def stampa_inventario(self):
		for d in self.dispositivi:
			print(d.descrizione())


def main():
	# Esempio di utilizzo
	# Fase 1
	smartphone = Smartphone("Apple", "iPhone 12", 999, 128)
	print(smartphone.get_marca())  # Output: Apple
	smartphone.vendi()
	print(smartphone.disponibile)  # Output: False

	# Fase 2
	laptop = Laptop("Dell", "XPS 13", 1200, 16)
	tablet = Tablet("Samsung", "Galaxy Tab S7", 650, 11)

	print(smartphone.descrizione())  # Output: Smartphone Apple iPhone 12 con 128GB di memoria
	print(laptop.descrizione())  # Output: Laptop Dell XPS 13 con 16GB di RAM
	print(tablet.descrizione())  # Output: Tablet Samsung Galaxy Tab S7 con schermo da 11 pollici

	# Fase 3
	print(Dispositivo.conta_dispositivi())  # Output: 3
	print(Dispositivo.calcola_sconto(1000, 10))  # Output: 900.0

	# Fase 4
	inventario = Inventario()
	inventario.aggiungi_dispositivo(smartphone)
	inventario.aggiungi_dispositivo(laptop)
	inventario.aggiungi_dispositivo(tablet)

	inventario.stampa_inventario()
	# Output:
	# Smartphone Apple iPhone 12 con 128GB di memoria
	# Laptop Dell XPS 13 con 16GB di RAM
	# Tablet Samsung Galaxy Tab S7 con schermo da 11 pollici

	# Cerca dispositivi per prezzo
	dispositivi_economici = inventario.cerca_per_prezzo(1000)
	print("Dispositivi con prezzo inferiore a 1000€:")
	for dispositivo in dispositivi_economici:
		print(dispositivo.descrizione())
	# Output:
	# Dispositivi con prezzo inferiore a 1000€:
	# Smartphone Apple iPhone 12 con 128GB di memoria
	# Tablet Samsung Galaxy Tab S7 con schermo da 11 pollici

	# Cerca dispositivi disponibili
	dispositivi_disponibili = inventario.cerca_disponibili()
	print("Dispositivi disponibili:")
	for dispositivo in dispositivi_disponibili:
		print(dispositivo.descrizione())
	# Output:
	# Dispositivi disponibili:
	# Laptop Dell XPS 13 con 16GB di RAM
	# Tablet Samsung Galaxy Tab S7 con schermo da 11 pollici

if __name__ == "__main__":
	main()