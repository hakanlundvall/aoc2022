from copy import deepcopy

data = [x.strip('\n') for x in open("i21.txt").readlines()]
# data = [x.strip('\n') for x in open("t21.txt").readlines()]

M=dict()

for d in data:
    m, r = d.split(':')
    M[m] = r.strip()

root = M['root']

def calc(m_str):
    m = M[m_str]
    if isinstance(m,int):
        return m
    if m.isnumeric():
        return int(m)
    else:
        a, op, b = m.split(' ')
        if op == '+':
            return calc(a) + calc(b)
        elif op == '*':
            return calc(a) * calc(b)
        elif op == '-':
            return calc(a) - calc(b)
        elif op == '/':
            return calc(a) // calc(b)
print(calc('root'))

M['humn'] = 'x'

def evaluate(m_str):
    m = M[m_str]
    if m.isnumeric():
        return m_str, []
    elif m == 'x':
        return 'x', [(m_str, 'x')]
    else:
        a, op, b = m.split(' ')
        aop = []
        bop = []
        a1, aop = evaluate(a)
        b1, bop = evaluate(b)
        
        assert (not aop) or (not bop)
        if aop:
            ops = [(op, 'l')]
        elif bop:
            ops = [(op, 'r')]
        else:
            ops = []
        if op == '+':
            return f"({a1} + {b1})", aop + bop + ops
        elif op == '*':
            return f"({a1} * {b1})", aop + bop + ops
        elif op == '-':
            return f"({a1} - {b1})", aop + bop + ops
        elif op == '/':
            return f"({a1} / {b1})", aop + bop + ops


a, op, b = M['root'].split(' ')
N = dict()
exprl, opsa = evaluate(a)
exprr, opsb = evaluate(b)
if opsa:
    l = a
    r = b
    ops = opsa
else:
    l = b
    r = a
    ops = opsb


count = 0
for op, d in reversed(ops):
    count += 1
    ml = M[l]
    mr = M[r]
    if ml == 'x':
        M['x'] = mr
        continue
    mll , _ , mlr = ml.split(' ')
    if op == '/':
        if d == 'l':
            M[f"v{count}"] = f"{r} * {mlr}"
            r = f"v{count}"
            l = mll
        elif d == 'r':
            M[f"v{count}"] = f"{mll} / {r}"
            r = f"v{count}"
            l = mlr
        else:
            assert False
    if op == '-':
        if d == 'l':
            M[f"v{count}"] = f"{r} + {mlr}"
            r = f"v{count}"
            l = mll
        elif d == 'r':
            M[f"v{count}"] = f"{mll} - {r}"
            r = f"v{count}"
            l = mlr
        else:
            assert False
    elif op == '+':
        if d == 'l':
            M[f"v{count}"] = f"{r} - {mlr}"
            r = f"v{count}"
            l = mll
        elif d == 'r':
            M[f"v{count}"] = f"{r} - {mll}"
            r = f"v{count}"
            l = mlr
        else:
            assert False
    elif op == '*':
        if d == 'l':
            M[f"v{count}"] = f"{r} / {mlr}"
            r = f"v{count}"
            l = mll
        elif d == 'r':
            M[f"v{count}"] = f"{r} / {mll}"
            r = f"v{count}"
            l = mlr
        else:
            assert False
    
print(calc('x'))