data = [x.strip('\n') for x in open("i12.txt").readlines()]
# data = [ x.strip('\n') for x in open("t12.txt").readlines() ]

m = dict()
starts=[]
for y,l in enumerate(data):
    for x,h in enumerate(l):
        m[(x,y)] = h
        if h == 'S':
            start = (x,y)
            starts.append(start)
        if h == 'a':
            starts.append((x,y))        
        if h == 'E':
            end = (x,y)

def height(p):
    if m[p] == "S":
        return ord('a')
    elif m[p] == "E":
        return ord('z')
    else:
        return ord(m[p]) 

def neighbors(pos):
    dirs = [(-1,0), (0,-1), (1,0) ,(0,1)]
    for d in dirs:
        p2 = (pos[0] + d[0], pos[1] + d[1])
        if p2 not in m:
            continue
        if height(p2)-1 <= height(pos):
            yield p2


from collections import deque

def bfs(part):
    Q = deque()
    if part == 1:
        Q.append((start, 0))
    else:
        for s in starts:
            Q.append((s, 0))
    
    v = set()

    while Q:
        p, c = Q.popleft()
        if p in v:
            continue
        v.add(p)
        for nb in neighbors(p):
            Q.append((nb, c+1))
            if nb == end:
                print(c+1)
                return

bfs(1)
bfs(2)


import networkx as nx

G = nx.DiGraph()

for p in m.keys():
    for n in neighbors(p):
        G.add_edge(p,n)

print(nx.shortest_path_length(G, start,end))

all = []
for st in starts:
    try:
        all.append(nx.shortest_path_length(G, st,end))
    except:
        pass

print(min(all))
