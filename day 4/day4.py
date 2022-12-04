import numpy as np
filename = "day4.txt"

with open(filename) as f:
    lines = f.readlines()

score1 = 0
score2 = 0
for pair in lines:    
    value = pair.split(",")
    p1,p2 = value
    p11, p12 = p1.split("-"); p21, p22 = p2.split("-")
    v1 = np.arange(int(p11), int(p12)+1)
    v2 = np.arange(int(p21), int(p22)+1)
    if len(v1) > len(v2):
        vmax = v1; vmin = v2
    else:
        vmin = v1; vmax = v2
    
    score1 += all(item in vmax for item in vmin)
    score2 += any(item in vmax for item in vmin)
    
print(f"Score of the fist section = {score1}")
print(f"Score of the second section = {score2}")

