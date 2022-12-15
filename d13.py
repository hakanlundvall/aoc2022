data = [x.strip('\n') for x in open("i13.txt").readlines()]
# data = [ x.strip('\n') for x in open("t13.txt").readlines() ]

parts = [x.split('_') for x in '_'.join(data).split('__')]


def compare(l,r):
    if type(l) == list and type(r) == list:
        for ll,rr in zip(l,r):
            c = compare(ll,rr)
            if c > 0:
                return 1
            if c < 0:
                return -1
        if len(l) < len(r):
            return -1
        elif len(l) > len(r):
            return 1
        else:
            return 0

    elif type(l) == list and not type(r) == list:
         return compare(l,[r])
    elif not type(l) == list and type(r) == list:
         return compare([l],r)
    else:
        return -1 if l < r else (0 if l == r else 1)
         

count = 0
sum = 0
lll = []
for l, r in parts:
    ll = eval(l)
    rr = eval(r)
    lll.append(ll)
    lll.append(rr)
    count += 1
    if compare(ll,rr) < 0:
        sum += count

print(sum)

sortedlist = []

lll += [[[2]], [[6]]]
while lll:
    l = lll.pop()
    for i, r in enumerate(sortedlist):
        if compare(l, r) < 1:
            sortedlist= sortedlist[:i] + [l] + sortedlist[i:]
            break
    else:
        sortedlist.append(l)

d1 = 0
d2 = 0
count = 0
for l in sortedlist:
    count += 1
    print(l)
    if l == [[2]]:
        d1 = count
    elif l == [[6]]:
        d2 = count

print(d1*d2)