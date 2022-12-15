data = [x.strip('\n') for x in open("i11.txt").readlines()]
data = [ x.strip('\n') for x in open("t11.txt").readlines() ]

monkeys = []
monkey = []
count = 0
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
    elif l.strip().startswith('If true'):
        tru = int(l.strip().split(' ')[-1].strip())
    elif l.strip().startswith('If false'):
        fls = int(l.strip().split(' ')[-1].strip())
        monkeys.append([items,op,t,tru,fls,0])
    else:
        assert False

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
            new = eval(op)
            if new % t == 0:
                monkeys[tru][0].append(new)
            else:
                monkeys[fls][0].append(new)
        monkeys[i][0] = []
        monkeys[i][5] += count

l = sorted([x[-1] for x in monkeys])[-2:]
print(l[0]*l[1])
        