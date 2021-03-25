# Importando as bibliotecas necessárias
import matplotlib.pyplot as plt
import numpy as np

# definindo um vetor com todos os pontos que usaremos no gráfico
#x = np.array([np.NINF, np.inf]) #aqui eu mudei manualmente pra ver o que acontecia se o array tivesse 2 pontos infinitos (não deu certo!)

# Podemos usar a função np.arange para 
# criar um gráfico com mais pontos
# o uso desta função pode ser visto em: https://realpython.com/how-to-use-numpy-arange/#
x = np.arange(-3, 4, 0.1) # argumentos do método arange -  esse eu não sei qual o limite

# Definindo nossa função. Atribuimos a y o resultado da aplicação da função
# a cada valor do array x 
y = np.e**x
w = 5 * np.e**(1-x) -4

#define a grade que vamos usar no plot disponível em https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html
plt.grid(color='lightgray', linestyle='-.', linewidth=0.1) #este método recebe três argumentos
# Cria o gráfico
plt.plot(x, y, 'r')
plt.plot(x, w, 'b')
# mostar o gráfico
plt.show()


