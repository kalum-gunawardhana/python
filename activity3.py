import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 400)
y = x**2

plt.figure()
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("f(x) = x^2")
plt.title("Plot of f(x) = x^2")
plt.grid(True)

plt.show()
