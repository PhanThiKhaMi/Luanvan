import numpy as np
# Khai báo ma trận A và vector b
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [2, 4, 5]])
b = np.array([4, 6, 9, 2])
# Khai báo ma trận C và vector d
C = np.array([[1, 2, 3],
              [3, 5, 7]])
d = np.array([4, 9])
# Tính các thành phần
AT_A = 2 * A.T @ A
AT_b = 2 * A.T @ b
CT = C.T
# Tạo hệ phương trình  # Ax = b # Cx = d
# Kết hợp hai hệ phương trình
# | 2A^T A   C^T | | x | = | 2A^T b |
# | C          0  | | λ | = | d     |
# Kích thước
n = A.shape[1]  # số biến x
m = C.shape[0]  # số ràng buộc
# Tạo ma trận hệ phương trình
M = np.zeros((n + m, n + m))
M[:n, :n] = AT_A
M[:n, n:] = CT
M[n:, :n] = C
M[n:, n:] = np.zeros((m, m))
# Tạo vector phải
rhs = np.zeros(n + m)
rhs[:n] = AT_b
rhs[n:] = d
# Giải hệ phương trình
solution = np.linalg.solve(M, rhs)
# Phân tích nghiệm
x_optimal = solution[:n]
lambda_optimal = solution[n:]
print("Nghiệm tối ưu x:", x_optimal)
print("Giá trị nhân tử Lagrange λ:", lambda_optimal)
