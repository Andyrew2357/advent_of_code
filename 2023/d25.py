# We're trying to find a minimum cut of a graph
# I'm just going to use the networkx library, 
# since they have a minimum_edge_cut implementation

import networkx as nx

G = nx.Graph()
with open('d25_in.txt', 'r') as f:
    for l in f.read().splitlines():
        A, *B = l.split()
        a = A[:-1]
        G.add_node(a)
        for b in B: 
            G.add_node(b)
            G.add_edge(a, b)

E = nx.minimum_edge_cut(G)
G.remove_edges_from(E)
N, M = [len(c) for c in nx.connected_components(G)]
print(N*M)
