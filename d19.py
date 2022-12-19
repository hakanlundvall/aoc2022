# import networkx as nx
from copy import deepcopy
import heapq
from collections import deque, defaultdict
import concurrent.futures
from multiprocessing import freeze_support

if __name__ == '__main__':
    freeze_support()    

data = [x.strip('\n') for x in open("i19.txt").readlines()]
# data = [x.strip('\n') for x in open("t19.txt").readlines()]

M = dict()

for l in data:
    id , rest = l.split(':')
    id = int(id.split()[-1])
    rest = rest.split('.')
    bp =[]
    for r in rest:
        if not r:
            continue
        r1, r2 = r.split(' robot costs ')
        r1 = r1.split()[-1]
        r2 = [x.split()[-2:] for x in r2.split(' and ')]
        r2 = [[int(a), b] for a,b in r2]
        bp.append((r1,r2))
    M[id] = bp

print(M)

def push(Q : list,s):
    heapq.heappush(Q, s)

def pop(Q : list):
    return heapq.heappop(Q)

def neg(x):
    return -x

def encode_state(time, res, rob):
    return [time] + list(zip(map(neg, res), map(neg, rob)))

def decode_state(state):
    rest = state[1:]
    time = state[0]
    res = [list(map(neg, x)) for x in  zip(*rest)]
    return tuple([time, res[0] , res[1]])

def make_key(state):
    return tuple(list(map(tuple, state[1:])))


def calc(id_, bp, end_time):
    print(f"id={id_}")
    Q = []
    push(Q, encode_state(0, [0,0,0,0], [0,0,0,1]))

    best = 0
    maxt = 0
    visited = set()

    max_spend=defaultdict(int)

    for r,c in bp:
        print(r,c)
        for a, b in c:
            max_spend[b] = max(max_spend[b], a)
    max_spend['geode'] = 10**10
    print(max_spend)

    robot_names = [n for n, _ in sorted(max_spend.items(), key=lambda x: -x[1])]
    robot_idx = dict()
    for i ,r in enumerate(robot_names):
        robot_idx[r] = i
    
    print(robot_names)

    while Q:
        state = decode_state(pop(Q))
        time, resources, robots = state

        # discard resources the we don't have time to spend
        for i in range(len(resources)):
            maxr = max_spend[robot_names[i]]*(1+end_time-time)
            if resources[i] > maxr:
                resources[i] = maxr
                pass

        geode = resources[robot_idx['geode']]
        best = max(geode, best)
        if time > maxt:
            maxt = time
            print(id_, state)
        if time >= end_time:
            break
        
        k = make_key(state)

        if k in visited:
            continue
        visited.add(k)
        mining = [0,0,0,0]
        for i, r in enumerate(robot_names):
            mining[i] += robots[i]

        for r, cost in bp:
            build = True
            if robots[robot_idx[r]] >= max_spend[r]:
                continue
            for c, res in cost:
                if resources[robot_idx[res]] - c < 0:
                    build = False
                    break
            if build:
                new_resources = deepcopy(resources)
                new_robots = deepcopy(robots)
                new_robots[robot_idx[r]] += 1
                for c, res in cost:
                    new_resources[robot_idx[res]] -= c
                new_resources = [ sum(a) for a in zip(new_resources,mining)]
                push(Q, encode_state(time +1, new_resources, new_robots))

        new_resources = [ sum(a) for a in zip(resources,mining)]
        push(Q, encode_state(time +1, new_resources, robots))
    return best

part1 = False
run_parallel = True

if part1:
    def calcbest(id_):
        return (id_, calc(id_, M[id_], 24))
    sum_ = 0

    if run_parallel:
        with concurrent.futures.ProcessPoolExecutor() as executor:
            pool = executor.map(calcbest, list(M.keys()))
            for res in pool:
                id_, best = res
                sum_ += id_*best
    else:
        pool = map(calcbest, list(M.keys()))
        for res in pool:
            id_, best = res
            sum_ += id_*best

    print(sum_)
else:
    def calcbest(id_):
        return (id_, calc(id_, M[id_], 32))
    sum_ = 1
    if run_parallel:
        with concurrent.futures.ProcessPoolExecutor() as executor:
            pool = executor.map(calcbest, [1,2,3])
            for res in pool:
                id_, best = res
                sum_ *= best
    else:
        pool = map(calcbest, [1,2,3])
        for res in pool:
            id_, best = res
            sum_ *= best

    print(sum_)
