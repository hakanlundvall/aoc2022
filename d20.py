from copy import deepcopy

data = [x.strip('\n') for x in open("i20.txt").readlines()]
# data = [x.strip('\n') for x in open("t20.txt").readlines()]


class unique:
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


msg = [unique(int(x)) for x in data]
msg2 = [unique(int(x)*811589153) for x in data]
orig = [x for x in msg]
orig2 = [x for x in msg2]


def mix(l, x, i):
    lm = len(l)
    if x.value == 0:
        return l
    rotm = l[i:] + l[:i]

    pos = x.value % (lm-1)
    rotm = rotm[1:]
    rotm.insert(pos, x)
    l = rotm[-i:] + rotm[:-i]

    return l


for x in orig:
    i = msg.index(x)
    msg = mix(msg, x, i)

for i, x in enumerate(msg):
    if x.value == 0:
        index = i

lm = len(msg)
print(msg[(index+1000) % lm].value + msg[(index+2000) %
      lm].value + msg[(index+3000) % lm].value)


for t in range(10):
    for x in orig2:
        i = msg2.index(x)
        msg2 = mix(msg2, x, i)

for i, x in enumerate(msg2):
    if x.value == 0:
        index = i

lm = len(msg2)
print(msg2[(index+1000) % lm].value + msg2[(index+2000) %
      lm].value + msg2[(index+3000) % lm].value)
