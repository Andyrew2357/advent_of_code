import heapq as hq
from collections import defaultdict

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

# The cost of making a move on the final (nth) layer if n = 0 is 1
# The cost of making a move on the final (nth) layer if n != 0 depends only on that move and the previous move.
# This is because, in order to make that move all but the n-1 layer above the nth layer must be on A.
# Therefore, the cost of making a move on the nth layer is determined by running dijkstra's on the n-1 layer with costs
# determined by running dijkstra's on the n-2 layer, with this recursive relationship propogating down to the zeroth layer.
# Thus we can solve this problem with a dynamic programming approach by memoizing the costs on each layer
SEEN = {}
def cost(pre_mov, mov, layer):
    k = (pre_mov, mov, layer)
    if k in SEEN: return SEEN[k]
    if layer == 0: return 1

    Q = [(0, 'A', pre_mov, '')]
    S = {}
    while Q:
        dist, pre_stp, x, s = hq.heappop(Q)

        if s == mov:
            SEEN[k] = dist
            return dist
        if len(s) > 0: continue
        s
        if (pre_stp, x) in S: continue
        S[(pre_stp, x)] = dist
        
        for stp in ['>', '^', '<', 'v']:
            if stp in KB[x]: hq.heappush(Q, (dist+cost(pre_stp, stp, layer - 1), stp, KB[x][stp], s))      
        hq.heappush(Q, (dist + cost(pre_stp, 'A', layer - 1), stp, x, s+x))
        # it almost feels like you can forgo this and shortcut to the end in the above step,
        # but you can't because of the way dijkstra's works (doing so would mean sometimes you
        # don't get the lowest option). This was a nightmare to debug.

def nstep(target, layers):
    Q = [(0, '', 'A', 'A')]
    D = {}
    while Q:
        dist, s, pre_mov,  x = hq.heappop(Q)
        if s == target: return dist
        if (s, pre_mov, x) in D: continue
        D[(s, pre_mov, x)] = dist

        for stp in ['>', '^', '<', 'v', 'A']:
            if stp == 'A':
                ns = s + x
                if not target[:len(ns)] == ns: continue
                hq.heappush(Q, (dist + cost(pre_mov, stp, layers), ns, stp, x))
            if stp in CB[x]: 
                hq.heappush(Q, (dist + cost(pre_mov, stp, layers), s, stp, CB[x][stp]))

s1 = 0
for t in C: s1+=int(t[:3])*nstep(t, 2)
print(s1)

s2 = 0
for t in C: s2+=int(t[:3])*nstep(t, 25)
print(s2)
