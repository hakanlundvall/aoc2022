data = [ x.strip('\n') for x in open("i8.txt").readlines() ]
# data = [ x.strip('\n') for x in open("t8.txt").readlines() ]

from collections import defaultdict

m = defaultdict(int)

w = len(data[0])
h = len(data)

for y, r in enumerate(data):
    for x, t in enumerate(r):
        m[(x,y)] = int(t)

count = 0
for x in range(w):
    for y in range(h):
        hidden = 0
        if x in [0,w-1] or y in [0, h-1]:
            count += 1
            continue
        # print(x,y)
        for xx in range(x+1,w):
            if m[(xx,y)] >= m[(x,y)]:
                hidden += 1
                break
        for xx in range(0,x):
            if m[(xx,y)] >= m[(x,y)]:
                hidden += 1
                break
        for yy in range(y+1,h):
            if m[(x,yy)] >= m[(x,y)]:
                hidden += 1
                break
        for yy in range(0,y):
            if m[(x,yy)] >= m[(x,y)]:
                hidden += 1
                break
        if hidden < 4:
            # print(x,y,m[(x,y)],'vis')
            count += 1
        else:
            # print(x,y,m[(x,y)],'inv')
            pass

print(count)
s = defaultdict(int)
for x in range(1,w-1):
    for y in range(1,h-1):
        seeing = [0,0,0,0]
        for xx in range(x+1,w):
            seeing[0] += 1
            if m[(xx,y)] >= m[(x,y)]:
                break
        for xx in range(x-1,-1, -1):
            seeing[1] += 1
            if m[(xx,y)] >= m[(x,y)]:
                break
        for yy in range(y+1,h):
            seeing[2] += 1
            if m[(x,yy)] >= m[(x,y)]:
                break
        for yy in range(y-1,-1,-1):
            seeing[3] += 1
            if m[(x,yy)] >= m[(x,y)]:
                break
        s2 = 1
        for p in seeing:
            s2 *= p
        s[(x,y)] = s2

print(max([ b for a,b in s.items()]))

