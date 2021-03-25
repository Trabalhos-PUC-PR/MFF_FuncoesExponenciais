import matplotlib.pyplot as plt
import numpy as np

deltaNumero = np.arange(-200, 200, 0.1) #serve pra pegar o seno de todos os numeros entre -200 e 200 (incluindo os com uma casa decimal)
raio = 1 #o raio é de um

cos = raio * np.cos(deltaNumero) #isso calcula o cosseno
sen = raio * np.sin(deltaNumero) #e isso calcula o seno

plt.grid(color='lightgray', linestyle='-.', linewidth=0.1) #é basicamente uma copia do grid que ta na outra atividade

plt.plot(cos, sen) #DESENHA O CIRCULO
# mostar o gráfico
plt.show() #mostra o circulo
