import numpy as np

# 已知數據點
x_vals = np.array([0.698, 0.733, 0.768, 0.803])
f_vals = np.array([0.7661, 0.7432, 0.7193, 0.6946])

# 要估算的 x
x_target = 0.750

# 拉格朗日插值函數
def lagrange_interpolation(x_vals, f_vals, x_target):
    n = len(x_vals)
    P_x = 0

    for i in range(n):
        L_i = 1
        for j in range(n):
            if i != j:
                L_i *= (x_target - x_vals[j]) / (x_vals[i] - x_vals[j])
        P_x += f_vals[i] * L_i
    
    return P_x

# 計算不同次數的拉格朗日插值結果
P1 = lagrange_interpolation(x_vals[:2], f_vals[:2], x_target)  # 一次插值
P2 = lagrange_interpolation(x_vals[:3], f_vals[:3], x_target)  # 二次插值
P3 = lagrange_interpolation(x_vals[:4], f_vals[:4], x_target)  # 三次插值

# 真實值（使用 numpy 計算 cos(0.750)）
true_value = np.cos(0.750)

# 計算誤差
error_P1 = abs(true_value - P1)
error_P2 = abs(true_value - P2)
error_P3 = abs(true_value - P3)

# 輸出結果
print(f"真實值: cos(0.750) = {true_value:.7f}")
print(f"一次插值 P1(0.750) = {P1:.7f}, 誤差 = {error_P1:.7f}")
print(f"二次插值 P2(0.750) = {P2:.7f}, 誤差 = {error_P2:.7f}")
print(f"三次插值 P3(0.750) = {P3:.7f}, 誤差 = {error_P3:.7f}")
