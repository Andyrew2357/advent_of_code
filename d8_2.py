# was writing something to rigorously solve this problem,
# but turns out the puzzle designer made it line up so a
# totally unjustified simplifcation (taking LCM of dist)
# works with every puzzle input.

with open('d8_in.txt', 'r') as f:
    lines = f.readlines()

instr = lines[0].strip()
N=len(instr)

rds = dict()
strt = []

for l in lines[2:]:
    a,_,b,c = l.strip().split()
    rds[a] = (b[1:-1],c[:-1])
    if a[-1] == 'A': strt.append(a)

def behavior(g):
    st = 0
    bhv = dict()

    cur = g
    while True:
        if cur[-1] == 'Z':
            k = (cur, st%N)
            if k in bhv:
                return bhv[k], st
            bhv[k] = st

        cur = rds[cur][0] if instr[st%N] == 'L' else rds[cur][1]
        st+=1

for a in strt:
    print(behavior(a))