def main():
    #Init variables
    total = 0
    ranges_string = '17330-35281,9967849351-9967954114,880610-895941,942-1466,117855-209809,9427633930-9427769294,1-14,311209-533855,53851-100089,104-215,33317911-33385573,42384572-42481566,43-81,87864705-87898981,258952-303177,451399530-451565394,6464564339-6464748782,1493-2439,9941196-10054232,2994-8275,6275169-6423883,20-41,384-896,2525238272-2525279908,8884-16221,968909030-969019005,686256-831649,942986-986697,1437387916-1437426347,8897636-9031809,16048379-16225280'
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