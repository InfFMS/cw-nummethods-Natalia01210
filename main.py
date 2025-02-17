import matplotlib.pyplot as plt
import numpy as np

T = 133.15
R = 8.314
a =  0.1382
b =  3.19 * 10**-5
V = np.linspace(b + 10 ** -5, 10 ** -3, 1000)
P =  (R * T) / (V - b) - a / V**2
fig = plt.figure(figsize=(14, 6))
ax = plt.subplot(2, 3, 1)
plt.plot(V, P)
plt.title("T = " + str(T) + "K")

T = 143.15
R = 8.314
a =  0.1382
b =  3.19 * 10**-5
P =  (R * T) / (V - b) - a / V**2
ax = plt.subplot(2, 3, 2)
plt.plot(V, P)
plt.title("T = " + str(T) + "K")

T = 153.15
R = 8.314
a =  0.1382
b =  3.19 * 10**-5
P =  (R * T) / (V - b) - a / V**2
ax = plt.subplot(2, 3, 3)
plt.plot(V, P)
plt.title("T = " + str(T) + "K")

T = 163.15
R = 8.314
a =  0.1382
b =  3.19 * 10**-5
P =  (R * T) / (V - b) - a / V**2
ax = plt.subplot(2, 3, 4)
plt.plot(V, P, color="red")
plt.title("T = " + str(T) + "K")

T = 173.15
R = 8.314
a =  0.1382
b =  3.19 * 10**-5
P =  (R * T) / (V - b) - a / V**2
ax = plt.subplot(2, 3, 5)
plt.plot(V, P)
plt.title("T = " + str(T) + "K")

plt.tight_layout()


fig = plt.figure(figsize=(14, 6))
ax = plt.subplot(1, 1, 1)
T = 143.15
R = 8.314
a =  0.1382
b =  3.19 * 10**-5
V = np.linspace(b + 10 ** -5, 10 ** -3, 1000)
P =  (R * T) / (V - b) - a / V**2
plt.plot(V, P)
plt.title("T = " + str(T) + "K")
r, l1 = 9.4 * 10 ** -5, 6 * 10 ** -5
while(abs(r - l1) > 10 ** -8):
        i = l1 + abs(r-l1)/3
        j = r - abs(r-l1)/3
        if (R * T) / (i - b) - a / i**2 < (R * T) / (j - b) - a / j**2:
            r = j
        else:
            l1 = i
print("Локальный минимум:", (R * T) / (l1 - b) - a / l1**2)
l, r = 9.4 * 10 ** -5, 0.0001854
while(abs(r - l) > 10 ** -8):
        i = l + abs(r-l)/3
        j = r - abs(r-l)/3
        if (R * T) / (i - b) - a / i**2 > (R * T) / (j - b) - a / j**2:
            r = j
        else:
            l = i
print("Локальный максимум:", (R * T) / (l - b) - a / l**2)

def f(x):
    return (R * T) / (x - b) - a / x**2

sum = 0
x = l1
while(x <= l):
    sum += ((10**-8)**2 + abs(f(x+10**-8) - f(x))**2) ** 0.5
    x += 10**-8
print("Длина кривой запрещённой зоны:", sum)




T = 143.15
R = 8.314
a =  0.1382
b =  3.19 * 10**-5
Pn = 3664186.998

def F(a, b):
    while(abs(a - b) > 10 ** -9):
        c = (a + b) / 2
        if f1(a) * f1(c) > 0:
            a = c
        else:
            b = c
    return a

def f1(V):
    return ((R * T) / (V - b) - a / V**2) - Pn

fig = plt.figure(figsize=(14, 6))
ax = plt.subplot(1, 1, 1)
V = np.linspace(0.00005, 0.00025, 1000)
P =  ((R * T) / (V - b) - a / V**2) - Pn
plt.plot(V, P)
plt.plot([0.00005, 0.00025], [0, 0])
Vl, Vo, Vg = F(0.00005, 0.000075), F(0.000075, 0.000125), F(0.000125, 0.000225)
print("Корни уравнения:", Vl, Vo, Vg)



def Fsq(l, r):
    i = l
    sq = 0
    while(i < r):
        sq += (f(i) + f(i+10**-8))/2*10**-8
        #sq += abs(f1(i) - f2(i))*0.001
        #sq += abs(f1((i + 0.001) / 2) - f2((i + 0.001)/2))*0.001

        i += 10 ** -8
    return sq
print("Интеграл 1:", Fsq(Vl, Vg))
print("Интеграл 2:", Pn * abs(Vg - Vl))




plt.show()