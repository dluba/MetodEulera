import matplotlib.pyplot as plot
import math

m = 2.08
p = 1.2
g = 9.81
C = 0.5
S = 0.0055
u0 = 0.5
tNow = 0.0
x = 0
alpha = 0
flaw = 0.0

print("Введите значение tMax:")
tMax = float(input())
tDelta = 0.0001
timeArr = []
xArr = []
xTrueArr = []

errors = []
fig, axs = plot.subplots(2)
axs[0].set_title("Синий - численный, оранжевый - аналитический")
axs[1].set_title("Ошибка")
plot.subplots_adjust(left = None, bottom = None, right = None, top = None, wspace = None, hspace = 0.367)

while tNow < tMax:
 a = -g + p * u0 * u0 * S * C / (2 / m)
u0 += a * tDelta
x += u0 * tDelta + a * tDelta * tDelta / 2
tNow += tDelta
print(tDelta)
print(str(tNow / tMax * 100) + " %")

xArr.append(x)
timeArr.append(tNow)

xTrue = -(-330 - 68 * tNow + 476 * math.log(1 + math.e ** (0.287 * tNow)))
xTrueArr.append(xTrue)
errors.append(x - xTrue)

axs[0].plot(timeArr, xArr)
axs[0].plot(timeArr, xTrueArr)

axs[1].plot(timeArr, errors)
plot.show()
