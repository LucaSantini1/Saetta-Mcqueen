class Persona:
    def __init__(self, nome, eta, citta):
        self.nome = nome 
        self.eta = eta   
        self.citta = citta  

    def saluta(self):
        """Restituisce un saluto contenente il nome della persona."""
        return f"Ciao, mi chiamo {self.nome}!"

    def descrizione(self):
        """Restituisce una descrizione contenente l'età e la città della persona."""
        return f"Ho {self.eta} anni e vivo a {self.citta}."

if __name__ == "__main__":
    persona1 = Persona("Mario", 30, "Roma")
    print(persona1.saluta())          
    print(persona1.descrizione())    