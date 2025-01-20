class Allenatore:
    def __init__(self, nome, cognome, specializzazione):
        self.nome = nome
        self.cognome = cognome
        self.specializzazione = specializzazione
        self.corsi = []

    def __str__(self):
        return f"Allenatore: {self.nome} {self.cognome}, Specializzazione: {self.specializzazione}"


class Membro:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
        self.allenatore = None
        self.corsi = []
        self.scheda_allenamento = None

    def set_allenatore(self, allenatore):
        self.allenatore = allenatore

    def iscrivi_corso(self, corso):
        self.corsi.append(corso)
        corso.aggiungi_membro(self)

    def set_scheda_allenamento(self, scheda):
        self.scheda_allenamento = scheda

    def __str__(self):
        corsi_nomi = [corso.nome for corso in self.corsi]
        return f"Membro: {self.nome} {self.cognome}, Allenatore: {self.allenatore.nome} {self.allenatore.cognome}, Corsi: {', '.join(corsi_nomi)}, Scheda: {self.scheda_allenamento}"


class Corso:
    def __init__(self, nome, durata, allenatore):
        self.nome = nome
        self.durata = durata
        self.allenatore = allenatore
        self.membri = []
        allenatore.corsi.append(self)

    def aggiungi_membro(self, membro):
        self.membri.append(membro)

    def __str__(self):
        return f"Corso: {self.nome}, Durata: {self.durata}, Allenatore: {self.allenatore.nome} {self.allenatore.cognome}"


class SchedaAllenamento:
    def __init__(self, membro, esercizi):
        self.membro = membro
        self.esercizi = esercizi

    def __str__(self):
        return f"Scheda di {self.membro.nome} {self.membro.cognome}: {', '.join(self.esercizi)}"


def main():
    allenatore1 = Allenatore("Giovanni", "Rossi", "Fitness")
    allenatore2 = Allenatore("Luca", "Bianchi", "Yoga")

    membro1 = Membro("Anna", "Verdi")
    membro2 = Membro("Marco", "Neri")

    membro1.set_allenatore(allenatore1)
    membro2.set_allenatore(allenatore2)

    corso1 = Corso("Pilates", "3 mesi", allenatore1)
    corso2 = Corso("HIIT", "6 mesi", allenatore1)
    corso3 = Corso("Yoga Avanzato", "4 mesi", allenatore2)

    membro1.iscrivi_corso(corso1)
    membro1.iscrivi_corso(corso2)
    membro2.iscrivi_corso(corso3)

    scheda1 = SchedaAllenamento(membro1, ["Esercizio 1: Squat", "Esercizio 2: Push-up"])
    scheda2 = SchedaAllenamento(membro2, ["Esercizio 1: Plank", "Esercizio 2: Burpee"])

    membro1.set_scheda_allenamento(scheda1)
    membro2.set_scheda_allenamento(scheda2)

    print(membro1)
    print(membro2)


if __name__ == "__main__":
    main()