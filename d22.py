from copy import deepcopy
from collections import defaultdict

data = [x.strip('\n') for x in open("i22.txt").readlines()]
# data = [x.strip('\n') for x in open("t22.txt").readlines()]

M = dict()

def maxdef() -> int :
    return 10*10

maxrows = defaultdict(int)
minrows = defaultdict(maxdef)
maxcols = defaultdict(int)
mincols = defaultdict(maxdef)

for r, l in enumerate(data,1):
    if l == "":
        break
    for c, x in enumerate(l,1):
        if x != " ":
            M[(r,c)] = x

instr = data[-1]

for r in range(1, 1+max([rr for rr, _ in M.keys()])):
    l = [ cc for rr,cc in M.keys() if rr == r]    
    maxcols[r] = max(l)
    mincols[r] = min(l)

for c in range(1, 1+max([cc for _, cc in M.keys()])):
    l = [ rr for rr,cc in M.keys() if cc == c]    
    maxrows[c] = max(l)
    minrows[c] = min(l)

def move(pos, d, i):
    r,c = pos
    for x in range(i):
        if d == 0:
            next_p = (r, c+1)
            m = M.get(next_p, 'x')
            if m == '.':
                r,c = next_p
                continue
            if m == "#":
                break
            c1 = mincols[r]
            if M[(r,c1)] == '.':
                c = c1
        elif d == 1:
            next_p = (r+1, c)
            m = M.get(next_p, 'x')
            if m == '.':
                r,c = next_p
                continue
            if m == "#":
                break
            r1 = minrows[c]
            if M[(r1,c)] == '.':
                r = r1
        elif d == 2:
            next_p = (r, c-1)
            m = M.get(next_p, 'x')
            if m == '.':
                r,c = next_p
                continue
            if m == "#":
                break
            c1 = maxcols[r]
            if M[(r,c1)] == '.':
                c = c1
        else:
            assert d == 3
            next_p = (r-1, c)
            m = M.get(next_p, 'x')
            if m == '.':
                r,c = next_p
                continue
            if m == "#":
                break
            r1 = maxrows[c]
            if M[(r1,c)] == '.':
                r = r1
    return (r,c)



def face(pos):
    r,c = pos
    if r <= 50:
        if c <= 100:
            return 'A'
        else:
            return 'B'
    elif r <= 100:
        return 'C'
    elif r <= 150:
        if c <= 50:
            return 'D'
        else:
            return 'E'
    else:
        return 'F'

tf = {
    'A': 
        { 
            0: ('B', 0, lambda r,c : (r, 101)), 
            1: ('C', 1, lambda r,c : (51, c)), 
            2: ('D', 0, lambda r,c : (151-r, 1)), 
            3: ('F', 0, lambda r,c : (c+100, 1)), 
        },
    'B': 
        { 
            0: ('E', 2, lambda r,c : (151-r, 100)),  
            1: ('C', 2, lambda r,c : (c-50, 100)),  
            2: ('A', 2, lambda r,c : (r, 100)), 
            3: ('F', 3, lambda r,c : (200, c-100)), 
        },
    'C': 
        { 
            0: ('B', 3, lambda r,c : (50, r+50)),  
            1: ('E', 1, lambda r,c : (101, c)),  
            2: ('D', 1, lambda r,c : (101, r-50)), 
            3: ('A', 3, lambda r,c : (50, c)), 
        },
    'D': 
        { 
            0: ('E', 0, lambda r,c : (r, 51)),  
            1: ('F', 1, lambda r,c : (151, c)),  
            2: ('A', 0, lambda r,c : (151-r, 51)), 
            3: ('C', 0, lambda r,c : (c+50, 51)), 
        },
    'E': 
        { 
            0: ('B', 2, lambda r,c : (151-r, 150)),  
            1: ('F', 2, lambda r,c : (c+100, 50)),  
            2: ('D', 2, lambda r,c : (r, 50)), 
            3: ('C', 3, lambda r,c : (100, c)), 
        },
    'F': 
        { 
            0: ('E', 3, lambda r,c : (150, r-100)),  
            1: ('B', 1, lambda r,c : (1, c+100)),  
            2: ('A', 1, lambda r,c : (1, r-100)), 
            3: ('D', 3, lambda r,c : (150, c)), 
        },
        }


def next_pos(pos,d):
    r,c = pos
    rr = r % 50
    cc = c % 50
    if (d == 0) and (cc != 0):
        return (r, c+1), d
    elif (d == 1) and (rr != 0):
        return (r+1, c), d
    elif (d == 2) and (cc != 1):
        return (r, c-1), d
    elif (d == 3) and (rr != 1):
        return (r-1, c), d

    f = face(pos)
    f2, d2, transf = tf[f][d] 
    next_p = transf(*pos)    
    
    ft = face(next_p)
    assert ft == f2
    f2t, d2t, transft = tf[ft][(d2+2)%4]
    next_pt = transft(*next_p)

    assert next_pt == pos

    return next_p, d2

def move2(pos, d, i):
    pos = deepcopy(pos)
    for x in range(i):
        next_p, next_d = next_pos(pos, d)
        if M[next_p] == '.':
            (pos , d) = (next_p, next_d)
        else:
            assert M[next_p] == '#'
            break
    return pos, d


pos = (1, mincols[1])
d = 0
x = ""
for i in instr:
    if i in "LR":
        ii = int(x)
        x = ""
        pos, d = move2(pos, d,ii)
        d += 1 if i == 'R' else -1
        d %= 4 
    else:
        x += i

if len(x) > 0:
    ii = int(x)
    x = ""
    pos = move(pos, d,ii)

# print(pos, d)
print(1000 * pos[0] + 4 * pos[1] + d)