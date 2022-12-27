filename = "day10.txt" 
with open(filename) as f:
    data = [line.rstrip() for line in f]

inst = [[l[0], int(l[1])] if len(l:=v.split()) == 2 else [v, 0] for i, v in enumerate(data)]
check = [20, 60, 100, 140, 180, 220]
signal = 0; x = 1; cycle = 1

for cmd, num in inst:
    if cmd == "noop":
        if cycle in check:
            signal += cycle*x
        cycle += 1
    elif cmd == "addx":
        for _ in range(2):
            if cycle in check:
                signal += cycle*x
            cycle +=1
        x += num
print(f"Fisrt part: {signal}")

i = 0; cmd = None ;arg = None
remain = 0; x = 1

rows = [[] for _ in range(6)]
for cycle in range(240):
    r = cycle // 40; c = cycle % 40
    rows[r].append("#" if abs(c-x) <= 1 else ".")
    
    if cmd is None:
        cmd, arg = inst[i]
        remain = 2 if cmd == "addx" else 1
        i += 1
            
    if cmd == "noop":
        pass
    
    elif cmd == "addx":
        if remain == 1:
            x += arg

    remain -= 1
    if remain == 0:
        cmd = None
print("Second part: ")
print(*("".join(row) for row in rows), sep="\n")
