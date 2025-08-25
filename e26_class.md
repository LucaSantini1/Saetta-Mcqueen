``` mermaid

classDiagram

	class Carburante {
		BENZINA
		DIESEL
	}

	class Veicolo {
		- marca : str
		- modello : str
		- carburante : Carburante
		+ get_info() str
	}

	class Flotta {
		- veicoli : list[Veicolo]
		+ aggiungi_veicolo(veicolo : Veicolo) bool
		+ get_veicoli() list[Veicolo]
		+ visualizza_veicoli() None
	}

	Veicolo "*" --> "1" Carburante : utilizza
	Veicolo <|-- Auto
	Veicolo <|-- Camion
	Flotta "1" --> "*" Veicolo : contiene

```