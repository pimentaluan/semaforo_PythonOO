import time
class Temporizador:
    def __init__(self):
        self.ligado = False
        self.contador = 0

    def ligar(self):
        self.ligado = True
    
    def desligar(self):
        self.ligado = False

    def contar(self):
        while self.contador > 0:
            self.contador -= 1

    def exibir(self, registrador: int):
        self.contador = registrador
        print(f'Timer defenido para {self.contador}')
        for i in range (self.contador):
            time.sleep(1)
            self.contador -= 1
            print(self.contador)

class Lampada:
    def __init__(self, cor):
        self.ligada = False
        self.cor = cor

    def ligar(self):
        self.ligada = True
        print(f"A luz {self.cor} foi ligada.")
    
    def desligar(self):
        self.ligada = False
        print(f"A luz {self.cor} foi desligada.")
    
class Semaforo:
    def __init__(self):
        self.temporizador = Temporizador()
        self.lampada_vermelha = Lampada("Vermelho")
        self.lampada_amarela = Lampada("Amarelo")
        self.lampada_verde = Lampada("Verde")

        self.lampada_verde.ligar()
        self.temporizador.exibir(10)
        
    def proximo_estado(self):
        if self.lampada_verde.ligada:
            self.lampada_verde.desligar()
            self.lampada_amarela.ligar()
            self.temporizador.exibir(2)

        elif self.lampada_amarela.ligada:
            self.lampada_amarela.desligar()
            self.lampada_vermelha.ligar()
            self.temporizador.exibir(5)
        
        else:
            self.lampada_vermelha.desligar()
            self.lampada_verde.ligar()
            self.temporizador.exibir(10)

    def __str__(self):
        return f'Meu semáforo foi ligado'


if __name__ == "__main__":
    semaforo1 = Semaforo()
    for i in range(11):
        semaforo1.proximo_estado()
