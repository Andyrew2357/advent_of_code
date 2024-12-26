# This actually reminds me a lot of low level circuit simulation
# Turns out the memoization I implemented reflexively never gets
# used, because the cycle is just too long.
M = 1000

from collections import defaultdict
from collections import deque

S = dict() # state
B = defaultdict(str) # behavior
O = defaultdict(list) # out
I = defaultdict(list) # in
with open('d20_in.txt', 'r') as f:
    for l in f.read().splitlines():
        e = l.split()
        k = 'IN' if e[0] == 'broadcaster' else e[0][1:] 
        O[k] = [s[:-1] if ',' in s else s for s in e[2:]]
        for o in O[k]: I[o].append(k)
        B[k] = l[0]
        S[k] = 'L'

SEEN = dict()
STACK = deque()

p = 0
L, H = 0, 0
while p < M:
    K = frozenset({(k,S[k]) for k in S})
    if K in SEEN: 
        pl, KL, KH = SEEN[K]
        STEP = p - pl
        REPS = ((M-p)//STEP)
        p+=REPS*STEP
        L+=REPS*(L - KL)
        H+=REPS*(H - KH)
        if p == M: break
    
    SEEN[K] = (p, L, H)
    p+=1

    # press the button
    L+=1
    for a in O['IN']: STACK.append((a, 'L'))

    while STACK:
        # receive a pulse
        a, s = STACK.popleft()

        if s == 'L': 
            L+=1
        else:
            H+=1
        
        match B[a]:
            case '%':
                if s == 'H': continue
                S[a] = 'H' if S[a] == 'L' else 'L' 
                for o in O[a]: STACK.append((o, S[a]))
            case '&':
                CH = True
                for i in I[a]: 
                    if S[i] == 'L': CH = False
                S[a] = 'L' if CH else 'H'
                for o in O[a]: STACK.append((o,S[a]))
            case '': continue

print(L*H)

# reasoning out part 2

# rx is only connected to &tg, which is connected to a bunch of &'s.
# I figure that the solution is just going to be taking the least
# common multiple of the cycles of these. I'm also suspicious of
# the fact that the broadcast node has exactly four branches, which
# is the same number of nodes that connect to tg, so I think that the
# puzzle input was constructed by combining four components with
# different cycles.

# I suspect this might be a problem that's very hard in general, but
# the puzzle input is set up in a way that makes it simpler. Basically
# I think that the circuit is somehow to designed to decompose into 
# segments with cycles of different length. Much like the ghost problem
# I think this is annoying, because it's not mathematically satisfying,
# but given past problems, it might work.

# I've figured it out essentially. There are basically just four binary
# counters with reset cycles hardcoded, so what I have to do is figure
# out what those numbers are.

# part 2 BS------------------------------------------------------

def uplayer(nodes): return [j for i in nodes for j in I[i]]
master_nodes = uplayer(uplayer(uplayer(['rx'])))

TIMES = []
for N in master_nodes:
    RESET = 0
    for n in uplayer([N]):
        place = 0
        nd = n
        while not nd == 'IN':
            place+=1
            nd = [a for a in uplayer([nd]) if not a == N][0]
        RESET+=2**(place-1)
    TIMES.append(RESET)

import math
print(math.lcm(*TIMES))

#----------------------------------------------------------------
