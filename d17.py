from copy import deepcopy

data = [x.strip('\n') for x in open("i17.txt").readlines()]
# data = [x.strip('\n') for x in open("t17.txt").readlines()]


p1 = list([(0, 0), (1, 0), (2, 0), (3, 0),])
p2 = list([(0, -1), (1, -1), (2, -1), (1, 0), (1, -2)])
p3 = list([(0, 0), (1, 0), (2, 0), (2, -1), (2, -2)])
p4 = list([(0, 0), (0, -1), (0, -2), (0, -3)])
p5 = list([(0, 0), (0, -1), (1, 0), (1, -1),])
rocks = [p1, p2, p3, p4, p5]


def checkcollision(m, rock):
    if (max([x for x, y in rock]) <= 4) and (min([x for x, y in rock]) > -3) and (max([y for x, y in rock]) < 0):
        for p in rock:
            if p in m:
                return False
        return True
    return False


def drawcave(m, rock):
    print()
    lines = ["+-------+"]
    for y in range(-1, -10, -1):
        line = "|"
        for x in range(-2, 5):
            if (x, y) in m:
                line += "#"
            elif rock and (x, y) in rock:
                line += "@"
            else:
                line += "."
        line += "|"

        lines.append(line)
    for l in reversed(lines):
        print(l)
    print()


def part(part):
    m = set()
    top = 0
    ii = 0
    visited = dict()

    MAX = 2022 if part == 1 else 1000000000000
    count = -1
    skipped = False
    while True:
        count += 1
        if count >= MAX:
            break
        if not skipped:
            key = []
            for yy in range(top, top+100):
                for xx in range(-2, 5):
                    key.append(1 if (xx, yy) in m else 0)
            key.append(count % 5)
            key.append(ii)
            key = tuple(key)
            if key in visited:
                visited[key].append((count, top))
                x, xt = zip(*visited[key])
                c = [a-b for a, b in zip(x, x[1:])]
                if (len(c) > 1) and (c[-1] == c[-2]):
                    count_period = x[-1] - x[-2]
                    top_period = xt[-2] - xt[-1]

                    remaining = MAX - count
                    skips = remaining//count_period
                    count += skips*count_period
                    new_top = top - skips*top_period
                    for y in range(top, top+top_period):
                        for x in range(-2, 5):
                            if (x, y) in m:
                                m.add((x, y+(new_top-top)))
                    top = new_top
                    skipped = True
            else:
                visited[key] = [(count, top)]

        fallingrock = deepcopy(rocks[count % 5])
        i = 4-top
        fallingrock = [(x, y - i) for x, y in fallingrock]
        # drawcave(m, fallingrock)

        while True:
            w = data[0][ii]
            ii += 1
            if ii >= len(data[0]):
                ii = 0

            d = 1 if w == '>' else -1
            nextfallingrock = [(x+d, y) for x, y in fallingrock]
            if checkcollision(m, nextfallingrock):
                fallingrock = nextfallingrock

            nextfallingrock = [(x, y+1) for x, y in fallingrock]
            if checkcollision(m, nextfallingrock):
                fallingrock = nextfallingrock
            else:
                for p in fallingrock:
                    m.add(p)
                    x, y = p
                    top = min(top, p[1])
                break

    print(-top)


part(1)
part(2)
