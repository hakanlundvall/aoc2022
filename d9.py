data = [x.strip('\n') for x in open("i9.txt").readlines()]
# data = [ x.strip('\n') for x in open("t9.txt").readlines() ]


def part(p):
    s = (0, 0)
    r = [s for i in range(10 if p == 2 else 2)]
    v = set()

    def m(h, t):
        hx, hy = h
        tx, ty = t
        if ((hx - tx) > 1) or ((hx - tx) == 1 and abs(hy-ty) > 1):
            dx = 1
        elif ((hx - tx) < -1) or ((hx - tx) == -1 and abs(hy-ty) > 1):
            dx = -1
        else:
            dx = 0
        if ((hy - ty) > 1) or ((hy - ty) == 1 and abs(hx-tx) > 1):
            dy = 1
        elif ((hy - ty) < -1) or ((hy - ty) == -1 and abs(hx-tx) > 1):
            dy = -1
        else:
            dy = 0

        return (tx + dx, ty + dy)

    for line in data:
        d, n = line.split()
        for i in range(int(n)):
            h = r[0]
            if d == 'U':
                h = (h[0], h[1]-1)
            elif d == 'D':
                h = (h[0], h[1]+1)
            elif d == 'L':
                h = (h[0]-1, h[1])
            elif d == 'R':
                h = (h[0]+1, h[1])
            else:
                assert False
            r[0] = h
            for i in range(len(r)-1):
                k = r[i+1]
                h = r[i]
                t = m(h, k)
                r[i+1] = t
            v.add(r[-1])
    print(len(v))


part(1)
part(2)
