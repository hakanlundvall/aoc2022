def check(r1,r2):
    if r1[0] >= r2[0]:
        if r1[1] <= r2[1]:
            return True
    if r1[0] <= r2[0]:    
        if r1[1] >= r2[1]:
            return True
    return False


def overlap(r1,r2):
    if r1[0] > r2[1]:
        return False
    if r2[0] > r1[1]:
        return False
    return True


sum = 0
sum2 = 0
for l in open("i4.txt"):
    p1,p2 = l.strip().split(',')
    r1 = [int(x) for x in p1.split('-')]
    r2 = [int(x) for x in p2.split('-')]
    # print(r1,r2)
    if check(r1,r2):
        assert check(r2,r1)
        sum += 1

    if overlap(r1,r2):
        assert overlap(r2,r1)
        sum2 += 1

print(sum, sum2)