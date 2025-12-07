import re
import operator

regex_pattern = '\S'

file = open('input')
ceph_math = file.read()

ceph_math_lines = ceph_math.split('\n')

total = 0

corrected_num_list = []

#Concat columns to gather the vertical numbers used in the math
for col in range(0,len(ceph_math_lines[0])):
    corrected_num_list.append(ceph_math_lines[0][col] + ceph_math_lines[1][col] + ceph_math_lines[2][col] + ceph_math_lines[3][col])

#Added correction to trigger final calculation
corrected_num_list.append('    ')

#Operator look up dict
operators = { '+': operator.add, '*': operator.mul}

#Isolate operators into their own list
operator_list = re.findall(regex_pattern, ceph_math_lines[4])
operator_index = 0

set_list = []

for each in corrected_num_list:
    #Looks for a set break, represented by 4 spaces
    if each != '    ':
        set_list.append(each)
    else:
        set_total = int(set_list[0])
        for each in set_list[1:]:
            set_total = operators[operator_list[operator_index]](set_total, int(each))
        total += set_total
        set_list = []
        operator_index+=1
        continue

print(total)