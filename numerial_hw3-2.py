import numpy as np

# 已知數據點
x_vals = np.array([-0.440818, -0.270320, -0.106531, 0.051188])
f_vals = np.array([0.3, 0.4, 0.5, 0.6])

# 要估算的 x
x_target = 0

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

P = lagrange_interpolation(x_vals[:4], f_vals[:4], x_target) 

print(f" P(0) = {P:.7f}")
