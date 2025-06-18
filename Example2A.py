"""
Example2A.py
Interactive version of linear adaptation visualization with iteration slider 
and matrix updates.

By Juan B. Gutiérrez, Professor of Mathematics
University of Texas at San Antonio.

License: Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider

np.random.seed(2025)

x = np.random.rand(10, 1)
y_desired = np.random.rand(10, 1)
n = len(x)
W = np.random.rand(n, n)
alpha = 0.01
num_iterations = 100

# Precompute all iterations for slider control
Ws = [W.copy()]
y_actuals = [W @ x]
errors = [np.mean((y_desired - Ws[-1] @ x) ** 2)]

for _ in range(num_iterations):
    y_actual = Ws[-1] @ x
    gradient_W = -2 * (y_desired - y_actual) @ x.T
    W_new = Ws[-1] - alpha * gradient_W
    Ws.append(W_new)
    y_actuals.append(W_new @ x)
    errors.append(np.mean((y_desired - W_new @ x) ** 2))

fig = plt.figure(figsize=(15, 6))
gs = fig.add_gridspec(2, 3, height_ratios=[15, 1])
ax0 = fig.add_subplot(gs[0, 0])
ax1 = fig.add_subplot(gs[0, 1])
ax2 = fig.add_subplot(gs[0, 2])
slider_ax = fig.add_subplot(gs[1, :])

ax0.set_title("Matrix and Vectors")
ax1.set_title("y_actual vs y_desired")
ax2.set_title("Error over Iterations")

matrix_display = ax0.imshow(Ws[0], aspect='auto', cmap='viridis', vmin=0, vmax=1)
x_display = ax0.imshow(x.reshape(-1, 1), extent=[-2, -1, 0, n], aspect='auto', cmap='gray', vmin=0, vmax=1)
y_display = ax0.imshow(y_actuals[0].reshape(-1, 1), extent=[n + 1, n + 2, 0, n], aspect='auto', cmap='Reds', vmin=0, vmax=1)

bars_actual = ax1.barh(range(n), y_actuals[0].flatten(), color='blue', label='y_actual')
bars_desired = ax1.barh(range(n), y_desired.flatten(), color='orange', alpha=0.5, label='y_desired')
ax1.set_xlim(0, 1)
ax1.set_ylim(-0.5, n - 0.5)
ax1.invert_yaxis()
ax1.legend()

error_line, = ax2.plot(range(num_iterations + 1), errors, 'r-')
current_iter_line = ax2.axvline(0, color='black', linestyle='--')
ax2.set_xlim(0, num_iterations)
ax2.set_ylim(0, 0.25)
ax2.set_xlabel("Iteration")
ax2.set_ylabel("Mean Squared Error")

slider = Slider(slider_ax, 'Iteration', 0, num_iterations, valinit=0, valstep=1)

def update(val):
    idx = int(slider.val)
    for i, bar in enumerate(bars_actual):
        bar.set_width(y_actuals[idx][i, 0])
    matrix_display.set_data(Ws[idx])
    y_display.set_data(y_actuals[idx].reshape(-1, 1))
    current_iter_line.set_xdata([idx, idx])
    fig.canvas.draw_idle()

slider.on_changed(update)
plt.tight_layout()
plt.show()
