import numpy as np
import matplotlib.pyplot as plt

# Malha representativa do plano dos complexos de -2 a 0.5 em x, e de -i a i em y
x = np.linspace(-2, 0.5, 100)
y = np.linspace(-1j, 1j, 100)
malha = np.meshgrid(x, y)
teste = malha[0]+malha[1]

numero = np.zeros(100)
for _ in range(100000):
    numero = (numero**2)+teste
    numero = (np.abs(numero)<2)*numero
    
a = numero!=0

plt.imshow(a, interpolation='none')
plt.show()