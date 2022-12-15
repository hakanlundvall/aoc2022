data = [x.strip('\n') for x in open("i10.txt").readlines()]
# data = [ x.strip('\n') for x in open("t10.txt").readlines() ]


def checkpix(c, x):
    pos = (c-1) % 40
    if pos in range(x-1, x+2):
        return "#" + ("\n" if pos == 39 else "")
    else:
        return " " + ("\n" if pos == 39 else "")

cycle = 1
x = 1
res = 0
screen = ""
for l in data:
    op, *n = l.split()
    if op == 'noop':
        if (cycle - 20) % 40 == 0 or (cycle - 20) % 40 == 0:
            # print(cycle, x, cycle*x)
            res += cycle*x
        screen += checkpix(cycle, x)
        cycle +=1
    elif op == 'addx':
        if (cycle - 20) % 40 == 0 or (cycle - 20) % 40 == 0:
            # print(cycle, x, cycle*x)
            res += cycle*x
        screen += checkpix(cycle, x)
        cycle +=1
        if (cycle - 20) % 40 == 0 or (cycle - 20) % 40 == 0:
            # print(cycle, x, cycle*x)
            res += cycle*x
        screen += checkpix(cycle, x)
        cycle +=1
        x += int(n[0])
    else:
        assert False        
    
print(res)
print(screen)