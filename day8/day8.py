import numpy as np

filename = "day8.txt" 
with open(filename) as f:
    data = [line.rstrip() for line in f]

grid = []
for i in range(len(data)):
    grid.append([int(s) for s in data[i]])

grid = np.array(grid)
count_1 = np.zeros_like(grid);count_2 = np.zeros_like(grid)
count_1[0] = 1; count_1[-1] = 1
count_1[:,0] = 1; count_1[:,-1] = 1

def score(select, choose):
    b = list(select >= choose)
    return b.index(True) + 1 if True in b else len(b)

for i in range(1, grid.shape[0]-1):
    for j in range(1, grid.shape[1]-1):
        
        choose = grid[i,j]
        file = grid[i]; column = grid[:,j]
        # first part
        left = all(np.where(file[:j] < choose, True, False))
        right = all(np.where(file[j+1:] < choose, True, False))
        up = all(np.where(column[:i] < choose, True, False))
        down = all(np.where(column[i+1:] < choose, True, False))
        
        if any([left, right, up, down]):
            count_1[i,j] = 1
        
        # second part
        left_score = score(file[:j][::-1],choose)
        right_score = score(file[j+1:], choose)
        up_score = score(column[:i][::-1],choose)
        down_score = score(column[i+1:],choose)
        
        count_2[i][j] = left_score * right_score * up_score * down_score

print(f"fisrt part {np.count_nonzero(count_1)}")
print(f"second part {count_2.max()}")