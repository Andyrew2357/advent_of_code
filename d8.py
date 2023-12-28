with open('d8_in.txt', 'r') as f:
    lines = f.readlines()

instr = lines[0].strip()
N=len(instr)

rds = dict()
ghst = []

for l in lines[2:]:
    a,_,b,c = l.strip().split()
    rds[a] = (b[1:-1],c[:-1])

    if a[-1] == 'A': ghst.append(a)

st = 0
cur = 'AAA'
while not cur == 'ZZZ':
    ins = instr[st%N]
    st+=1
    cur = rds[cur][0] if ins == 'L' else rds[cur][1]

print(st)

# part 2: I hate this problem, because this is not at all 
# guaranteed to work just given the prompt

dist = []
for a in ghst:
    st = 0
    cur = a
    while not cur[-1] == 'Z':
        ins = instr[st%N]
        st+=1
        cur = rds[cur][0] if ins == 'L' else rds[cur][1]

    dist.append(st)

import math

m=1
for d in dist: m = math.lcm(m,d)

print(m)