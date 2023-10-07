# ---------------------------------------------------------------------------- #
#                                     SETUP                                    #
# ---------------------------------------------------------------------------- #

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


# ---------------------------------------------------------------------------- #
#                                  PARAMETERS                                  #
# ---------------------------------------------------------------------------- #

quality = int(1e3) # Related to pixel density, image quality and size
iterations = int(1e3) # Related to precision, number of iterations


# ---------------------------------------------------------------------------- #
#                                   FUNCTIONS                                  #
# ---------------------------------------------------------------------------- #

def cmapByPower(array, exponent:float, c1:float, c2:float):
    '''
    Create a colormap based on the input array and a power-law transformation.
    
    The function takes an input array of distance values and applies a power-law
    transformation with the given exponent. It then maps these transformed values to
    colors in the HSV color space, where the hue and saturation components are
    scaled by the provided constants c1 and c2. The resulting colormap is returned
    as a ListedColormap object.

    Args:
        array (numpy.ndarray): Array with the distance values to be transformed
         into colors.
        exponent (float): Exponent for the power-law transformation.
        c1 (float): Scaling constant for the hue component.
        c2 (float): Scaling constant for the saturation component.

    Returns:
        matplotlib.colors.ListedColormap: A ListedColormap object representing the
            colormap generated based on the power-law transformed values.
    '''
    sorted = np.sort(array.ravel())
    colors = []
    
    for dist in sorted:
        power = dist**exponent
        hsv = (1+c1*power, 1-c2*power, 0.9)
        colors.append(hsv)
        
    colormap = ListedColormap(colors)
    
    return colormap


def Mandelbrot(quality:int, iterations:int, ver='A'):
    '''
    Plot the Mandelbrot set using specified parameters.
    
    The function generates a plot of the Mandelbrot set based on the specified
    parameters. It creates a complex plane mesh and iterates over it to
    determine set membership and finally plots it using one of three methods
    available ('A', 'B' or 'C').
    
    Args:
        quality (int): Array size, equivalent to the graph's pixel density.
        iterations (int): Number of iterations to determine set membership.
        ver (str, optional): Which version of the Mandelbrot check/coloring
         method to use; either 'A', 'B' or 'C'. Defaults to 'A'.

    Raises:
        ValueError: If an invalid value is provided for the 'ver' parameter.
    '''
    VALID_VERS = {'A', # Regular version: applies mask before plotting
                  'B', # Applies mask during iterations, but not before plotting
                  'C'} # Regular version, but coloring according to power-law
    
    # Complex plane mesh array
    x = np.linspace(-2, 0.5, quality)
    y = np.linspace(-1j, 1j, quality)
    mesh = np.meshgrid(x, y)
    mesh = mesh[0]+mesh[1]

    # Mandelbrot check
    nums = np.zeros(quality)
    
    # (Version A and C)
    if ver in ['A', 'C']:
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
            
    # Raise error
    else: raise ValueError(f'Invalid value for \'ver\': Valid values are \
{VALID_VERS}. \'{ver}\' was provided.')

    # Graph plot
    abs = np.abs(nums)

    cmap = cmapByPower(abs, 0.2, 0.6, 0.4) if (ver == 'C') else 'viridis'
    plt.imshow(abs, interpolation='none', aspect='auto', cmap=cmap)
    plt.axis('off')
    plt.tight_layout()

    plt.savefig(f'./figs/v2{ver}-qual{int(quality)}_iter{int(iterations)}.png')
    plt.show()


# ---------------------------------------------------------------------------- #
#                                    SCRIPT                                    #
# ---------------------------------------------------------------------------- #

Mandelbrot(quality, iterations)


# ----------------------------------- TO DO ---------------------------------- #
# v3 - parallel computing :(