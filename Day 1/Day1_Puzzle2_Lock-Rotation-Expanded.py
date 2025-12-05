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
        prev_dial = dial

        if addition == True:
            dial = dial + i
        elif addition == False:
            dial = dial - i

        #Logic for keeping the number in scope
        if dial >= 100:
            dial, counter = upper_correction(dial, counter)
        elif dial <= -1:
            #Increments counter for all cases of underflow, except for those caused by dial starting at 0 this rotation
            if prev_dial > 0:
                counter+=1
            dial, counter = lower_correction(dial, counter)

        #When the dial is equal to 0, add 1 to the count
        if dial == 0:
            counter+=1
    return counter

def upper_correction(dial, counter):
    #Function to correct an overflow

    #Init variables
    string_of_int = str(dial)
    length_of_string = len(string_of_int)
    counter_addition = ""

    #Converted the int to a str to remove overflow, keeping removed digits to add to the counter
    while length_of_string > 2:
        counter_addition += string_of_int[0]
        string_of_int = string_of_int.replace(string_of_int[0],"",1)
        length_of_string = len(string_of_int)

    #If the dial lands on 0 after correction, removes a count as it will be accounted for in rotate function
    if int(string_of_int) == 0:
        counter -= 1

    counter += int(counter_addition)
    return (int(string_of_int), counter)

def lower_correction(dial, counter):
    #Function for correcting underflow

    #Adds 100 as many times as needed to remove underflow, adds 1 to counter for every pass over 0
    while dial < 0:
        if dial < -99:
            counter += 1
        dial += 100

    #If the dial lands on 0 after correction, removes a count as it will be accounted for in rotate function
    if dial == 0:
        counter -= 1

    return (dial, counter)

main()