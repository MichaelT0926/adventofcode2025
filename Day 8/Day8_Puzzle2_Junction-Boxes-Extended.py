import re

import math

from collections import defaultdict

inputStr = open('input').read()

regex_pattern = '\d+'

#Regex to grab sets of 3 numbers (x,y,z)
compos_list = [re.findall(regex_pattern, inputStr)[x:x+3] for x in range(0, len(re.findall(regex_pattern, inputStr)), 3)]

dist_pair_list = []

#Compares each junction box to every other junction box, calculates the straight-line distance and after sorts them by asc distance
for each_index in range(0,len(compos_list)):

    if each_index + 1 > len(compos_list):
        break

    for next_index in range(each_index+1, len(compos_list)):
        xs = [int(compos_list[each_index][0]), int(compos_list[next_index][0])]
        ys = [int(compos_list[each_index][1]), int(compos_list[next_index][1])]
        zs = [int(compos_list[each_index][2]), int(compos_list[next_index][2])]
        dist = math.sqrt(math.pow(xs[0] - xs[1], 2) + math.pow(ys[0] - ys[1], 2) + math.pow(zs[0] - zs[1], 2)*1.0)
        dist_pair_list.append((compos_list[each_index], compos_list[next_index], dist))

sorted_list = sorted(dist_pair_list, key=lambda pair: pair[2])

circuit_list = []

#Combines the xyz of each box into one string for easy comparison
#Unlimited from part 1 as we must complete the full circuit for part 2
for i in range(0,len(sorted_list)):
    circuit_list.append([''.join(sorted_list[i][0]), ''.join(sorted_list[i][1])])


def merge_common(circuit_list):
    #Two sets to track current circuits and coords already visited
    circuits = defaultdict(set)
    visited = set()
    #Initialized at -1 to account for index 0 bringing it up by 1
    combine_index = -1
    for circuit in circuit_list:
        #If statement stops the program when all boxes have been accounted for and prints the product of the final two boxes' x coord
        if len(circuits) < 1000:
            combine_index += 1
        else:
            print(int(sorted_list[combine_index][0][0]) * int(sorted_list[combine_index][1][0]))
            return(None)
        for box in circuit:
            circuits[box].update(circuit)

    def comp(box, circuits = circuits, visited = visited, vis = visited.add):
        #Compares current box with the circuits and visited arrays, updates them as needed
        boxes = set([box])
        next_box = box.pop
        while box:
            if len(boxes) == 0:
                break
            box = next_box()
            vis(box)
            boxes |= circuits[box] - visited
            yield box

    for box in circuits:
        if box not in visited:
            yield sorted(comp(box))

#Could only get my function to run if the output was being converted to a list for whatever reason
output = list(merge_common(circuit_list))
