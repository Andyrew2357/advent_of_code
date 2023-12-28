import numpy as np

def nxt(seq):
    if np.all(seq == 0): return 0
    return seq[-1] + nxt(np.diff(seq))

def prev(seq):
    if np.all(seq == 0): return 0
    return seq[0] - prev(np.diff(seq))


s1, s2 = 0, 0
with open('d9_in.txt', 'r') as f:
    for l in f.readlines():
        seq = np.array([int(e) for e in l.strip().split()])
        s1+=nxt(seq)
        s2+=prev(seq)

print(s1, s2)