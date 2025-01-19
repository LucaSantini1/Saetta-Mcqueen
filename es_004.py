class Calcolatrice:
    @staticmethod
    def addizione(a, b):
        return a + b

    @staticmethod
    def sottrazione(a, b):
        return a - b

    @staticmethod
    def moltiplicazione(a, b):
        return a * b

    @staticmethod
    def divisione(a, b):
        if b == 0:
            return "Errore: Divisione per zero"
        return a / b

if __name__ == "__main__":
    print(Calcolatrice.addizione(5, 3))  # Output: 8
    print(Calcolatrice.sottrazione(5, 3))  # Output: 2
    print(Calcolatrice.moltiplicazione(5, 3))  # Output: 15
    print(Calcolatrice.divisione(5, 0))  # Output: Errore: Divisione per zero
    print(Calcolatrice.divisione(5, 2))  # Output: 2.5