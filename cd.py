class CD:
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore
        self.brani = []

    def aggiungi_brano(self, brano):
        self.brani.append(brano)

    def durata_complessiva(self):
        return sum(b.durata for b in self.brani)

    def __str__(self):
        return f"CD: {self.titolo} di {self.autore}"