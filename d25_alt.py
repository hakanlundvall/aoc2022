from itertools import zip_longest, accumulate

data = [x.strip('\n') for x in open("i25.txt").readlines()]

def SNAFU_to_number(x: str) -> int:
    A = {'=': -2, '-': -1, '0': 0, '1': 1, '2': 2, }
    return A[x]

def number_to_SNAFU(x: int):
    B = {-2: '=',  -1: '-',  0: '0',  1: '1',  2: '2', }
    return B[x]

def addSNAFU(a: str, b: str) -> str:
    z = zip_longest(map(SNAFU_to_number, reversed(a)),
                    map(SNAFU_to_number, reversed(b)), fillvalue=0)
    result = []
    carry = 0
    for a, b in z:
        c = a + b + carry
        carry, c = divmod(c+2,5)
        result.append(c-2)
    if carry != 0:
        result.append(carry)
    return ''.join(list(map(number_to_SNAFU, reversed(result))))

print(list(accumulate(data, func=addSNAFU, initial=""))[-1])
