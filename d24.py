from collections import defaultdict, deque
import heapq
from math import gcd

data = [x.strip('\n') for x in open("i24.txt").readlines()]
# data = [x.strip('\n') for x in open("t24.txt").readlines()]

pos = (0,1)

M = defaultdict(str)
blizzards = defaultdict(list)


for r, l in enumerate(data):
    for c, x in enumerate(l):
        if x in '<>^v':
            blizzards[x].append((r,c))
        if x in '<>^v#':
            M[(r,c)] = x

ep = M.keys()
rs = [r for r,c in ep]
cs = [c for r,c in ep]
maxc = max(cs)
minc = min(cs)
maxr = max(rs)
minr = min(rs)

endpos = (max(rs), max(cs)-1)

w = -1+maxc-minc
h = -1+maxr-minr
period = w*h / gcd(w,h)

state = (0, pos)
Q = []
heapq.heappush(Q, state)

def make_key(state):
    time, pos = state
    return (time%period, pos)


def blizzard_list(time, blizzards):
    d = {
        '<': (0,-time),
        '>': (0,time),
        '^': (-time,0),
        'v': (time,0),
    }
    res = set()
    for k,v in blizzards.items():
        for b in v:
            nr,nc = tuple(map(sum,zip(b,d[k])))
            nr,nc = nr-1,nc-1
            nr %= h
            nc %= w
            nr,nc = nr+1,nc+1
            res.add((nr,nc))
    return res


def trip(time, startpos, endpos):
    maxt = 0
    state = (time, startpos)
    visited = set(make_key(state))
    Q = []
    heapq.heappush(Q, state)

    while Q:
        state = heapq.heappop(Q)
        k = make_key(state)
        if k in visited:
            continue
        visited.add(k)
        time, pos = state
        if time > maxt:
            maxt = time
            print(time)
        if pos == endpos:
            print("end", time)
            return time

        nogo = blizzard_list(time+1, blizzards)
        for d in [(-1,0),(1,0),(0,-1),(0,1),(0,0)]:
            newPos = tuple(map(sum,zip(pos,d)))
            nr, nc = newPos 
            if (nr >= (maxr if nc != maxc-1 else maxr+1)) or (nr <= (minr if nc != 1 else minr-1)) or (nc >= maxc) or (nc <= minc):
                continue
            if (newPos not in nogo):
                heapq.heappush(Q, (time+1, newPos))

t1 = trip(0,(0,1), endpos)
print('Part1', t1)
t2 = trip(t1,endpos, (0,1))
t3 = trip(t2,(0,1), endpos)
print('Part2', t3)
