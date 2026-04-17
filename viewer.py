import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import numpy as np

from reader import dataset_reader

def plot_Ea(X,Y,Z):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    im1 = ax1.pcolormesh(X, Y, Z, shading='gouraud', cmap="plasma",)
    fig.colorbar(im1, ax=ax1)
    ax1.set_aspect('equal')
    ax1.set_title('Ea')
    im2 = ax2.pcolormesh(X, Y, Z, norm=LogNorm(vmin=Ea.min(), vmax=Ea.max()), shading='gouraud', cmap="plasma",)
    fig.colorbar(im2, ax=ax2)
    ax2.set_aspect('equal')
    ax2.set_title('Ea (LogNorm)')
    fig.savefig('double_disk.png')  
    plt.show()

def plot_complex_split(X, Y, Z, title="Z"):
    """plot two graph: magnitude and phase."""
    # Magnitude 
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    amp = np.abs(Z)
    im1 = ax1.pcolormesh(X, Y, amp, cmap='magma', shading='gouraud')
    fig.colorbar(im1, ax=ax1, label='Magnitude')
    ax1.set_aspect('equal')
    ax1.set_title(f'Magnitude |{title}|')

    # phase (arg)
    phase = np.angle(Z) # Значения от -pi до pi
    im2 = ax2.pcolormesh(X, Y, phase, cmap='twilight', shading='gouraud')
    fig.colorbar(im2, ax=ax2, label='Phase (radians)')
    ax2.set_aspect('equal')
    ax2.set_title(f'Phase arg({title})')

    plt.show()

def plot_complex_domain(X, Y, Z):
    """Рисует поле методом Domain Coloring."""
    # код с hsv_to_rgb...

file_path = 'data/results.h5'
                                # Имя 2D массива внутри HDF5-файла
nphi = "-012"
X =  dataset_reader(file_path, f'/nphi{nphi}/grid_2d/X')
Y =  dataset_reader(file_path, f'/nphi{nphi}/grid_2d/Y')
Ea = dataset_reader(file_path, f'/nphi{nphi}/field_2d/Ea')

plot_Ea(X,Y,Ea)

Ex = dataset_reader(file_path, f'/nphi{nphi}/field_2d/Ex')
plot_complex_split(X, Y, Ex, "Ex")

Ey = dataset_reader(file_path, f'/nphi{nphi}/field_2d/Ey')
plot_complex_split(X, Y, Ey, "Ey")

Ez = dataset_reader(file_path, f'/nphi{nphi}/field_2d/Ez')
plot_complex_split(X, Y, Ey, "Ez")