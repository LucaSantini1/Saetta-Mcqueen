class Pagamento:
    def processa_pagamento(self):
        raise NotImplementedError("Questo metodo deve essere implementato dalle classi derivate.")

class CartaDiCredito(Pagamento):
    def __init__(self, numero_carta, scadenza, cvv):
        self.numero_carta = numero_carta
        self.scadenza = scadenza
        self.cvv = cvv

    def processa_pagamento(self):
        return f"Pagamento elaborato con carta di credito: {self.numero_carta}"

class PayPal(Pagamento):
    def __init__(self, email):
        self.email = email

    def processa_pagamento(self):
        return f"Pagamento elaborato con PayPal: {self.email}"

def elabora_pagamento(pagamento):
    print(pagamento.processa_pagamento())

if __name__ == "__main__":
    carta = CartaDiCredito("1234-5678-9012-3456", "12/25", "123")
    paypal = PayPal("utente@example.com")

    elabora_pagamento(carta)
    elabora_pagamento(paypal)