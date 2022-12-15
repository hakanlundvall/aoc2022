f = open("i2.txt")
rounds = [ r.split() for r in f.readlines()]
# print(rounds)

# t = """A Y
# B X
# C Z"""
# rounds = [ r.split() for r in t.split('\n')]
# print(rounds)

def calc(r):
    a1 ,b1 = r
    a = ord(a1)-ord('A')
    b = ord(b1)-ord('X')
    s = b+1 + 3 * ((1+b-a)%3)
    return s

def calc_p2(r):
    a1 ,b1 = r
    a = ord(a1)-ord('A')
    c = ord(b1)-ord('X')
    b = (a + c - 1) % 3
    s = b+1 + 3 * ((1+b-a)%3)
    return s

res = [ calc(r) for r in rounds ]
print(sum(res))

res2 = [ calc_p2(r) for r in rounds ]
print(sum(res2))
