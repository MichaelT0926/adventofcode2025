import re
import operator

#Looks for any run of non-whitespace characters
regex_pattern = '\S+'

file = open('input')
ceph_math_input = file.read()

ceph_math_lines = [re.findall(regex_pattern, line) for line in open('input')]

#Operator look up dict
operators = { '+': operator.add, '*': operator.mul}

total = 0

#Solution will not work for any input without exactly 5 rows that follow the rules of cephalopod math
for col in range(0,len(ceph_math_lines[0])):
    num_1 = int(ceph_math_lines[0][col])
    num_2 = int(ceph_math_lines[1][col])
    num_3 = int(ceph_math_lines[2][col])
    num_4 = int(ceph_math_lines[3][col])

    #Uses the operator library to apply the operator for the given column to each number in the column
    total += operators[ceph_math_lines[4][col]](operators[ceph_math_lines[4][col]](num_1, num_2), operators[ceph_math_lines[4][col]](num_3, num_4))

print (total)
