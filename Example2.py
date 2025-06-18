import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

np.random.seed(2025)

# Initialize parameters
x = np.random.rand(10, 1)
y_desired = np.random.rand(10, 1)
n = len(x)
W = 0.1 * np.ones((n, n))
alpha = 0.01
num_iterations = 100

# Set up figure and axes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
plt.subplots_adjust(wspace=0.4)

# Titles and formatting
ax1.set_title("y_actual vs y_desired")
ax2.set_title("Error over Iterations")

# Initialize bar plots for y_actual and y_desired
bars_actual = ax1.barh(range(n), np.zeros(n), color='blue', label='y_actual')
bars_desired = ax1.barh(range(n), y_desired.flatten(), color='orange', alpha=0.5, label='y_desired')
ax1.set_xlim(0, 1)
ax1.set_ylim(-0.5, n - 0.5)
ax1.invert_yaxis()
ax1.legend()

# Initialize error plot
error_values = []
error_line, = ax2.plot([], [], 'r-')
ax2.set_xlim(0, num_iterations)
ax2.set_ylim(0, 0.25)
ax2.set_xlabel("Iteration")
ax2.set_ylabel("Mean Squared Error")

# Animation update function
def update(frame):
    global W
    y_actual = W @ x
    error = np.mean((y_desired - y_actual) ** 2)
    error_values.append(error)

    gradient_W = -2 * (y_desired - y_actual) @ x.T
    W = W - alpha * gradient_W

    for i, bar in enumerate(bars_actual):
        bar.set_width(y_actual[i, 0])
    error_line.set_data(range(len(error_values)), error_values)
    return [*bars_actual, error_line]

ani = animation.FuncAnimation(fig, update, frames=num_iterations, blit=True, interval=100)
plt.show()
