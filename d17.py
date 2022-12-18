from collections import defaultdict
import networkx as nx
import heapq

data = [x.strip('\n') for x in open("i17.txt").readlines()]
data = [ x.strip('\n') for x in open("t17.txt").readlines() ]


p1 = list([(0,0),(1,0),(2,0),(3,0),])
p2 = list([(0,-1),(1,-1),(2,-1),(1,0),(1,-2)])
p3 = list([(0,0),(1,0),(2,0),(2,-1),(2,-2)])
p4 = list([(0,0),(0,-1),(0,-2),(0,-3)])
p5 = list([(0,0),(0,-1),(1,0),(1,-1),])

rocks = [p1,p2,p3,p4,p5]
r = 0
top = 0
ii = 0

m=set()

def checkcollision(rock):
    if (max([x for x,y in rock]) <= 4) and (min([x for x,y in rock]) > -3) and (max([y for x,y in rock]) < 0):
        for p in rock:
            if p in m:
                return False
        return True
    return False

from copy import deepcopy


def drawcave(rock):
    print()
    lines=["+-------+"]
    for y in range(-1,-10,-1):
        line = "|"
        for x in range(-2,5):
            if (x,y) in m:
                line += "#"
            elif rock and (x,y) in rock:
                line += "@"
            else:
                line += "."
        line += "|"

        lines.append(line)
    for l in reversed(lines):
        print(l)
    print()

maxpos = defaultdict(int)


for count in range(2022):
    fallingrock = deepcopy(rocks[count%5])
    i = 4-top
    fallingrock = [ (x, y - i) for x,y in fallingrock]
    # drawcave(fallingrock)

    while True:
        w = data[0][ii]
        ii += 1
        if ii >= len(data[0]):
            ii = 0

        d = 1 if w == '>' else -1
        nextfallingrock =  [ (x+d, y) for x,y in fallingrock]
        if checkcollision(nextfallingrock):
            fallingrock = nextfallingrock

        nextfallingrock =  [ (x, y+1) for x,y in fallingrock]
        if checkcollision(nextfallingrock):
            fallingrock = nextfallingrock
        else:
            for p in fallingrock:
                m.add(p)
                x,y = p
                maxpos[x] = min(y,maxpos[x])
                top = min(top, p[1])
            remove = set()
            for p in m:
                x,y = p
                if y > maxpos[x]+1000:
                    remove.add(p)
            m.difference_update(remove)
            break

print(top)