import time
def main():
    file = open('input')
    rotation_sequence = file.read()
    dial_start = 50

    rotation_list = stringToArray(rotation_sequence)

    print(rotate(rotation_list, dial_start))


def stringToArray(sequence_string):
    #Converts rotational sequence to an array split at each new line, resulting in an array that looks like so: [R1,L20,...,L18]
    return sequence_string.split("\n")

def rotate(sequence_list, dial_start):
    #Init variables
    addition = False
    dial = dial_start
    counter = 0

    #Begins loop through the array
    for i in sequence_list:
        #Determines if the dial will increment or decrement
        if i[0] == "R":
            addition = True
        elif i[0] == "L":
            addition = False
        
        #Removes the leading letter and converts the remainder into an int
        i = int(i.replace(i[0], "", 1))

        #Logic for addition or subtraction
        if addition == True:
            dial = dial + i
        elif addition == False:
            dial = dial - i

        #Logic for keeping the number in scope
        if dial > 99:
            dial = upper_correction(dial)
        elif dial < 0:
            dial = lower_correction(dial)

        #When the dial is equal to 0, add 1 to the count
        if dial == 0:
            counter+=1

    return counter

def upper_correction(dial):
    string_of_int = str(dial)
    length_of_string = len(string_of_int)

    while length_of_string > 2:
        string_of_int = string_of_int.replace(string_of_int[0],"",1)
        length_of_string = len(string_of_int)

    return int(string_of_int)

def lower_correction(int):
    while int < 0:
        int += 100
    return (int)

main()