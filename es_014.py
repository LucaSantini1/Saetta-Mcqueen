class Studente:
    def __init__(self, nome, matricola):
        self.nome = nome
        self.matricola = matricola
        self.corsi = []

    def aggiungi_corso(self, corso):
        if corso not in self.corsi:
            self.corsi.append(corso)
            corso.aggiungi_studente(self)

    def rimuovi_corso(self, corso):
        if corso in self.corsi:
            self.corsi.remove(corso)
            corso.rimuovi_studente(self)

class Corso:
    def __init__(self, titolo, codice):
        self.titolo = titolo
        self.codice = codice
        self.studenti = []

    def aggiungi_studente(self, studente):
        if studente not in self.studenti:
            self.studenti.append(studente)
            studente.aggiungi_corso(self)

    def rimuovi_studente(self, studente):
        if studente in self.studenti:
            self.studenti.remove(studente)
            studente.rimuovi_corso(self)

studente1 = Studente("Alice Rossi", "MAT123")
studente2 = Studente("Marco Bianchi", "MAT456")

corso1 = Corso("Programmazione Python", "PY101")
corso2 = Corso("Database Relazionali", "DB201")
corso3 = Corso("Sistemi Operativi", "SO301")

studente1.aggiungi_corso(corso1)
studente1.aggiungi_corso(corso2)
studente2.aggiungi_corso(corso2)
studente2.aggiungi_corso(corso3)

print(f"{studente1.nome} è iscritto ai seguenti corsi:")
for corso in studente1.corsi:
    print(f"- {corso.titolo} ({corso.codice})")

print(f"\n{corso2.titolo} ha i seguenti studenti iscritti:")
for studente in corso2.studenti:
    print(f"- {studente.nome} ({studente.matricola})")