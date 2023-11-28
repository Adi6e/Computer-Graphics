import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import LightSource
from matplotlib import cm

a = 10
c = 20

print('Введите параметр аппроксимации: ')
approximation = int(input())
u = np.linspace(0, 1, approximation)
t = np.linspace(0, 2 * np.pi, approximation)

tt, uu = np.meshgrid(t, u)
x = a * np.sinh(uu) * np.cos(tt)
y = a * np.sinh(uu) * np.sin(tt)
z = c * np.cosh(uu)

ls = LightSource(azdeg=360, altdeg=0)
rgb = ls.shade(x, cmap=cm.Blues, vert_exag=0.1, blend_mode='soft')
 
 
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, facecolors=rgb, color='red')
ax.grid(None)
ax.axis('off')
 
plt.show()
