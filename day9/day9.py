import numpy as np 
import matplotlib.pyplot as plt

filename = "day9.txt" 
with open(filename) as f:
    data = [line.rstrip() for line in f]
    
rt, rh = np.array([0,0]), np.array([0,0])

rules ={
    # First rart
    (2, 1):(1, 1),  (1, 2):(1, 1),(2, 0):(1, 0),  
    (2, -1):(1, -1),(1, -2):(1, -1), (0, -2):(0, -1),
    (-1, -2):(-1,-1), (-2, -1):(-1, -1), (-2, 0):(-1, 0),
    (-2, 1):(-1, 1), (-1, 2):(-1, 1), (0, 2):(0, 1),
    # Second part
    (2, 2):(1, 1), (-2, -2):(-1, -1),
    (-2, 2):(-1, 1), (2, -2):(1, -1)}

direction = {
    "R":(0,1), "L":(0,-1), "U":(1,0), "D":(-1,0)}

tail = set([tuple(rt)])
rope = np.full((10,2), [0,0])
tail_2 = set([tuple(rope[9])])
for move in data:
    move = move.split()
    dir, spaces = move[0], int(move[1])
    for _ in range(1, spaces+1):
        op = direction[dir]
        rh += np.array(op)
        rope[0] += np.array(op)
        dif = tuple(rh -rt)
        rt += np.array(rules.get(dif,(0,0)))
        tail.add(tuple(rt))
        for i in range(1, len(rope)):
            dif = tuple(rope[i-1]-rope[i])
            rope[i] += np.array(rules.get(dif, (0,0)))
        tail_2.add(tuple(rope[9]))
        
print(f"First section = {len(tail)}")
print(f"Second section = {len(tail_2)}")