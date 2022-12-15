f = open("i1.txt")
elves = []
elf = 0
for l in f.readlines():
    if l.strip() == "":
        elves.append(elf)
        elf = 0
    else:
        elf += int(l.strip())


print(max(elves))
print(sum(sorted(elves)[-3:]))
