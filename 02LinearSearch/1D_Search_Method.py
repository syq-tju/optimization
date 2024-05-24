import matplotlib.pyplot as plt
import numpy as np

# Define the function and the interval
def f(x):
    return x**2 - 4*x + 4

x = np.linspace(-1, 5, 400)
y = f(x)

# Plot the function
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='f(x) = $x^2 - 4x + 4$')
plt.scatter([0, 2, 4], [f(0), f(2), f(4)], color='red')  # Example points of search
plt.text(0, f(0)+0.5, 'x=0', fontsize=9, ha='center')
plt.text(2, f(2)-1, 'x=2 (min)', fontsize=9, ha='center')
plt.text(4, f(4)+0.5, 'x=4', fontsize=9, ha='center')
plt.title('1D Search Visualization on $f(x) = x^2 - 4x + 4$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)

# Save the plot
image_path = '1d_search_visualization.png'
plt.savefig(image_path)
plt.close()

image_path
