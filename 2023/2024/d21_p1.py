import heapq as hq

with open('d21_in.txt', 'r') as f: C = f.read().splitlines()

KB = {
    '<':{'>':'v'}, 
    'v':{'>':'>', '^':'^', '<':'<'}, 
    '^':{'v':'v', '>':'A'}, 
    '>':{'^':'A', '<':'v'},
    'A':{'<':'^', 'v':'>'}
}
CB = {
    'A':{'^':'3', '<':'0'},
    '0':{'>':'A', '^':'2'},
    '1':{'>':'2', '^':'4'},
    '2':{'>':'3', '^':'5', '<':'1', 'v':'0'},
    '3':{'^':'6', '<':'2', 'v':'A'},
    '4':{'>':'5', '^':'7', 'v':'1'},
    '5':{'>':'6', '^':'8', '<':'4', 'v':'2'},
    '6':{'^':'9', '<':'5', 'v':'3'},
    '7':{'>':'8', 'v':'4'},
    '8':{'>':'9', '<':'7', 'v':'5'},
    '9':{'<':'8', 'v':'6'}    
}

def propogate(s, p, m, l=0):
    if m == 'A': 
        if l == len(B)-1: return (s+p[l], p[:])
        return propogate(s, p[:], p[l], l+1)
    if not m in B[l][p[l]]: return None
    np = p[:]
    np[l] = B[l][p[l]][m]
    return (s, np)

def nsteps(target, i):
    Q = [(0, '', tuple(['A']*i))]
    D = {}
    while Q:
        d, s, p  = hq.heappop(Q)
        if (s, p) in D: continue
        if s == target: return d
        D[(s, p)] = d

        p = list(p)
        for m in ['>', '^', '<', 'v', 'A']:
            nq = propogate(s, p[:], m)
            if nq is None: continue
            ns, np = nq
            if not ns == target[:len(ns)]: continue
            hq.heappush(Q, (d+1, ns, tuple(np)))

B = [KB.copy(), KB.copy(), CB.copy()]
s1 = 0
for t in C: 
    n = nsteps(t, len(B))
    c = int(t[:3])
    s1+=c*n
print(s1)

# quit()
B = [KB.copy()]*25 + [CB.copy()]
s2 = 0
for t in C:
    print(t) 
    n = nsteps(t, len(B))
    c = int(t[:3])
    s2+=c*n
print(s2)

# I expected this wouldn't work for part 2, but the implementation was easy for part 1 so I kind of crossed my fingers.
# The full solution I came up with is in d21.py