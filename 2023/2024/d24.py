from collections import deque

nout = 46
with open('d24_in.txt', 'r') as f:
    XX = {}
    YY = {}
    while True:
        l = f.readline()
        if l == '\n': break
        k, v = l.strip().split()
        if k[0] == 'x': 
            XX[k[:-1]] = int(v)
        else:
            YY[k[:-1]] = int(v)

    RUL = {}
    for l in f.read().splitlines():
        a, op, b, _, o = l.split()
        RUL[o] = (a, op, b)

def oper(a, op, b):
    match op:
        case 'AND': return a&b
        case 'OR': return a|b
        case 'XOR': return a^b

def evaluate(X, Y, nd):
    if nd[0] == 'x': return X[nd]
    if nd[0] == 'y': return Y[nd] 
    a, op, b = RUL[nd]
    return oper(evaluate(X, Y, a), op, evaluate(X, Y, b))
    
ZZ = [evaluate(XX, YY, 'z'+str(i).zfill(2)) for i in range(nout)]
print(sum([(2**i)*ZZ[i] for i in range(nout)]))

def bit_preset(x, y, a, i):
    X = {'x'+str(i).zfill(2):0 for i in range(nout-1)}
    Y = {'y'+str(i).zfill(2):0 for i in range(nout-1)}
    if x: X['x'+str(i).zfill(2)] = 1
    if y: Y['y'+str(i).zfill(2)] = 1
    if a:
        X['x'+str(i-1).zfill(2)] = 1
        Y['y'+str(i-1).zfill(2)] = 1
    return X, Y

def profile_bit(i):
    for a in [0, 1]:
        for x, y in [(0,0), (0,1), (1,0), (1,1)]:
            z = evaluate(*bit_preset(x, y, a, i), 'z'+str(i).zfill(2))
            if not z == x^y^a: return False
        if i == 0: break
    return True

def bad_bits():
    b = []
    for i in range(nout):
        if not profile_bit(i): b.append(i)
    return b

def dependents(nd):
    if nd[0] in ['x', 'y']: return set()
    a, op, b = RUL[nd]
    S = set() if nd[0] == 'z' else {nd}
    return S.union(dependents(a)).union(dependents(b))

bad = bad_bits()
# print(bad)
frozen = set()
for i in range(nout):
    if i in bad: continue
    frozen = frozen.union(dependents('z'+str(i).zfill(2)))


obv_wrong = []
obv_ind = []
dep_wrong = []
dep_ind = []
# print('output ops')
for i in bad:
    a, op, b = RUL['z'+str(i).zfill(2)]
    # print('z'+str(i).zfill(2), RUL['z'+str(i).zfill(2)])
    if op == 'XOR': 
        dep_wrong.append('z'+str(i).zfill(2))
        dep_ind.append(i)
    else:
        obv_wrong.append('z'+str(i).zfill(2))
        obv_ind.append(i)
# print('----------------------------')

candidates = []
for rul in RUL:
    a, op, b = RUL[rul]
    if op == 'XOR': 
        if rul[0] == 'z'and not int(rul[1:]) in bad: continue
        if a[0] in ['x', 'y']: continue
        if b[0] in ['x', 'y']: continue
        candidates.append(rul)
        # print(rul, RUL[rul])

def swap(nd1, nd2):
    temp = RUL[nd1]
    RUL[nd1] = RUL[nd2]
    RUL[nd2] = temp

def ppp(nd):
    print(nd, RUL[nd])

# print(bad)
# print(obv_wrong) # 45 is a fluke since it's the last bit and behaves differently

# I tried an approach looking for nodes that could replace the ones that were obviously out of place, but I definitely did it incorrectly
# part of this was because I didn't realize until a little later that the last bit was a fluke since it's a half adder.

def print_dep(nd):
    Q = deque([nd])
    while Q:
        # print(Q)
        nd = Q.popleft()
        if nd == 'break':
            print('--------------------------------')
            continue
        ppp(nd)
        a, op, b = RUL[nd]
        if not a[0] in ['x', 'y']: 
            Q.append('break')
            Q.append(a)
            Q.append(b)

# attempt to solve by eye using print_dep
# print_dep('z10')
# nnf
# print_dep('z30')
# kqh
# print_dep('z31')
# ddn
# print_dep('z21')
# nhs
# This is slightly off, so I need to think a little harder something I did here was wrong, though, 
# as it turns out, it wasn't all that far off from the real answer.

# The circuit itself appears to be a ripple carry adder, so we can do some checks to find out of place nodes
# I'm not totally convinced this will work for every input, but I don't care to think too deeply about it.
WRONG = set()
for o in RUL:
    a, op, b = RUL[o]
    if o[0] == 'z' and op != 'XOR' and int(o[1:]) != nout-1: WRONG.add(o)
    if op == 'XOR' and all(s[0] not in ['x', 'y', 'z'] for s in [o, a, b]): WRONG.add(o)
    if op == 'AND' and 'x00' not in [a, b]:
        for o1 in RUL:
            a1, op1, b1 = RUL[o1]
            if (o == a or o == b) and op1 != 'OR': WRONG.add(o)
    if op == 'XOR':
        for o1 in RUL:
            a1, op1, b1 = RUL[o1]
            if (o == a1 or o == b1) and op1 == 'OR': WRONG.add(o)


nds = list(WRONG)
print(','.join(sorted(nds)))