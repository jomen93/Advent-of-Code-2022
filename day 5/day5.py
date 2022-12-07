import numpy as np
filename = "day5.txt"

with open(filename) as f:
    lines = f.readlines()

files = 9; element_size = 4; highest_row = 8
part = "first"
stack = []

for row in lines[:highest_row]:
    stack.append([row[i*element_size:(i+1)*element_size] for i in range(files)])
    
stack = np.array(stack)
stack[:,-1] = np.char.replace(stack[:,-1], "\n", " "*2)
num_empty = ((stack==" "*4)).sum(); max_crack = (stack.shape[0]*stack.shape[1]) - num_empty
max_height_stack = np.array([[" "*element_size]*files]*max_crack)
stack = np.append(max_height_stack, stack, axis=0)
moves = lines[highest_row+2:]

for i in range(len(moves)):
    move = moves[i]
    amount, init_stack, end_stack = [int(s) for s in str.split(move) if s.isdigit()]
    init_stack -= 1; end_stack -= 1 
    init_stack_lp = [("[" in x) & ("]"in x) for x in stack[:,init_stack]]
    end_stack_lp = [("[" in x) & ("]" in x) for x in stack[:,end_stack]]

    if any(init_stack_lp) == False:
        init_stack_lp = 0
    else:
        init_stack_lp = init_stack_lp.index(True)    
    if any(end_stack_lp) == False:
        end_stack_lp = 0
        if part == "first":
            stack[:, end_stack][end_stack_lp-amount:] = stack[:, init_stack][init_stack_lp:init_stack_lp+amount][::-1]
        else:
            stack[:, end_stack][end_stack_lp-amount:] = stack[:, init_stack][init_stack_lp:init_stack_lp+amount]
    else:
        end_stack_lp = end_stack_lp.index(True)
        if part == "first":
            stack[:, end_stack][end_stack_lp-amount:end_stack_lp] = stack[:, init_stack][init_stack_lp:init_stack_lp+amount][::-1]
        else:
            stack[:, end_stack][end_stack_lp-amount:end_stack_lp] = stack[:, init_stack][init_stack_lp:init_stack_lp+amount]
    
    stack[:, init_stack][init_stack_lp:init_stack_lp+amount] = [" "*4]*amount
    
print(stack)

