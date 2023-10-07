# ---------------------------------------------------------------------------- #
#                                     SETUP                                    #
# ---------------------------------------------------------------------------- #

import numpy as np
import matplotlib.pyplot as plt


# ---------------------------------------------------------------------------- #
#                                  PARAMETERS                                  #
# ---------------------------------------------------------------------------- #

quality = 1e3 # Related to pixel density, image quality and size
iterations = 1e3 # Related to precision, number of iterations


# ---------------------------------------------------------------------------- #
#                                   FUNCTIONS                                  #
# ---------------------------------------------------------------------------- #

# Mandelbrot plot function :)
def Mandelbrot(quality, iterations, ver='A'):
    quality, iterations = int(quality), int(iterations)
    
    # Complex plane mesh array
    x = np.linspace(-2, 0.5, quality)
    y = np.linspace(-1j, 1j, quality)
    mesh = np.meshgrid(x, y)
    mesh = mesh[0]+mesh[1]

    # Mandelbrot check
    nums = np.zeros(quality)
    
    # (Version A)
    if ver == 'A':
        for current in range(iterations):
            nums = (nums**2)+mesh
            nums = (np.abs(nums)<2)*nums
            
            # Anxiety reliever :)
            print(f'\nProcessing: {round(current/iterations*100, 2)}% done.')
    
    # (Version B)
    elif ver == 'B':
        for current in range(iterations):
            nums = (((np.abs(nums)<2)*nums)**2)+mesh
            
            # Anxiety reliever :)
            print(f'\nProcessing: {round(current/iterations*100, 2)}% done.')
            
    else: print(f'Version {ver} not found.')

    # Graph plot
    abs = np.abs(nums)

    plt.imshow(abs, interpolation='none', aspect='auto')
    plt.xticks([])
    plt.yticks([])

    plt.savefig(f'./figs/v2{ver}-qual{int(quality)}_iter{int(iterations)}.png')
    plt.show()


# ---------------------------------------------------------------------------- #
#                                    SCRIPT                                    #
# ---------------------------------------------------------------------------- #

Mandelbrot(quality, iterations)


# ----------------------------------- TO DO ---------------------------------- #
# coloring