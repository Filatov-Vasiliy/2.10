import math
def chebishev(x, T, i):
    if i == 1:
        return T
    return chebishev(x, T + [2 * x * T[-1] - T[-2]], i - 1)


n = 3
x = 10
a = 1
b = 10
T = []
print(chebishev(x, [1, x], n))
for i in range(n):
    T.append(1/2*(a+b)+1/2*(b-a)*math.cos(2*i-1/2*n*math.pi))
print(T)