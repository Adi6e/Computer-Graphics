from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.widgets import Button

figure = plt.figure()
figure.subplots_adjust(bottom=0.3)
figure.patch.set_facecolor('lightblue')
axis_obj = figure.add_subplot(111, projection='3d')

# array of prism vertexes
v = []
for i in range(10):
    v.append([np.cos(2 * np.pi * i / 10), np.sin(2 * np.pi * i / 10), 0])
    v.append([np.cos(2 * np.pi * i / 10), np.sin(2 * np.pi * i / 10), 2])

v = np.array(v)
# adding vertexes to plot
axis_obj.scatter3D(v[:, 0], v[:, 1], v[:, 2])

# sides of prism
edges = [[v[i % 20],
          v[(i + 1) % 20],
          v[(i + 3) % 20],
          v[(i + 2) % 20]] for i in range(0, 19, 2)]

edges.append([v[i] for i in range(0, 19, 2)])
edges.append([v[i] for i in range(1, 20, 2)])

# adding sides to plot
axis_obj.add_collection3d(Poly3DCollection(edges, alpha = 0.5, edgecolors = 'black'))

# making buttons
# isometric button

def isometric_button_function(param):
    axis_obj.view_init(35, 45)
    plt.draw()

isometric_axis = figure.add_axes([0.35, 0.23, 0.31, 0.06])
isometric_button = Button(isometric_axis, "Show isometric projection")
isometric_button.on_clicked(isometric_button_function)

# ortograpic top button
def ortographic_top_function(param):
    axis_obj.view_init(90)
    plt.draw()

ortographic_top_axis = figure.add_axes([0.15, 0.13, 0.31, 0.06])
ortographic_top_button = Button(ortographic_top_axis, "Show ortographic top")
ortographic_top_button.on_clicked(ortographic_top_function)

# ortographic front button
def button_callback_ortographic_front(event):
    axis_obj.view_init(0)
    plt.draw()

button_ax_ortographic_front = figure.add_axes([0.15, 0.03, 0.31, 0.06])
button_ortographic_front = Button(button_ax_ortographic_front, "Show ortographic front")
button_ortographic_front.on_clicked(button_callback_ortographic_front)

# show invisible lines button
def show_invisible_lines_function(event):
    axis_obj.add_collection3d(Poly3DCollection(edges, alpha=0.5, edgecolors='black'))
    plt.draw()

show_lines_axis = figure.add_axes([0.55, 0.13, 0.31, 0.06])
button_show_button = Button(show_lines_axis, "Show invisible lines")
button_show_button.on_clicked(show_invisible_lines_function)

# remove invisible lines button
def remove_lines_function(event):
    axis_obj.add_collection3d(Poly3DCollection(edges, alpha=1, edgecolors='black'))
    plt.draw()

remove_lines_axis = figure.add_axes([0.55, 0.03, 0.31, 0.06])
remove_button = Button(remove_lines_axis, "Remove invisible lines")
remove_button.on_clicked(remove_lines_function)

axis_obj.grid(None)
axis_obj.axis('off')
axis_obj.patch.set_facecolor("orange")
plt.show()
