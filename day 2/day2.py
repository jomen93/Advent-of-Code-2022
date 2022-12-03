import numpy as np
filename = "day2.txt"

with open(filename) as f:
    lines = f.readlines()

# Matrix Rules
M = np.zeros((3,3))
M[0,0] = 3; M[0,1] = 6; M[0,2] = 0 
M[1,0] = 0; M[1,1] = 3; M[1,2] = 6 
M[2,0] = 6; M[2,1] = 0; M[2,2] = 3 
mapping = {
    "A":0, "B":1, "C":2, "X":0, "Y":1, "Z":2
}
election = {
    "X":1, "Y":2, "Z":3
}
condition ={
    "X":0, "Y":3, "Z":6
}
election_2 = {
    0:"X", 1:"Y", 2:"Z"
}
score = 0
score2 = 0
for r in lines:
    r = r.split()
    j1,j2 = mapping[r[0]], mapping[r[1]]
    index = M[j1].tolist().index(condition[r[1]])
    j22 = mapping[election_2[index]] 
    j2_election = election[r[1]]
    score += M[j1,j2] + j2_election
    score2 += M[j1,j22] + election[election_2[index]]

    
print(f"Score first section = {score:,.0f}")
print(f"Score second section = {score2:,.0f}")

