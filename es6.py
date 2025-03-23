# Definisci una classe base chiamata Pagamento con un metodo processa_pagamento
# Definisci una classe derivata chiamata CartaDiCredito che eredita dalla classe Pagamento.
# Implementa il metodo processa_pagamento per gestire i pagamenti con carta di credito.
# Definisci una classe derivata chiamata PayPal che eredita dalla classe Pagamento.
# Implementa il metodo processa_pagamento per gestire i pagamenti con PayPal.
# Crea una funzione che accetti un oggetto di tipo Pagamento e chiami il metodo processa_pagamento su di esso,
# dimostrando il polimorfismo.

class Pagamento:
	def __init__(self, mittente : str):
		self.mittente = mittente

	def processa_pagamento(self):
		pass


class CartaDiCredito(Pagamento):
	def __init__(self, mittente : str, numero : str, scadenza : str, CVC : str):
		super().__init__(mittente)
		self.numero = numero
		self.scadenza = scadenza
		self.CVC = CVC

	def processa_pagamento(self):
		print(f'Elaborazione pagamento con Carta di Credito per {self.mittente}')

class PayPal(Pagamento):
	def __init__(self, mittente : str, password : str):
		super().__init__(mittente)
		self.password = password

	def processa_pagamento(self):
		print(f'Elaborazione pagamento con PayPal per {self.mittente}')


# Esempio di utilizzo
def effettua_pagamento(metodo_di_pagamento: Pagamento):
	metodo_di_pagamento.processa_pagamento()

pagamento_carta = CartaDiCredito("Mario Rossi", "1234 5678 9012 3456", "12/23", "123")
pagamento_paypal = PayPal("mario.rossi@example.com", "password123")

effettua_pagamento(pagamento_carta)  # Output: Elaborazione pagamento con Carta di Credito per Mario Rossi
effettua_pagamento(pagamento_paypal)  # Output: Elaborazione pagamento con PayPal per mario.rossi@example.com
