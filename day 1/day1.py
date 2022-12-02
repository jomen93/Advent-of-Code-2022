
filename = "day1.txt"

with open(filename) as f:
    lines = f.readlines()

n_index = [i for i, x in enumerate(lines) if x == "\n"]
N_elfs = len(n_index) + 1
n_index.insert(0,0); n_index.insert(len(lines)+1,len(lines)+1)

# Fisrt part
elfs = []
for i in range(0, N_elfs):
    i_elf = lines[n_index[i]+1:n_index[i+1]]
    i_elf = [int(i) for i in i_elf]
    elfs.append(sum(i_elf))
    
print(f"Total Calories = {max(elfs)}, Elf -> {elfs.index(max(elfs))}")

# Second Part
sum_3best = sum(sorted(elfs)[-3:])
print(f"sum calories of the 3 best {sum_3best}")