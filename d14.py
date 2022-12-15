data = [x.strip('\n') for x in open("i14.txt").readlines()]
# data = [ x.strip('\n') for x in open("t14.txt").readlines() ]

m = dict()

def print_map(m):
    keys = m.keys()
    a = list(zip(*map(sorted,(zip(*keys)))))
    x1, y1 = a[0]
    x2, y2 = a[-1]
    for y in range(y1, y2+1):
        for x in range(x1, x2+1):
            print(m.get((x,y), " "), end="")
        print()

for l in data:
    path = [list(map(int,p.strip().split(','))) for p in l.split('->')]
    for p1, p2 in zip(path, path[1:]):
        xs,ys = list(map(sorted, zip(p1,p2)))
        for x in range(xs[0],xs[1]+1):
            for y in range(ys[0],ys[1]+1):
                m[(x,y)] = "#"

m[(500,0)]='+'

# print_map(m)

keys = m.keys()
a = list(zip(*map(sorted,(zip(*keys)))))
x1, y1 = a[0]
x2, y2 = a[-1]

count = -1
done = False
part1 = None
while not done:
    at_rest = False
    sand = (500,0)
    count += 1
    while not at_rest:
        x,y = sand
        at_rest = True
        for dx,dy in [(0,1), (-1,1),(1,1)]:
            tp = (x + dx,  y + dy)
            if (tp[1] < (y2+2)) and (tp not in m or m[tp] == ' '):
                sand = tp
                if sand[1] > y2 and not part1:
                    part1 = count
                    # print(count)
                at_rest = False
                break
    m[sand] = "o"
    # print_map(m)
    if sand[1] == 0:
        done = True

# print_map(m)
print(part1)
print(count+1)
        