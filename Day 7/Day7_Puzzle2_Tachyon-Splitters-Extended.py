import numpy as np

file = open('input')
tachyon_input = file.read()

tach_map = tachyon_input.split('\n')

#Weight map to track number of timelines
weight_map = [0] * len(tach_map[0])

'''Weight Map Logic
The weight map will track how many timelines touch each index, adding the weights together when 2 timelines intersect on an index.
The weight will be removed from an index when the beam splits as that weight has been transferred to 2 different indices.
'''

#Initial set up of firing the beam/puts the first '|' into the map and starts the weight map tracking
start_index = tach_map[0].index('S')
temp = list(tach_map[1])
temp[start_index] = '|'
tach_map[1] = ''.join(temp)
weight_map[start_index] = 1

for line in range(2,len(tach_map[2:])):
    #Use NumPy to grab a list of indices where a beam exists in the prev line
    beam_indices = np.where(np.array(list(tach_map[line-1])) == '|')[0]

    break_down_current_line = list(tach_map[line])

    #Logic for extending the beam and tracking weight map
    for beam_index in beam_indices:
        if break_down_current_line[beam_index] == '.':
            break_down_current_line[beam_index] = '|'
        elif break_down_current_line[beam_index] == '^':
            break_down_current_line[beam_index-1] = '|'
            weight_map[beam_index-1] += weight_map[beam_index]
            break_down_current_line[beam_index+1] = '|'
            weight_map[beam_index+1] += weight_map[beam_index]
            weight_map[beam_index] = 0
    tach_map[line] = ''.join(break_down_current_line)

print(sum(weight_map))
