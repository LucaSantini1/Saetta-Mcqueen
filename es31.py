from datetime import datetime

class Domanda:
	def __init__(self, testo: str, opzioni: list, risposta_corretta: int):
		self.testo = testo
		self.opzioni = opzioni
		self.risposta_corretta = risposta_corretta

	def verificaRisposta(self, risposta: int) -> bool:
		return risposta == self.risposta_corretta
	
	def __str__(self):
		ris = f"{self.testo}\n"

		for i in range(len(self.opzioni)):
			ris += f"\t{i}. {self.opzioni[i]} {'(*)' if self.risposta_corretta == i else ''}\n"

		return ris

class Quiz:
	def __init__(self, titolo: str, punteggio_minimo: int):
		self.titolo = titolo
		self.punteggio_minimo = punteggio_minimo
		self.punteggio = 0
		self.domande : list[Domanda] = []

	def aggiungiDomanda(self, domanda : Domanda):
		if domanda not in self.domande:
			self.domande.append(domanda)

	def valutaRisposte(self, risposte: list[int]) -> int:
		risultato = 0

		if len(risposte) == len(self.domande):
			for i in range(len(self.domande)):
				if self.domande[i].verificaRisposta(risposte[i]):
					risultato += 1

		self.punteggio = risultato

		return risultato

	def verificaSuperamento(self, punteggio: float) -> bool:
		return self.punteggio >= punteggio
	
	def __str__(self):
		ris = f"{self.titolo}\n"

		for domanda in self.domande:
			ris += f"- {domanda}\n"

		return ris

class Corso:
	def __init__(self, titolo : str, descrizione : str, docente : str):
		self.titolo = titolo
		self.descrizione = descrizione
		self.docente = docente
		self.iscritti : list[Studente] = []
		self.quiz : Quiz = None

	def impostaQuiz(self, quiz: Quiz):
		self.quiz = quiz

	def iscriviStudente(self, studente: "Studente"):
		if studente not in self.iscritti:
			self.iscritti.append(studente)

		if self not in studente.corsiIscritti:
			studente.corsiIscritti.append(self)

class QuizAttempt:
	def __init__(self, quiz : Quiz, studente : "Studente"):
		self.quiz = quiz
		self.studente = studente
		self.risposte = []
		self.dataOra = None
		self.punteggio = 0
		self.superato = False

	def submitRisposte(self, risposte: list[int]):
		self.risposte = risposte
		self.dataOra = datetime.now()
		self.calcolaPunteggio()

	def calcolaPunteggio(self) -> int:
		self.punteggio = self.quiz.valutaRisposte(self.risposte)
		self.superato = self.quiz.verificaSuperamento(self.punteggio)

	def __str__(self):
		ris = f"{self.quiz.titolo}\n"

		for d in range(len(self.quiz.domande)):
			domanda = self.quiz.domande[d]
			ris += f"- {domanda.testo}\n"
			for i in range(len(domanda.opzioni)):
				ris += f"\t{i}. {domanda.opzioni[i]} {'(*)' if domanda.risposta_corretta == i else ''} {'<-' if self.risposte[d] == i else ''}\n"
			ris += f'Punteggio: {1 if self.risposte[d] == domanda.risposta_corretta else 0} / 1\n\n'

		ris += f"Punteggio totale: {self.punteggio} / {len(self.quiz.domande)}\n\n"
		ris += f"Superato: {'Si' if self.superato else 'No'}\n"

		return ris

class Studente:
	def __init__(self, nome: str, cognome: str, email : str):
		self.nome = nome
		self.cognome = cognome
		self.email = email
		self.corsiIscritti : list[Corso] = []
		self.tentativi : list[QuizAttempt] = []

	def tentaQuiz(self, quiz : Quiz, risposte : list[int]) -> bool:
		quiz_attempt = QuizAttempt(quiz, self)
		quiz_attempt.submitRisposte(risposte)
		self.tentativi.append(quiz_attempt)
		return quiz_attempt.superato

# Esempio di utilizzo
if __name__ == "__main__":
	# Creare un corso
	corso_python = Corso(
		titolo = "Corso Python", 
		descrizione = "Introduzione a Python", 
		docente = "Prof. Rossi")

	# Creare un quiz
	quiz = Quiz("Quiz Python Base", punteggio_minimo = 2)

	# Aggiungere domande al quiz
	domanda1 = Domanda(
		testo = "Cosa è Python?", 
		opzioni = ["Un serpente", "Un linguaggio di programmazione", "Un gioco"],
		risposta_corretta = 1
	)
	
	domanda2 = Domanda(
		testo = "Quale dei seguenti è un framework web per Python?",
		opzioni = ["Django", "Flask", "Pyramid"],
		risposta_corretta = 0
	)

	domanda3 = Domanda(
		testo = "Quale linguaggio è noto come il 'linguaggio del web'?",
		opzioni = ["Python", "JavaScript", "Java"],
		risposta_corretta = 1
	)

	quiz.aggiungiDomanda(domanda1)
	quiz.aggiungiDomanda(domanda2)
	quiz.aggiungiDomanda(domanda3)

	# Impostare il quiz per il corso
	corso_python.impostaQuiz(quiz)

	# Creare uno studente
	studente = Studente("Mario", "Rossi", "mario.rossi@example.com")

	corso_python.iscriviStudente(studente)

	# print studenti del corso
	print(f"Studenti del corso {corso_python.titolo}:")
	for studente in corso_python.iscritti:
		print(studente.nome)
	print()
	
	print(quiz)

	passato = studente.tentaQuiz(quiz, [1, 0, 0])

	print(studente.tentativi[0])
