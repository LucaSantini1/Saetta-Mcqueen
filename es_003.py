class Veicolo:
 
    numero_veicoli = 0

    def __init__(self):
     
        Veicolo.numero_veicoli += 1

    @classmethod
    def get_numero_veicoli(cls):
        """Restituisce il numero totale di veicoli creati."""
        return cls.numero_veicoli


if __name__ == "__main__":
    veicolo1 = Veicolo() 
    veicolo2 = Veicolo()  
    veicolo3 = Veicolo() 

    # Stampa il numero totale di veicoli creati
    print(f"Numero totale di veicoli creati: {Veicolo.get_numero_veicoli()}")  