import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Paramètres de l'hélicoïde
radius = 1  # Rayon de l'hélice
height = 3  # Hauteur de l'hélice
turns = 5  # Nombre de tours de l'hélice

# Générer les points de l'hélicoïde
theta = np.linspace(0, 2 * np.pi * turns, 1000)
z = np.linspace(0, height, 1000)
r = np.linspace(0, radius, 1000)
theta, z = np.meshgrid(theta, z)
x = r * np.cos(theta)
y = r * np.sin(theta)

# Afficher l'hélicoïde en 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='inferno')

# Paramètres d'affichage
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Ajuster l'échelle des axes pour une meilleure visualisation
max_range = max(radius, height)
ax.set_xlim(-max_range, max_range)
ax.set_ylim(-max_range, max_range)
ax.set_zlim(0, height)

# Afficher le graphique
plt.show()
