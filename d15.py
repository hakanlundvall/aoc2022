data = [x.strip('\n') for x in open("i15.txt").readlines()]
# data = [ x.strip('\n') for x in open("t15.txt").readlines() ]

d = []
r = set()
for l in data:
    a,b = l.split(':')
    aa = a.split(" ")
    x = int(aa[2].strip("xy=,"))    
    y = int(aa[3].strip("xy=,"))
    # print(aa, x, y)    
    bb = b.split(" ")
    x2 = int(bb[5].strip("xy=,"))    
    y2 = int(bb[6].strip("xy=,"))
    # print(bb, x2, y2)
    d.append([(x,y), (x2,y2)])
# print(d)

y = 2000000

for s,b in d:
    dy = abs(b[1]-s[1])
    dx = abs(b[0]-s[0])
    ddy = abs(s[1] - y)
    dx = dx + dy - ddy
    for x in range(s[0]-dx, s[0]+dx+1):
        if b[1] == y and b[0] == x:
            continue
        r.add(x)

print(len(r))