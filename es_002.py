class ContoBancario:
    def __init__(self, numero_conto, intestatario, saldo_iniziale=0):
        self.numero_conto = numero_conto  
        self.intestatario = intestatario 
        self._saldo = saldo_iniziale        

    def get_saldo(self):
        """Restituisce il valore dell'attributo privato _saldo."""
        return self._saldo

    def deposita(self, importo):
        """Incrementa il saldo di un importo specificato."""
        if importo > 0:
            self._saldo += importo
            print(f"Deposito di {importo} effettuato. Nuovo saldo: {self._saldo}.")
        else:
            print("L'importo del deposito deve essere positivo.")

    def preleva(self, importo):
        """Decrementa il saldo di un importo specificato, se sufficiente."""
        if importo > 0:
            if self._saldo >= importo:
                self._saldo -= importo
                print(f"Prelievo di {importo} effettuato. Nuovo saldo: {self._saldo}.")
            else:
                print("Saldo insufficiente per effettuare il prelievo.")
        else:
            print("L'importo del prelievo deve essere positivo.")


if __name__ == "__main__":
    conto = ContoBancario("123456789", "Mario Rossi", 1000)  
    print(f"Saldo attuale: {conto.get_saldo()}") 

    conto.deposita(500)  
    print(f"Saldo attuale: {conto.get_saldo()}")  

    conto.preleva(200)  
    print(f"Saldo attuale: {conto.get_saldo()}")  

    conto.preleva(1500)  