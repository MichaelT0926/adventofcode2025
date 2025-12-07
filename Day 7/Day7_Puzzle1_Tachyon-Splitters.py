import numpy as np
import time
print(np.__version__)

file = open('input')
tachyon_input = file.read()

tach_map = tachyon_input.split('\n')

#Initial set up of firing the beam/puts the first '|' into the map
start_index = tach_map[0].index('S')
temp = list(tach_map[1])
temp[start_index] = '|'
tach_map[1] = ''.join(temp)

total_splits = 0

for line in range(2,len(tach_map[2:])):
    #Use NumPy to grab a list of indices where a beam exists in the prev line
    beam_indices = np.where(np.array(list(tach_map[line-1])) == '|')[0]

    break_down_current_line = list(tach_map[line])

    #Logic for extending the beam
    for beam_index in beam_indices:
        if break_down_current_line[beam_index] == '.':
            break_down_current_line[beam_index] = '|'
        elif break_down_current_line[beam_index] == '^':
            total_splits += 1
            break_down_current_line[beam_index-1] = '|'
            break_down_current_line[beam_index+1] = '|'
    tach_map[line] = ''.join(break_down_current_line)

print(total_splits)
