class Dipendente:
    def __init__(self, nome, stipendio):
        self.nome = nome
        self.stipendio = stipendio

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_stipendio(self):
        return self.stipendio

    def set_stipendio(self, stipendio):
        self.stipendio = stipendio

class Manager(Dipendente):
    def __init__(self, nome, stipendio, numero_di_team):
        super().__init__(nome, stipendio)
        self.numero_di_team = numero_di_team

    def get_numero_di_team(self):
        return self.numero_di_team

    def set_numero_di_team(self, numero_di_team):
        self.numero_di_team = numero_di_team

class Sviluppatore(Dipendente):
    def __init__(self, nome, stipendio, linguaggio_di_programmazione):
        super().__init__(nome, stipendio)
        self.linguaggio_di_programmazione = linguaggio_di_programmazione

    def get_linguaggio_di_programmazione(self):
        return self.linguaggio_di_programmazione

    def set_linguaggio_di_programmazione(self, linguaggio_di_programmazione):
        self.linguaggio_di_programmazione = linguaggio_di_programmazione

if __name__ == "__main__":
    manager = Manager("Alice", 80000, 5)
    sviluppatore = Sviluppatore("Bob", 60000, "Python")

    print(f"Manager: {manager.get_nome()}, Stipendio: {manager.get_stipendio()}, Team: {manager.get_numero_di_team()}")
    print(f"Sviluppatore: {sviluppatore.get_nome()}, Stipendio: {sviluppatore.get_stipendio()}, Linguaggio: {sviluppatore.get_linguaggio_di_programmazione()}")