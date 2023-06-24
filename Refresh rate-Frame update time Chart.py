import matplotlib.pyplot as plt
import numpy as np

def inverse_proportion(x, k):
    return k / x

k = 1000
x = np.linspace(1, 180, 100)
y = inverse_proportion(x, k)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Refresh rate-Frame update time Chart')
plt.xlabel('Refresh rate (Hz)')
plt.ylabel('Frame update time (ms)')
plt.plot(x, y, color='k')  # 等同于 plt.plot(x, y, 'k')
plt.show()