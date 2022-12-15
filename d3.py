f = open("i3.txt")
bags = [ list(r.strip()) for r in f.readlines()]
s = 0
for b in bags:
    l = len(b) // 2
    it = list(set(b[:l]).intersection(set(b[l:])))
    assert len(it) == 1
    it = it[0]
    a = ord(it)
    if a in range(ord('a'),ord('z')+1):
        s += a - ord('a') + 1
    elif a in range(ord('A'),ord('Z')+1):
        s += a - ord('A') + 27
print(s)


s = 0
s2 = 0
for i in range(len(bags)//3):
    s = set(list("abcdefghijklmnopqsrtuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    for b in bags[i*3:i*3+3]:
        s = s.intersection(set(b))
    it = list(s)
    assert len(it) == 1
    a = ord(it[0])
    if a in range(ord('a'),ord('z')+1):
        s2 += a - ord('a') + 1
    elif a in range(ord('A'),ord('Z')+1):
        s2 += a - ord('A') + 27
print(s2)

#         assert len(it) == 1
#         it = it[0]
#         a = ord(it)
#         if a in range(ord('a'),ord('z')+1):
#             s += a - ord('a') + 1
#         elif a in range(ord('A'),ord('Z')+1):
#             s += a - ord('A') + 27
# print(s)