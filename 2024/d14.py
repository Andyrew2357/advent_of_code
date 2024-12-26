XX, YY = 101, 103
T = 100
C = [0, 0, 0, 0]
R = []
with open('d14_in.txt', 'r') as f:
    for l in f.read().splitlines():
        X, V = l.split()
        x, y = X.split(',')
        dx, dy = V.split(',')
        x, y = int(x[2:]), int(y)
        dx, dy = int(dx[2:]), int(dy)
        R.append((x, y, dx, dy))

        xf, yf = (x + T*dx)%XX, (y + T*dy)%YY
        if xf == XX//2 or yf == YY//2: continue
        C[2*((xf+XX//2)//XX) + (yf+YY//2)//YY]+=1

p = 1
for c in C: p*=c
print(p)

from matplotlib import pyplot as plt
from math import lcm
from collections import defaultdict

def disp(t):
    X = [(x+t*dx)%XX for x, y, dx, dy in R]
    Y = [-(y+t*dy)%YY for x, y, dx, dy in R]

    plt.scatter(X, Y)
    plt.title(f'Time: {t}') 
    plt.show()

# My philosophy is similar logic to the random phase approximation in condensed matter
# If the robots are randomly distributed, we expect the sum to be small, but if there
# is a systematic order, we can expect it to be nonzero
def score(t):
    X = [((x+t*dx)%XX, (y+t*dy)%YY) for x, y, dx, dy in R]
    return abs(sum((x-XX//2)+(y-YY//2) for x, y in X))

best_t = 0
best_s = 0
for t in range(lcm(XX, YY)): 
    if t%100 == 0: print(t, best_t, best_s)
    s = score(t)
    if s > best_s:
        best_s = s
        best_t = t

print(best_t)
if False: disp(best_t)
