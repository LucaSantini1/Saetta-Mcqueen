from datetime import datetime
from typing import List

class Utente:
    def __init__(self, nome_utente: str, email: str, password: str, immagine_profilo: str = "", biografia: str = ""):
        self.nome_utente = nome_utente
        self.email = email
        self.password = password
        self.immagine_profilo = immagine_profilo
        self.biografia = biografia
        self.foto = []
        self.album = []

    def carica_foto(self, titolo: str, descrizione: str, album=None):
        nuova_foto = Foto(titolo, descrizione, self, album)
        self.foto.append(nuova_foto)
        if album:
            album.aggiungi_foto(nuova_foto)
        return nuova_foto

    def crea_album(self, titolo: str, descrizione: str):
        nuovo_album = Album(titolo, descrizione, self)
        self.album.append(nuovo_album)
        return nuovo_album

class Foto:
    _id_counter = 1

    def __init__(self, titolo: str, descrizione: str, utente: Utente, album=None):
        self.id = Foto._id_counter
        Foto._id_counter += 1
        self.titolo = titolo
        self.descrizione = descrizione
        self.data_caricamento = datetime.now()
        self.utente = utente
        self.album = album
        self.commenti = []

    def aggiungi_commento(self, utente: Utente, testo: str):
        nuovo_commento = Commento(utente, self, testo)
        self.commenti.append(nuovo_commento)
        return nuovo_commento

class Album:
    def __init__(self, titolo: str, descrizione: str, utente: Utente):
        self.titolo = titolo
        self.descrizione = descrizione
        self.utente = utente
        self.foto = []

    def aggiungi_foto(self, foto: Foto):
        self.foto.append(foto)

class Commento:
    def __init__(self, utente: Utente, foto: Foto, testo: str):
        self.utente = utente
        self.foto = foto
        self.testo = testo
        self.data_commento = datetime.now()