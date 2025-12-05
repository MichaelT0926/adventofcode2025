def main():
    #Init variables
    total = 0
    file = open('input')
    ranges_string = file.read()
    ranges_list = string_to_list(ranges_string)
    ranges_two_d_list = list_to_two_d_list(ranges_list)

    print(check_validity(ranges_two_d_list, total))

def string_to_list(ranges_string):
    #Split the string at ',' to separate the ranges
    return ranges_string.split(',')

def list_to_two_d_list(ranges_list):
    #Init first dimension of array to be appended into
    two_d_ranges_list = []

    #Loop through current list, appending a list containing each range's min and max to create the second dimension
    for i in ranges_list:
        two_d_ranges_list.append(i.split('-'))

    return two_d_ranges_list

def check_validity(ranges_two_d_list, total):
    #Loop through the outer dimension of arrays
    for range_pair in ranges_two_d_list:
        #Grab the min and max from the inner dimension and convert into a range, adding 1 to the max for inclusion
        current_range = range(int(range_pair[0]), int(range_pair[1])+1)

        #Loop through each number in the range
        for each_number in current_range:
            #Converting each number into a string for ease of length finding and index searching
            each_number = str(each_number)

            #Logic to kill current process if the current number is not able to meet invalid criteria by virtue of length
            if len(each_number)%2 != 0:
                continue
            else:
                #Find the midpoint index and check to see if the front and back halves of the number are the same, if so, adding that number to the total
                midway_index = len(each_number)//2

                if each_number[:midway_index] == each_number[midway_index:]:
                    total += int(each_number)

    return total

main()