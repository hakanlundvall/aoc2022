data = [x.strip('\n') for x in open("i25.txt").readlines()]
# data = [x.strip('\n') for x in open("t25.txt").readlines()]

A = {
    '=' : -2,
    '-' : -1,
    '0' : 0,
    '1' : 1,
    '2' : 2,
}

B = {
    -2: '=',
    -1: '-',
    0: '0',
    1: '1',
    2: '2',
}

def fromSNAFU(x):
    y = 0
    for a,b in enumerate(x):
        y *= 5
        y += A[b]
    return y

s = 0
for l in data:
    s += fromSNAFU(l)


def toSNAFU(x):
    l = []
    reminder = 0
    while x > 0:
        a = x // 5
        b = (x % 5) + reminder 
        if b > 2:
            reminder = 1
            b -= 5
        else: 
            reminder = 0
        l.append(b)
        x = a
    if reminder > 0:
        l.append(reminder)
    r =  ''.join(map(lambda x: B[x],reversed(l)))
    return r

print(toSNAFU(s))

