import networkx as nx
from networkx.algorithms.approximation import max_clique

with open('d23_in.txt', 'r') as f:
    G = nx.Graph()
    for l in f.read().splitlines():
        a, b = l.split('-')
        G.add_node(a)
        G.add_node(b)
        G.add_edge(a, b)
        G.add_edge(b, a)

print('part 1')
Cyc3 = nx.simple_cycles(G, length_bound=3)
s1 = 0
for cyc in Cyc3:
    if any(nd[0] == 't' for nd in cyc): s1+=1

print(s1)

print('part 2')
party = max_clique(G)
print(party)
print(','.join(sorted(party)))

# this runs like garbage, but it's super easy to implement, so I don't really care
