data = [x.strip('\n') for x in open("i11.txt").readlines()]
# data = [ x.strip('\n') for x in open("t11.txt").readlines() ]

monkeys = []
monkey = []
count = 0

mm = 1

for l in data:
    if l.strip() == "":
        count += 1
        continue
    if l.startswith('Monkey'):
        pass
    elif l.strip().startswith('Starting'):
        items = [int(x) for x in l.strip().split(':')[-1].strip().split(',')]
    elif l.strip().startswith('Operation'):
        op = l.strip().split('=')[-1].strip()
    elif l.strip().startswith('Test'):
        t = int(l.strip().split(' ')[-1].strip())
        mm *= t
    elif l.strip().startswith('If true'):
        tru = int(l.strip().split(' ')[-1].strip())
    elif l.strip().startswith('If false'):
        fls = int(l.strip().split(' ')[-1].strip())
        monkeys.append([items,op,t,tru,fls,0])
    else:
        assert False


def op0(old):
    return old * 3
def op1(old):
    return old + 3
def op2(old):
    return old + 5
def op3(old):
    return old * 19
def op4(old):
    return old + 1
def op5(old):
    return old + 2
def op6(old):
    return old * old
def op7(old):
    return old + 8

# monkeys[0][1] = op0
# monkeys[1][1] = op1
# monkeys[2][1] = op2
# monkeys[3][1] = op3
# monkeys[4][1] = op4
# monkeys[5][1] = op5
# monkeys[6][1] = op6
# monkeys[7][1] = op7

for round in range(10000):
    print("Round", round)
    # l = [x[-1] for x in monkeys]
    # if round in [1,20,1000]:
    #     print(l)
    for i in range(len(monkeys)):
        count = 0
        items,op,t,tru,fls,_ = monkeys[i]
        new_items = []
        for k in items:
            old = k
            count += 1
            # new = eval(op) // 3
            new = eval(op) % mm
            # new = op(old)
            if new % t == 0:
                monkeys[tru][0].append(new)
            else:
                monkeys[fls][0].append(new)
        monkeys[i][0] = []
        monkeys[i][5] += count

l = sorted([x[-1] for x in monkeys])[-2:]
print(l[0]*l[1])
        