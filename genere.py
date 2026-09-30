class Genere:
    def __init__(self, nome: str, descrizione: str):
        self.nome = nome
        self.descrizione = descrizione

    def __str__(self):
        return f"Genere: {self.nome}"