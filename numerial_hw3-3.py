import numpy as np
import math

def hermite_interpolation(t_vals, d_vals, v_vals, t_target):
    n = len(t_vals)
    z = np.repeat(t_vals, 2)  # 生成節點的重複列表 (Hermite 需要雙重)
    f = np.zeros(2 * n)       # 儲存函數值
    
    # 填充 f(x) 值
    f[0::2] = d_vals
    f[1::2] = d_vals

    # 構造 Newton 差分表
    divided_diff = np.zeros((2 * n, 2 * n))
    divided_diff[:, 0] = f

    for i in range(1, 2 * n):
        for j in range(2 * n - i):
            if z[j] == z[j + i]:  # 重複節點，使用導數
                if i == 1:
                    divided_diff[j, i] = v_vals[j // 2]  # 直接使用對應的導數
                else:
                    divided_diff[j, i] = (divided_diff[j + 1, i - 1] - divided_diff[j, i - 1]) / math.factorial(i)
            else:
                divided_diff[j, i] = (divided_diff[j + 1, i - 1] - divided_diff[j, i - 1]) / (z[j + i] - z[j])

    # 計算 Hermite 插值多項式的值
    result = divided_diff[0, 0]
    product_term = 1
    for i in range(1, 2 * n):
        product_term *= (t_target - z[i - 1])
        result += divided_diff[0, i] * product_term

    return result


def check_speed_limit(speed):
    mph_speed = speed * 0.681818  # 1 ft/s = 0.681818 mph
    return mph_speed >= 55

def find_first_exceed_time(t_vals, v_vals):
    for t in np.linspace(min(t_vals), max(t_vals), 1000):
        speed = hermite_interpolation(t_vals, v_vals, np.zeros_like(v_vals), t)
        if check_speed_limit(speed):
            return t 
    return None

def find_max_speed(t_vals, v_vals):
    t_range = np.linspace(min(t_vals), max(t_vals), 1000)
    speeds = [hermite_interpolation(t_vals, v_vals, np.zeros_like(v_vals), t) for t in t_range]
    return max(speeds)

t_vals = np.array([3, 5, 8, 13])
d_vals = np.array([200, 375, 620, 990])
v_vals = np.array([77, 80, 74, 72])

t_target = 10
position_at_10s = hermite_interpolation(t_vals, d_vals, v_vals, t_target)
speed_at_10s = hermite_interpolation(t_vals, v_vals, np.zeros_like(v_vals), t_target)

first_exceed_time = find_first_exceed_time(t_vals, v_vals)
max_speed = find_max_speed(t_vals, v_vals)

is_over_limit = check_speed_limit(max_speed)
print(f"t = 10 ， D(10) = {position_at_10s:.2f} ")
print(f"t = 10 ， V(10) = {speed_at_10s:.2f} ")
print(f"是否超過 55 mph : {'是' if is_over_limit else '否'}")
if first_exceed_time:
    print(f"第一次超過 55 mph 的時間點: t ≈ {first_exceed_time:.2f} 秒")
else:
    print("沒超速")
print(f"最大速度: {max_speed:.2f} ft/s")
