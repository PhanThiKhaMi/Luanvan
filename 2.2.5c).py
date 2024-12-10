import numpy as np
from scipy import optimize
# Định nghĩa ma trận A và vector b
A = np.array([[-2, 0], [1, 2], [0, 1]])
b = np.array([-2, -1, 1])
# Thực hiện phân tích QR của ma trận A
Q, R = np.linalg.qr(A)
# Giải nghiệm bình phương tối thiểu x̂ bằng R^(-1) Q^T b
x_hat_qr = np.linalg.inv(R) @ Q.T @ b
# Tính giá trị nhỏ nhất của ‖Ax̂ - b‖^2
residual_norm_squared_qr = np.linalg.norm(A @ x_hat_qr - b) ** 2
# In kết quả
print("Nghiệm bình phương tối thiểu x̂:", x_hat_qr)
print("Giá trị nhỏ nhất của ‖Ax̂ - b‖^2:", residual_norm_squared_qr)
print("Ma trận trực giao Q trong phân tích QR của ma trận A là:", Q)
print("Ma trận bậc thang R trong phân tích QR của ma trận A là:", R)
