class Artista:
    def __init__(self, nome: str, nazionalita: str):
        self.nome = nome
        self.nazionalita = nazionalita

    def __str__(self):
        return f"{self.nome} ({self.nazionalita})"