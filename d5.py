stacklines = []
moves = []
phase = 1
part = 1
# for l in open("t5.txt"):
for l in open("i5_2.txt"):
    if l.strip() == "":
        phase = 2
    elif l.strip()[0] == '1':
        n = int(l.strip().split()[-1])
    elif phase == 1:
        stacklines.append(l.strip('\n'))
    else:
        moves.append(l.strip())

# print(stacklines)
# print(moves)

stacks = [ list() for x in range(n)]
for l in reversed(stacklines):
    for k, i in enumerate(range(1, n*4+1, 4)):
        x = l[i]
        if x != ' ':
            stacks[k].append(x)

# print(stacks)

for m in moves:
    _, c, _, f, _, t = m.split()
    # print(c,f,t)
    popped = []
    if part == 1:
        for i in range(int(c)):
            x = stacks[int(f)-1].pop()
            stacks[int(t)-1].append(x)
    else:
        for i in range(int(c)):
            x = stacks[int(f)-1].pop()
            popped.append(x)
        for i in range(int(c)):
            x = popped.pop()
            stacks[int(t)-1].append(x)

res = [x[-1] for x in stacks]
print(''.join(res))