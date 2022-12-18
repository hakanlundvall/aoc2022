import networkx as nx
from collections import Counter

data = [x.strip('\n') for x in open("i18.txt").readlines()]
# data = [x.strip('\n') for x in open("t18.txt").readlines()]


m = dict()
G = nx.Graph()
G2 = nx.Graph()

def add_scan2(m, s):
    assert s not in m
    other = m.keys()
    sides = 6
    neighbors = list()
    G.add_node(s)
    for x in other:
        c = Counter([abs(a-b) for a, b in zip(x, s)])
        if c[0] == 2 and c[1] == 1:
            m[x][0] -= 1
            m[x][1].append(s)
            sides -= 1
            neighbors.append(x)
            G.add_edge(s, x)
    m[s] = [sides, neighbors]


for l in data:
    x = tuple([int(x) for x in l.split(',')])
    add_scan2(m, x)

part1 = sum([a for a, b in m.values()])
print(part1)

v  = m.keys()
G = nx.Graph()
hole = set()
coords = list(zip(*v))
minc = [min(list(x)) for x in coords]
maxc = [max(list(x)) for x in coords]
for x in range(minc[0], maxc[0]+1):
    for y in range(minc[1], maxc[1]+1):
        for z in range(minc[2], maxc[2]+1):
            m = (x, y, z)
            G.add_node(m)
            for d in [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0),]:
                n = (x+d[0], y+d[1], z+d[2])
                if (n in v) == (m in v):
                    G.add_edge(n, m)
                else:
                    G2.add_edge(n,m)
                if (m in v):
                    G.add_edge(m, 1)
                else:
                    if ((n[0] < minc[0]) or (n[0] > maxc[0]) or (n[1] < minc[1]) or (n[1] > maxc[1]) or (n[2] < minc[2]) or (n[2] > maxc[2])):
                        G.add_edge(m, 0)
cc = nx.connected_components(G)
# print([x for x in nx.neighbors(G,(2,2,5))])


trapped = set()
for x in cc:
    if 0 in x:
        pass
        # print("Edge")
    elif 1 in x:
        pass
        # print("Rock")
    else:
        # print("Trapped")
        # print(x)
        trapped.update(x)

# print(trapped)    
count = 0
for n in trapped:
    # print(list(nx.neighbors(G2,n)))
    if n in G2.nodes():
        count += len(list(nx.neighbors(G2,n)))

print(part1-count)