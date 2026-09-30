class CasaDiscografica: 
    def __init__(self, nome: str, anno_fondazione: int): 
        self.nome = nome 
        self.anno_fondazione = anno_fondazione 
    def __str__(self): 
        return f"Etichetta: {self.nome} (fondata nel {self.anno_fondazione})" 