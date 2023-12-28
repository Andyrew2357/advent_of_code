import numpy as np

# part 1: expan = 2, part 2: expan = 1000000
expan = 1000000
M = expan - 1

with open('d11_in.txt', 'r') as f:
    lines = np.array(f.read().splitlines(), dtype=str)
    grd = np.array([[ch for ch in l] for l in lines])

X, Y = np.where(grd=='#')
# already sorted by rows so expansion there is easy
X[1:]+=M*np.cumsum(np.maximum(0,np.diff(X) - 1))
# sort both lists by cols before expanding cols
Y, X = zip(*sorted(zip(Y,X)))
X, Y = np.array(X), np.array(Y)
Y[1:]+=M*np.cumsum(np.maximum(0,np.diff(Y) - 1))

N=len(X)
s=0
for i in range(N):
    for j in range(i+1,N): s+=np.abs(X[j]-X[i])+(Y[j]-Y[i])

print(s)