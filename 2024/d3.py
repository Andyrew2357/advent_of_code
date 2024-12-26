import re

with open('d3_in.txt', 'r') as f:
    text = f.read()
    muls = re.findall(r'mul\((\d+),(\d+)\)', text)
    print(sum([int(a)*int(b) for a, b in muls]))

    instr = re.findall(r'(do\(\)|don\'t\(\)|mul\((\d+),(\d+)\))', text)
    P = 0
    enabled = True
    for inst, a, b in instr:
        if inst == "do()": 
            enabled = True
        elif inst == "don't()":
            enabled = False
        elif enabled:
            P+=int(a)*int(b)
    
    print(P)
