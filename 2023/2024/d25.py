import numpy as np

with open('d25_in.txt', 'r') as f:
    LKS = []
    KYS = []
    brd = np.zeros((7, 5))

    T = {'.':0, '#':1}
    def addrow(r, l):
        brd[r,:] = np.array([T[s] for s in l.strip()])
    while True:        
        l1 = f.readline()
        addrow(0, l1)
        for i in range(1, 7):
            addrow(i, f.readline())
        if l1 == '#####\n':
            LKS.append(brd.copy())
        else:
            KYS.append(brd.copy())
        lf = f.readline()
        if lf == '': break

s1 = 0
for L in LKS:
    for K in KYS:
        if np.any(L+K == 2): continue
        s1+=1
print(s1)