import math

with open('d6_in.txt','r') as f:
    lines = f.readlines()
    times = [int(e) for e in lines[0].strip().split()[1:]]
    dists = [int(e) for e in lines[1].strip().split()[1:]]

m=1
for i in range(len(times)):
    T, d = times[i], dists[i]

    disc = math.sqrt((T/2)*(T/2)-d)
    l=T/2-disc
    u=T/2+disc

    if not l == int(l): 
        l = math.ceil(l)
    else:
        l = int(l+1)
    if not u == int(u): 
        u = math.floor(u)
    else:
        u = int(u-1)

    m*=(u-l+1)

print(m)


# part 2
with open('d6_in.txt','r') as f:
    lines = f.readlines()
    T = int(''.join(lines[0].strip().split()[1:]))
    d = int(''.join(lines[1].strip().split()[1:]))

disc = math.sqrt((T/2)*(T/2)-d)
l=T/2-disc
u=T/2+disc

if not l == int(l): 
    l = math.ceil(l)
else:
    l = int(l+1)
if not u == int(u): 
    u = math.floor(u)
else:
    u = int(u-1)

print(u-l+1)