from collections import defaultdict

part = 2

data = [x.strip('\n') for x in open("i23.txt").readlines()]
# data = [x.strip('\n') for x in open("t23.txt").readlines()]

for part in [1,2]:
    M = dict()

    for r, l in enumerate(data):
        for c, x in enumerate(l):
            if x == '#':
                M[(r,c)] = (r,c)

    dirs = [
        [(-1,0),(-1,1),(-1,-1),],
        [(1,0),(1,1),(1,-1),],
        [(0, -1),(1, -1),(-1, -1),],
        [(0, 1),(1, 1),(-1, 1),],

    ]

    def printmap(M):
        ep = M.keys()
        rs = [r for r,c in ep]
        cs = [c for r,c in ep]
        for r in range(min(rs), max(rs)+1):
            for c in range(min(cs), max(cs)+1):
                print('#' if (r,c) in M else '.', end='')
            print()


    for round in range(10 if part == 1 else 10000000):
        # print(f"\nround {round}")
        # printmap(M)
        for e in M.keys():
            found = False
            for dp in [(-1,0),(-1,1),(-1,-1),(1,0),(1,1),(1,-1),(0, -1),(0, 1),]:
                check_pos = tuple(map(sum,zip(e,dp))) 
                if check_pos in M:
                    found = True
            if not found:
                M[e] = e
                continue
                
            for test_d in range(round, round + 4):
                d = dirs[test_d%4]
                new_pos = tuple(map(sum,zip(e,d[0]))) 
                found = False
                for dp in d:
                    check_pos = tuple(map(sum,zip(e,dp))) 
                    if check_pos in M:
                        found = True
                        break
                if found:
                    M[e] = e
                else:
                    M[e] = new_pos
                    break
        
        M2 = defaultdict(int)
        for e, e2 in M.items():
            M2[e2] += 1

        M3 = dict()
        for e, e2 in M.items():
            if M2[e2] > 1:
                M3[e] = e
            else:
                M3[e2] = e2
        if part == 2 and M.keys() == M3.keys():
            print('Part2', round+1)
            break
        else:
            M = M3


    if part == 1:
        ep = M.keys()
        rs = [r for r,c in ep]
        cs = [c for r,c in ep]
        tot = (max(rs)-min(rs)+1) * (max(cs)-min(cs)+1)
        print('part1', tot - len(ep))