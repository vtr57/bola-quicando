import numpy as np
import matplotlib.pyplot as plt

class Particula:
    def __init__(self, v0, g, k_p, n=20):
        self.velocidadeInicial = v0
        self.aceleracao = g
        self.coeficientePerda = k_p
        self.perdaVelocidade = np.multiply(self.coeficientePerda, self.velocidadeInicial)
        self.quiques = np.divide(1, self.coeficientePerda)
        self.n = n
        self.dt = np.divide(np.multiply(2, self.velocidadeInicial), np.multiply(self.n, self.aceleracao))

    def tempo(self):
        self.t = np.array([])
        dti = self.dt
        v0 = self.velocidadeInicial
        for i in np.arange(self.quiques):
            y = np.arange(0, np.divide(np.multiply(2, v0), self.aceleracao), dti)
            self.t = np.append(self.t, y)
            v0 -= self.perdaVelocidade
            dti = np.divide(np.multiply(2,v0), np.multiply(self.n, self.aceleracao))

    def velocidade(self):
        self.v = np.array([])
        v0 = self.velocidadeInicial
        dti = self.dt
        for i in np.arange(self.quiques):
            w = np.multiply(np.ones(self.n), v0)
            self.v = np.append(self.v, w)
            v0 -= self.perdaVelocidade

    def posicao(self):
        self.pos = np.multiply(self.t, self.v) - np.multiply(np.divide(self.aceleracao, 2), np.power(self.t, 2))
        
    def cronometro(self):
        a = 0
        v0 = self.velocidadeInicial
        t0 = 0
        self.cronometro = np.array([])
        for i in np.arange(self.quiques):
            tempoqueda = np.divide(np.multiply(2, v0), self.aceleracao)
            a += tempoqueda
            v0 -= self.perdaVelocidade
            dti = np.divide(tempoqueda,self.n)
            m = np.arange(t0, a, dti)
            t0 = a
            self.cronometro = np.append(self.cronometro, m)

    def grafico(self):
        fig, ax = plt.subplots()
        ax.plot(self.cronometro, self.pos)
        # plt.savefig('Lançamento Vertical.png')
        plt.show()

