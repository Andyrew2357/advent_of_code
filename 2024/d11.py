with open('d11_in.txt', 'r') as f:
    S = [int(s) for s in f.readline().strip().split()]

SEEN = {}
def nstone(n, t):
    if t == 0: return 1
    st = (n, t)
    if st in SEEN: return SEEN[st]

    s = str(n)
    ns = len(s)
    if ns%2 == 0:
        res = nstone(int(s[:ns//2]), t-1) + nstone(int(s[ns//2:]), t-1)
    elif n == 0:
        res = nstone(1, t-1)
    else:
        res = nstone(n*2024, t-1)

    SEEN[st] = res
    return res

print(sum([nstone(s, 25) for s in S]))
print(sum([nstone(s, 75) for s in S]))
