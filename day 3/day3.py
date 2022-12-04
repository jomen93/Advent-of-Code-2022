import string

filename = "day3.txt"

with open(filename) as f:
    lines = f.readlines()

alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)

# First Part
score1 = 0
for s in lines:
    intersection = list(set(s[:len(s)//2]).intersection(s[len(s)//2:]))[0]
    score1 += alphabet.index(intersection) + 1

print(f"Score of first part {score1:,.0f}")

# Second part
n_int = 3; score2 = 0
n_group = len(lines)//n_int
for group in range(n_group):
    g = lines[group*n_int:(group+1)*n_int]
    sg1, sg2, sg3 = set(g[0]),set(g[1]),set(g[2])
    value = list(sg1.intersection(sg2, sg3))
    if "\n" in value:
        value.remove("\n")
    score2 += alphabet.index(value[0]) + 1

print(f"Score of the second part {score2:,.0f}")
    
