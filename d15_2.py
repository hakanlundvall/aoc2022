data = [x.strip('\n') for x in open("i15.txt").readlines()]
# data = [ x.strip('\n') for x in open("t15.txt").readlines() ]
bcn = []
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
    bcn.append([x2,y2])
# print(d)

from copy import deepcopy

def checkrow(r, n):
    if len(r) == 0:
        return [n]

    head = r[0:]
    tail = r[0:]
    for i, a in enumerate(r):
        if a[1] >= n[0]:
            head = r[:i]
            break
    
    for j in range(len(r)-1, i-1, -1):
        a = r[j]
        if a[0] <= n[1]:
            tail = r[j+1:]
            break

    f = r[i]
    g = r[j]
    if f[1] >= n[0] and n[0] > f[0]:
        n[0] = f[0]
    if g[0] <= n[1] and n[1] < g[1]:
        n[1] = g[1]
    return head + [n] + tail
        
count = 0
r = [[]  for x in range(4000000)]
for s,b in d:
    count +=1
    print(count)
    dy = abs(b[1]-s[1])
    dx = abs(b[0]-s[0])
    ys = max(0, s[1]-(dx+dy))
    ye = min(4000000,s[1]+(dx+dy)+1)
    for y in range(ys, ye):
        ddy = abs(s[1] - y)
        dx2 = dx + dy - ddy
        sx1 = max(0,s[0]-dx2)
        sx2 = min(4000000, s[0]+dx2)
        if b[1] == y:
            if b[0]==sx1:
                sx1+=1
            elif b[0]==sx2:
                sx2-=1
        r[y] = checkrow(r[y], [sx1,sx2])

res = list(filter(lambda y : len(y[1])>1, enumerate(r)))
for y,x in res:
    xx = (x[0][1]+1)
    if [xx,y] in bcn:
        continue
    print(xx,y,y+4000000*xx )
