class Aviao:

    def __init__(self):
        self.avioes = []

    def vazio(self):
        return self.avioes == []

    def adcAviao(self, modelo, empresa, origem, destino, numPassageiros, numVoo):
        aviao = [modelo, empresa, origem, destino, numPassageiros, numVoo]
        self.avioes.append(aviao)

    def decolar(self):
       return self.avioes.pop(0)

    def tamanho(self):
        return len(self.avioes)