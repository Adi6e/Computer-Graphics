import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox

# x = a * cos(t)
# y = b * sin(t)
# initial values

t = np.linspace(0, 2 * np.pi, 500)
a = 1
b = 2
x = a * np.cos(t)
y = b * np.sin(t)

fig = plt.figure()
fig.subplots_adjust(bottom=0.3)
fig.canvas.mpl_disconnect(fig.canvas.manager.key_press_handler_id)

ax = fig.add_subplot(111)
p, = ax.plot(x, y)
p.set_color("red")
plt.xlabel("x")
plt.ylabel("y")
ax.set_title("x=a*cos(t); y=b*sin(t)")
ax.grid(True)

def submit_a(val):
	x = int(val) * np.cos(t)
	p.set_xdata(x)
	ax.set_xlim(np.min(x) - 5, np.max(x) + 5)
	plt.draw()

axbox_a = fig.add_axes([0.7, 0.15, 0.2, 0.06])
text_box_a = TextBox(axbox_a, "a= ")
text_box_a.on_submit(submit_a)
text_box_a.set_val(a)

def submit_b(val):
	y = int(val) * np.sin(t)
	p.set_ydata(y)
	ax.set_ylim(np.min(y) - 5, np.max(y) + 5)
	plt.draw()

axbox_b = fig.add_axes([0.7, 0.05, 0.2, 0.06])
text_box_b = TextBox(axbox_b, "b= ")
text_box_b.on_submit(submit_b)
text_box_b.set_val(b)

plt.show()