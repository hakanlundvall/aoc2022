data = [ x.strip('\n') for x in open("i7.txt").readlines() ]
# data = [ x.strip('\n') for x in open("t7.txt").readlines() ]

stack = []
cwd = []
ls = []
sss = 0
lss = 0
from collections import defaultdict
d = defaultdict(int)
for l in data:
    first, second, *parts = l.split()
    if first == '$':
        print(cwd, ls)
        ss = sum([ int(s[0]) for s in filter(lambda x: x[0].isnumeric(), ls)])
        d['/'.join(cwd)] += ss
        if second == 'cd':
            ls = []
            if parts[0] == "/":
                cwd = []
            elif parts[0] == "..":
                x = d['/'.join(cwd)]
                cwd = cwd[:-1]
                d['/'.join(cwd)] += x
            else:
                cwd.append(parts[0])
        elif second == 'ls':
            ls = []
            pass
        else:
            assert False
    else:
        ls.append([first, second])
ss = sum([ int(s[0]) for s in filter(lambda x: x[0].isnumeric(), ls)])
d['/'.join(cwd)] += ss


while cwd:
    x = d['/'.join(cwd)]
    cwd = cwd[:-1]
    d['/'.join(cwd)] += x
   
s2 = 0
for cwd,s in d.items():
    print(cwd,s)
    if s <= 100000:
        s2 += s

print(s2)

total = 70000000
need = 30000000
current = d[""]
unused = total - current
print(unused)
freeup = need - unused
print(freeup)
c = []
for cwd,s in d.items():
    if s >= freeup:
        c.append((s, cwd))

print(sorted(c))
