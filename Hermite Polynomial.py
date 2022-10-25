import sympy as sp
import numpy as np

sum1 = 0
sum2 = 0

x = np.array([2.0, 2.5, 3.0])
y = np.array([0.69315, 0.91629, 1.09861])
dy = np.array([0.5, 0.4000, 0.33333])

x_s = sp.Symbol('x')

for i in range(0, len(x)):
    l = 1
    for j in range(0, len(x)):
        if i != j:
            l *= (x_s - x[j])/(x[i] - x[j])

    dl = sp.diff(l, x_s).subs(x_s, x[i])

    sum1 += (1 - 2 * (x_s - x[i]) * dl) * y[i] * (l ** 2)
    sum2 += (x_s - x[i]) * dy[i] * (l ** 2)

H = sum1 + sum2
H = sp.simplify(H)
print(H)
print(H.subs(x_s, 2.7))
