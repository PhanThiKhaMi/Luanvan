import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-poster')
# Định nghĩa x và y
x = np.linspace(0, 1, 101)
y = 1 + x + x * np.random.random(len(x))
# Xây dựng ma trận A
A = np.vstack([x, np.ones(len(x))]).T
# Sử dụng`optimize.curve_fit` từ scipy
def func(x, a, b):
    y = a*x + b
    return y
theta= optimize.curve_fit(func, xdata = x, ydata = y)[0]
print(theta)
# Vẽ đồ thị kết quả
plt.figure(figsize = (10,8))
plt.plot(x, y, 'b.')
plt.plot(x, theta[0]*x + theta[1], 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
