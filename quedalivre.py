import numpy as np
import matplotlib.pyplot as plt

class Particula:
    def __init__(self, v0, g, k_p, n=20, cd = 16):
        self.velocidadeInicial = v0
        self.aceleracao = g
        self.coeficientePerda = k_p
        self.perdaVelocidade = np.multiply(self.coeficientePerda, self.velocidadeInicial)
        self.quiques = np.divide(1, self.coeficientePerda)
        self.n = n
        self.casasDecimais = cd
        self.dt = round(np.divide(np.multiply(2, self.velocidadeInicial), np.multiply(self.n, self.aceleracao)), self.casasDecimais)

    def tempo(self):
        self.t = np.array([])
        dti = self.dt
        v0 = self.velocidadeInicial
        for i in np.arange(self.quiques):
            y = np.arange(0, np.divide(np.multiply(2, v0), self.aceleracao), dti)
            self.t = np.append(self.t, y)
            v0 -= self.perdaVelocidade
            dti = round(np.divide(np.multiply(2,v0), np.multiply(self.n, self.aceleracao)), self.casasDecimais)

    def velocidade(self):
        self.v = np.array([])
        v0 = self.velocidadeInicial
        dti = self.dt
        for i in np.arange(self.quiques):
            w = np.multiply(np.ones(self.n), v0)
            self.v = np.append(self.v, w)
            v0 -= self.perdaVelocidade

    def posicao(self):
        try:
            self.pos = np.multiply(self.t, self.v) - np.multiply(np.divide(self.aceleracao, 2), np.power(self.t, 2))
        except:
            bmais = len(self.t) - len(self.v)
            self.t = np.delete(self.t, np.s_[:bmais])
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
            dti = round(np.divide(tempoqueda,self.n), self.casasDecimais)
            m = np.arange(t0, a, dti)
            t0 = a
            self.cronometro = np.append(self.cronometro, m)

    def executando_grafico(self):
        fig, self.ax = plt.subplots()
        try:
            self.grafico()
        except:
            amais = len(self.cronometro) - len(self.pos)
            self.cronometro = np.delete(self.cronometro, np.s_[:amais])
            self.grafico()
        plt.savefig('Lançamento Vertical.png')
        plt.show()

    def grafico(self):
        self.ax.scatter(self.cronometro, self.pos, s=1, c='r')
        self.ax.set_title('Partícula quicando')
        self.ax.set_xlabel("cronômetro (s)")
        self.ax.set_ylabel("posição (m)")
        self.ax.grid(True)