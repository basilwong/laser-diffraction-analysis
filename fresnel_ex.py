import numpy as np
from scipy.special import fresnel
import matplotlib.pyplot as plt

t = np.linspace(0, 5.0, 201)
ss, cc = fresnel(t / np.sqrt(np.pi / 2))
scaled_ss = np.sqrt(np.pi / 2) * ss
scaled_cc = np.sqrt(np.pi / 2) * cc
i = ss ** 2 + cc ** 2
# plt.plot(t, scaled_cc, 'g--', t, scaled_ss, 'r-', linewidth=2)
plt.plot(t,i)
plt.grid(True)
plt.show()
