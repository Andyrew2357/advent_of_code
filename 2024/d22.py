from collections import defaultdict

with open('d22_in.txt', 'r') as f: N = [int(s) for s in f.read().splitlines()]

msk = (1 << 24) - 1
def update(n):
    a = msk&(n^(n << 6))
    a = msk&(a^(a >> 5))
    return msk&(a^(a << 11))

def update_t(n, t):
    a = n
    for _ in range(t): a = update(a)
    return a

s1 = 0
for n in N: 
    s1+=update_t(n, 2000)
print(s1)

TOT_BANANAS = defaultdict(int)
def buys(n, t):
    SEEN = set()
    a = n
    p1, p2, p3, p4, = None, None, None, None
    for i in range(t):
        b = update(a)
        pr = b%10
        p1, p2, p3, p4 = p2, p3, p4, pr - a%10
        a = b
        k = (p1, p2, p3, p4)
        if any(p is None for p in k): continue
        if k in SEEN: continue
        SEEN.add(k)
        TOT_BANANAS[k]+=pr

for n in N: buys(n, 2000)
print(max([TOT_BANANAS[k] for k in TOT_BANANAS]))
