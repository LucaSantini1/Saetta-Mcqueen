class Auto:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
        self.motore = None
        
        
    def get_marca(self):
        return self.marca
        
    def set_marca(self, marca):
        self.marca = marca
        
    def get_modello(self):
        return self.modello
    
    def set_modello(self, modello):
        self.modello = modello
        
    def associa_motore(self, motore):
        self.Motore = Motore
        motore.associa_auto(self)
    

class Motore:
    def __init__(self, numero_seriale, tipo):
        self.numero_seriale = numero_seriale
        self.tipo = tipo
        self.auto = None
        
    def get_numero_seriale(self):
        return self.numero_seriale
        
    def set_numero_seriale(self, numero_seriale):
        self.numero_seriale = numero_seriale
        
    def get_tipo(self):
        return self.tipo
    
    def set_tipo(self, tipo):
        self.tipo = tipo
        
    def associa_auto(self, auto):
        self.auto = Auto
        motore.associa_motore(self)
        
        
    