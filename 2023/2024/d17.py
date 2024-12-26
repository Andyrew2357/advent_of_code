with open('d17_in.txt', 'r') as f:
    AA = int(f.readline().split()[2])
    BB = int(f.readline().split()[2])
    CC = int(f.readline().split()[2])
    f.readline()
    inst = [int(s) for s in f.readline().strip().split()[1].split(',')]

# part 1
def out(A, B, C, inst):
    def get_combo(opd):
        if opd > 3:
            match opd:
                case 4: return A
                case 5: return B
                case 6: return C
        else: return opd

    i = 0
    log = []
    while i < len(inst):
        cmd, opd = inst[i:i+2]

        match cmd:
            case 0:
                A//=(2**get_combo(opd))
            case 1:
                B=B^opd
            case 2:
                B=get_combo(opd)%8
            case 3:
                if not A == 0:
                    i = opd
                    continue
            case 4:
                B=B^C
            case 5:
                log.append(get_combo(opd)%8)
            case 6:
                B=A//(2**get_combo(opd))
            case 7:
                C=A//(2**get_combo(opd))
        
        i+=2
    return log

print(','.join([str(s) for s in out(AA, BB, CC, inst)]))

# part 2
# The easiest way to do this is to reverse engineer the input a little bit.

# Observation 1: The only time the optcode 3 appears is at the end with 3, 0, 
# meaning that the whole program is a loop that terminates when a is zero. 

# Observation 2: A is only modified by optcode 0, in which case it gets floor
# divided. In my input (and I expect everyone's, because otherwise this is hard),
# there is only one such operation, and it importantly only ever has a literal 
# value. For me, it floor divides by 8. (The instruction is 0, 3).

# Observation 3: My input has one print operation that strictly prints whatever
# is in register B. This means, I need the loop to execute a number of times equal
# to the length of the program. Mine has length 16, which means I need the starting
# value of register A to be between 8^15 and 7*8^15. That is an enormously huge
# parameter space to search, so we still need to be more clever.

# Observation 4: The optcodes which modify B are 1, 2, 4, and 6. In my program, the
# commands that modify B are, in order: (2, 4), (1, 5), (4,0), (1, 6), which sets 
# B to A%8, take XOR with 5 (101), take XOR with C, and take XOR with 6 (110).
# This amounts to XOR with 3 (011) and C, equivalently B=B^C^3, where B is the last
# 3 bits of A

# Observation 5: In my input, C gets modified once by the command (7, 5), which sets
# C to A//((A%8)^(101))

# Observation 6: Since the out command only cares about the last 3 bits, effectively
# this means that the full loop takes x=A%8, sets C to A//((A%8)^5), takes the 
# last 3 bits into y, and prints x^y^3.  

# We can now back out the right starting A from these observations.
# Consider the code z as the first in the list. We need x^y^3 = z.
# If we assume we know x, this tells us what y needs to be by y = x^z^3.
# This lets us determine the possible bits prior to x that are consistent.
# This gives us an iterative method to find the right A.

from collections import deque, defaultdict

N = len(inst)
Q = deque([(0, 0)])
nbest = 0
SEEN = {(0, 0)}
solutions = []
while Q:
    A, n = Q.popleft()

    if n > nbest: 
        nbest = n
        print(nbest, len(Q))

    if n == N: 
        solutions.append(A)
        continue

    for i in range(2**9):
        B = A + i*(2**(3*n))
        if B >= 8**N: continue
        if (B, n+1) in SEEN: continue
        if out(B, 0, 0, inst)[:n+1] == inst[:n+1]:
            SEEN.add((B, n+1))
            Q.append((B, n+1))

s = min(solutions)
print(s)