from collections import defaultdict

filename = "day7.txt" 
size_max = 100_000

with open(filename) as f:
    data = [line.rstrip() for line in f]

path = []
total_space = defaultdict(int)
for line in data:
    split = line.split()
    if split[1] == 'ls':
        continue
    elif split[1] == 'cd':
        if split[2] == '..':
            path.pop()
        else:
            total_space[split[2]] += 0
            path.append(split[2])
    elif split[0].isnumeric():
        bytes = int(split[0])
        for i in range(len(path) + 1):
            last = '/'.join(path[:i])
            total_space[last] += bytes

r1 = sum([t for t in total_space.values() if t <= size_max])
print(r1)

total_space = 70_000_000
space_needed = 30_000_000
free_space = total_space - total_space['/']
update_space = space_needed - free_space

r2 = min([t for t in total_space.values() if t >= update_space])
print(r2)

