# Imports
import numpy as np
import matplotlib.pyplot as plt

# Mandelbrot plot function
def Mandelbrot(den, rng):
    den, rng = int(den), int(rng)
    
    # Complex plane mesh array
    x = np.linspace(-2, 0.5, den)
    y = np.linspace(-1j, 1j, den)
    mesh = np.meshgrid(x, y)
    mesh = mesh[0]+mesh[1]

    # Mandelbrot check (?)
    nums = np.zeros(den)
    for _ in range(rng):
        nums = (nums**2)+mesh
        nums = (np.abs(nums)<2)*nums

    # Graph plot
    abs = np.abs(nums)

    plt.imshow(abs, interpolation='none')
    plt.savefig(f'./figs/den1e{int(np.log10(den))}_rng1e{int(np.log10(rng))}.png')
    plt.show()
    
# Parameters
den = 1e3
rng = 1e3

Mandelbrot(den, rng)