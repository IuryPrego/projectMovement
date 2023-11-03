import matplotlib.pyplot as plt
import numpy as np


def integral(x_axis, y_axis):
    dydx = [0]
    for i in range(0, len(y_axis) - 1):
        dx = x_axis[i + 1] - x_axis[i]
        dy = y_axis[i + 1] - y_axis[i]
        dydx.append(dx * (dy + 2 * y_axis[i]))
    return(dydx)


def axis(Data, a):
    eixo = [0]
    for m in range(0, len(Data)):
        try:
            eixo.append(float(Data[m][a]))
        except:
            continue
    return eixo


def trig(ang, n):
    newang = []
    if abs(n) == 1:
        for i in range(0, len(ang)):
            newang.append(np.sin(ang[i]) * n/abs(n))
    if abs(n) == 2:
        for i in range(0, len(ang)):
            newang.append(np.cos(ang[i]) * n/abs(n))
    if abs(n) == 3:
        for i in range(0, len(ang)):
            newang.append(np.tan(ang[i]) * n/abs(n))
    return(newang)


def clean_axis(axis, trigon, g):
    for i in range(0, len(axis)):
        axis[i] -= (g[i] * trigon[i])
    return(axis)


arq = open('Datas\Accelerometer Data 0005.txt', 'rt')
big_data = arq.read()
arq.close()
big_data = big_data.split('\n')
data = []
for n in big_data:
    data.append(n.split(','))
for i in range(0, len(data)):
    for j in range(0, len(data[i])):
        data[i][j] = data[i][j].strip()

lat_ang = axis(data, 5)
for i in lat_ang:
    i = np.deg2rad(i)
back_ang = axis(data, 6)
for i in back_ang:
    i = np.deg2rad(i)

time = axis(data, 0)
ag = axis(data, 4)

cos_ax = trig(lat_ang, 2)
sin_ay = trig(lat_ang, 1)
cos_az = trig(back_ang, 2)
ax = clean_axis(axis(data, 1), cos_ax, ag)
ay = clean_axis(axis(data, 2), sin_ay, ag)
az = clean_axis(axis(data, 3), cos_az, ag)

dx = integral(time, integral(time, ax))
dy = integral(time, integral(time, ay))
dz = integral(time, integral(time, az))

for i in range(1, 5):
    plt.subplot(3, 2, i).plot(time, axis(data, -i))
plt.subplot(3, 2, 5).plot(time, az)
plt.subplot(3, 2, 6).plot(time, dz)
plt.show()
