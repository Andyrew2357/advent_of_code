# calculate the internal area with a path integral ydx

with open('d18_in.txt', 'r') as f:
    lines = [l.split() for l in f.read().splitlines()]
    instr = [(a, int(b), c) for (a, b, c) in lines]

y = 0
clk = 0
aclk = 0
pdr = '-'
for dr, d, clr in instr:
    match dr:
        case 'U': 
            if pdr == 'R': clk-=y # CLK
            if pdr == 'L': aclk+=y # aCLK
            y+=d
        case 'D': 
            if pdr == 'L': clk+=(y-1) # CLK
            if pdr == 'R': aclk-=(y-1) # aCLK
            y-=d
        case 'L': 
            if pdr == 'D': clk-=(y-1) # CLK
            clk-=d*(y-1) # CLK
            if pdr == 'U': aclk-=y # aCLK
            aclk-=d*y # aCLK
        case 'R':
            if pdr == 'U': clk+=y # CLK
            clk+=d*y # CLK
            if pdr == 'D': aclk+=(y-1) # aCLK
            aclk+=d*(y-1) # aCLK
    pdr = dr

print(max(abs(clk), abs(aclk)))

# part 2 (same thing, different input)
y = 0
clk = 0
aclk = 0
pdr = '-'
DR = {'0':'R', '1':'D', '2':'L', '3':'U'}
for _, __, clr in instr:
    d, dr = int(clr[2:-2], 16), DR[clr[-2]]
    match dr:
        case 'U': 
            if pdr == 'R': clk-=y # CLK
            if pdr == 'L': aclk+=y # aCLK
            y+=d
        case 'D': 
            if pdr == 'L': clk+=(y-1) # CLK
            if pdr == 'R': aclk-=(y-1) # aCLK
            y-=d
        case 'L': 
            if pdr == 'D': clk-=(y-1) # CLK
            clk-=d*(y-1) # CLK
            if pdr == 'U': aclk-=y # aCLK
            aclk-=d*y # aCLK
        case 'R':
            if pdr == 'U': clk+=y # CLK
            clk+=d*y # CLK
            if pdr == 'D': aclk+=(y-1) # aCLK
            aclk+=d*(y-1) # aCLK
    pdr = dr

print(max(abs(clk), abs(aclk)))
