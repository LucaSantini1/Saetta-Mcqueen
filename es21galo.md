classDiagram
    class Camera {
        int numero
        string tipo
        bool disponibilita
    }
    class Albergo {
        string nome
        +aggiungiCamera()
        +prenotaCamera()
        +visualizzaCamereDisponibili()
        +visualizzaPrenotazioni()
    }
    Albergo "1" -- "*" Camera : gestisce
