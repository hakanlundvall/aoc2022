from collections import defaultdict
import networkx as nx
import heapq

data = [x.strip('\n') for x in open("i16.txt").readlines()]
# data = [ x.strip('\n') for x in open("t16.txt").readlines() ]


m = dict()
for l in data:
    parts = l.split()
    v = parts[1]
    rate = int(parts[4].split('=')[1].strip(';'))
    tunnels = parts[9:]
    tunnels = [x.strip(',') for x in tunnels]
    m[v] = [rate, tunnels]

G = nx.Graph()

for k, v in m.items():
    for n in v[1]:
        G.add_edge(k, n)

has_flow = [x for x in m.keys() if m[x][0] > 0] + ['AA']
dist = defaultdict(list)
for i in has_flow:
    for j in has_flow:
        if i != j:
            dist[i].append((nx.shortest_path_length(G, i, j), j))

q = []
n_hasflow = len(has_flow)
heapq.heappush(q, [0, 0, "AA", frozenset(["AA"])])
best = dict()
end_time = 30
while q:
    tot_time, s, valve, opened = heapq.heappop(q)

    if tot_time == end_time:
        print(-min(best.values()))
        break

    heapq.heappush(q, [end_time, s, valve, opened])
    
    for dst, new_valve in dist[valve]:
        new_time = tot_time+dst+1
        if (new_valve not in opened) and (new_time <= end_time):
            new_s = s - (end_time - new_time) * m[new_valve][0]
            new_opened = frozenset(list(opened) + [new_valve])
            if best.get(new_opened, 1) > new_s:
                heapq.heappush(q, [new_time, new_s, new_valve, new_opened])
                best[new_opened] = new_s


q = []
heapq.heappush(q, [4, 0, 4, "AA", 4, "AA", frozenset(["AA"])])
best = dict()
while q:
    tot_time, s, t1, valve1, t2, valve2, opened = heapq.heappop(q)
    valve = [valve1, valve2]
    t = [t1, t2]

    if tot_time == end_time:
        print(-min(best.values()))
        break

    heapq.heappush(q, [end_time, s, end_time,
                    valve1, end_time, valve2, opened])

    for moving in range(2):
        for dst, new_valve in dist[valve[moving]]:
            new_time = t[moving]+dst+1
            if (new_valve not in opened) and (new_time <= end_time):
                new_s = s - (end_time - new_time) * m[new_valve][0]
                new_opened = frozenset(list(opened) + [new_valve])
                if best.get(new_opened, 1) > new_s:
                    if moving == 0:
                        heapq.heappush(
                            q, [new_time, new_s, new_time, new_valve, t2, valve2, new_opened])
                    else:
                        heapq.heappush(
                            q, [new_time, new_s, t1, valve1, new_time, new_valve, new_opened])
                    best[new_opened] = new_s
