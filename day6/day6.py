filename = "day6.txt"

with open(filename) as f:
    lines = f.readlines()[0]
    
len_pack_1 = 4; len_pack_2 = 14

for i in range(len(lines)):
    p1 = lines[i:i+len_pack_1]; np1 = set(p1)
    if len(p1) == len(np1):
        print(f"First part = {i+len_pack_1}")
        break
    
for i in range(len(lines)):
    p2 = lines[i:i+len_pack_2]; np2 = set(p2)    
    if len(p2) == len(np2):
        print(f"Second part {i+len_pack_2}")
        break