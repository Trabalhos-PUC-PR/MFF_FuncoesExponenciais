import matplotlib.pyplot as plt
import numpy as np

deltaNumero = np.arange(-200, 200, 0.1)
raio = 1

cos = raio * np.cos(deltaNumero)
sen = raio * np.sin(deltaNumero)

plt.grid(color='lightgray', linestyle='-.', linewidth=0.1) #é basicamente uma copia do grid que ta na outra atividade

plt.plot(cos, sen)
# mostar o gráfico
plt.show()
