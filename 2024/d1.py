with open('d1_in.txt', 'r') as f:
    A, B = zip(*[(int(s.split(' ')[0]), int(s.split(' ')[-1])) for s in f.read().splitlines()])
    A = sorted(list(A))
    B = sorted(list(B))
    D = [abs(a - b) for a, b in zip(A, B)]
    print(sum(D))

    M = [a*B.count(a) for a in A]
    print(sum(M))
