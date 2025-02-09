import matplotlib.pyplot as plt
import numpy as np

a = np.random.normal(0, 1, 1000)


plt.hist(a, bins=10)
plt.xlabel("x ось")
plt.ylabel("y ось")
plt.title("Тестовая гистограма")
plt.show()

