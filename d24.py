Mn, Mx = 200000000000000, 400000000000000
S = []
with open('d24_in.txt', 'r') as f:
    for l in f.read().splitlines():
        X, V = l.split(' @ ')
        x, y, z = [int(e) for e in X.split(',')]
        vx, vy, vz = [int(e) for e in V.split(',')]

        S.append((x, y, z, vx, vy, vz))
N = len(S)

W = 0
for i in range(N):
    for j in range(i+1, N):
        x11, x21, x31, v11, v21, v31 = S[i]
        x12, x22, x32, v12, v22, v32 = S[j]

        x1, x2 = x12 - x11, x22 - x21
        DET = v11*v22 - v12*v21
        # velocities are linearly dependent
        if DET == 0:
            v1, v2 = v11 - v12, v21 - v22

            # check if same line
            if not (x1*v1 + x2*v2)**2 == (x1**2 + x2**2)*(v1**2 + v2**2):
                continue

            # check if in region particle 1
            if (v11, v21) == (0, 0):
                if not Mn <= x11 <= Mx and Mn <= x21 <= Mx:
                    continue
            t0 = (Mn - x11)/v11 if not v11 == 0 else (Mn - x21)/v21
            t1 = (Mx - x11)/v11 if not v11 == 0 else (Mx - x21)/v21
            t0, t1 = max(t0, 0), max(t1, 0)
            xa, xb = sorted([x11 + t0*v11, x11 + t1*v11])
            ya, yb = sorted([x21 + t0*v21, x21 + t1*v21])

            if not (Mn <= xa <= Mx or Mn <= xb <= Mx or (xa < Mn and xb > Mx)):
                continue
            if not (Mn <= ya <= Mx or Mn <= yb <= Mx or (ya < Mn and yb > Mx)):
                continue

            # check if in region particle 2
            if (v12, v22) == (0, 0):
                if not Mn <= x12 <= Mx and Mn <= x22 <= Mx:
                    continue
            t0 = (Mn - x12)/v12 if not v12 == 0 else (Mn - x22)/v22
            t1 = (Mx - x12)/v12 if not v12 == 0 else (Mx - x22)/v22
            t0, t1 = max(t0, 0), max(t1, 0)
            xa, xb = sorted([x12 + t0*v12, x12 + t1*v12])
            ya, yb = sorted([x22 + t0*v22, x22 + t1*v22])

            if not (Mn <= xa <= Mx or Mn <= xb <= Mx or (xa < Mn and xb > Mx)):
                continue
            if not (Mn <= ya <= Mx or Mn <= yb <= Mx or (ya < Mn and yb > Mx)):
                continue
            
            W+=1
            continue
        # velocities not linearly independent
        t1 = (v22*(x1) - v12*(x2))/DET
        t2 = -(v11*(x2) - v21*(x1))/DET

        if t1 < 0 or t2 < 0: continue
        x, y = x11 + t1*v11, x21 + t1*v21
        if Mn <= x <= Mx and Mn <= y <= Mx: 
            W+=1
        
print(W)

# part 2
# Let (x0, v0) be the initial conditions of the projectile in question
# Let (xi, vi) be the initial conditions of the ith projectile.
# To get a collision with the ith projectile, we must satisfy
#           x0 - xi = ti*(vi - v0)
# Due to the number of equations (3 per i) and unknowns (1 per i + 6),
# the solution is overdetermined by the 3rd projectile, so the rest of
# the input is redundant.

# Annoyingly, this is a nonlinear system of equations, which complicates
# things slightly (makes the solution less satisfying in my opinion)
# It also forced me to learn how z3 works though, so I guess that's a plus.

from z3 import *

s = Solver()
x, y, z = Int('x'), Int('y'), Int('z')
vx, vy, vz = Int('vx'), Int('vy'), Int('vz')
T = [Int(f't{i}') for i in range(3)]

for i in range(3):
    xi, yi, zi, vxi, vyi, vzi = S[i]
    s.add(xi + T[i]*vxi == x + T[i]*vx)
    s.add(yi + T[i]*vyi == y + T[i]*vy)
    s.add(zi + T[i]*vzi == z + T[i]*vz)

res = s.check()
m = s.model()
print(m.eval(x+y+z))
