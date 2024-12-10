import numpy as np
from scipy import optimize
# Định nghĩa ma trận A và vector b
A = np.array([[-2, 0], [1, 2], [0, 1]])
b = np.array([-2, -1, 1])
# Tính A^T A và A^T b
ATA = A.T @ A
ATb = A.T @ b
# Giải phương trình để tìm nghiệm bình phương tối thiểu x̂
x_hat = np.linalg.solve(ATA, ATb)
# Tính giá trị nhỏ nhất của ‖Ax̂ - b‖^2
residual_norm_squared = np.linalg.norm(A @ x_hat - b) ** 2
# In kết quả
print("Nghiệm bình phương tối thiểu x̂:", x_hat)
print("Giá trị nhỏ nhất của ‖Ax̂ - b‖^2:", residual_norm_squared)