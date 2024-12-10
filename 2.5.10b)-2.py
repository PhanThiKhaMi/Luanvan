import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-poster')
# Định nghĩa x và y
x = np.linspace(0, 1, 101)
y = 1 + x + x * np.random.random(len(x))
# Xây dụng ma trận A
A = np.vstack([x, np.ones(len(x))]).T
# Chuyển y thành vector cột
y = y[:, np.newaxis]
# Gọi hàm tích hợp sẵn trong NumPy
theta = np.linalg.lstsq(A, y, rcond=None)[0]
print(theta)
# Vẽ đồ thị kêt quả
plt.figure(figsize = (10,8))
plt.plot(x, y, 'b.')
plt.plot(x, theta[0]*x + theta[1], 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
