with open('d19_in.txt', 'r') as f:
    T = f.readline().strip().split(', ')
    f.readline()
    D = f.read().splitlines()

SEEN = {}
def buildable(dsn):
    if dsn == '': return True
    if dsn in SEEN: return SEEN[dsn]

    for twl in T:
        n = len(twl)
        if n > len(dsn): continue
        if twl == dsn[:n]:
            if buildable(dsn[n:]):
                SEEN[dsn] = True
                return True

    SEEN[dsn] = False
    return False

s1 = 0
for dsn in D:
    if buildable(dsn): s1+=1
print(s1)

# part 2
SEEN = {}
def nbuilds(dsn):
    if dsn == '': return 1
    if dsn in SEEN: return SEEN[dsn]

    builds = 0
    for twl in T:
        n = len(twl)
        if n > len(dsn): continue
        if twl == dsn[:n]: builds+=nbuilds(dsn[n:])

    SEEN[dsn] = builds
    return builds

s2 = 0
for dsn in D:
    s2+=nbuilds(dsn)
print(s2)
