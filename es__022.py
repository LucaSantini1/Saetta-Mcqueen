class Automobile:
    def __init__(self, targa, modello, categoria):
        self.targa = targa
        self.modello = modello
        self.categoria = categoria
        self.disponibile = True

    def noleggia(self):
        if self.disponibile:
            self.disponibile = False
        else:
            raise Exception("L'auto non è disponibile")

    def restituisci(self):
        self.disponibile = True

    def is_disponibile(self):
        return self.disponibile == True


class AgenziaNoleggio:
    def __init__(self):
        self.automobili = []
        self.noleggi = []

    def aggiungi_auto(self, auto):
        self.automobili.append(auto)

    def noleggia_auto(self, targa):
        for auto in self.automobili:
            if auto.targa == targa and auto.is_disponibile():
                auto.noleggia()
                self.noleggi.append(auto)
                return
        raise Exception("Auto non disponibile o non trovata")

    def visualizza_disponibili(self):
        return [auto for auto in self.automobili if auto.is_disponibile()]

    def visualizza_noleggi(self):
        return self.noleggi
    