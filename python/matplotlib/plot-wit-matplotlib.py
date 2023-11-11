import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = np.sin(x)

plt.plot(x, y)
plt.title('sin(x) Function')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)
plt.show()

