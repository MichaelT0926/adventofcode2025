def main():

    file = open('input')
    input_str = file.read()

    input_ranges, input_available = str_to_list(input_str)

    fresh_total = 0

    input_ranges = range_str_to_range_int(input_ranges)

    print(check(input_ranges, fresh_total))

   

def str_to_list(input_str):

    temp = input_str.split('\n')

    split = temp.index('')

    return temp[:split], temp[split+1:]

   

def range_str_to_range_int(input_ranges):

    temp_range = []

    for ranges in input_ranges:

        temp_str = ranges.split('-')

        temp_range.append([int(temp_str[0]), int(temp_str[1])])

    return(temp_range)

   

def check(input_ranges, fresh_total):

    input_ranges.sort(key=lambda x: x[0])

    merged_intervals = [input_ranges[0]]

    for current in input_ranges[1:]:

        last_merged = merged_intervals[-1]

        if current[0] <= last_merged[1]:

            last_merged[1] = max(last_merged[1], current[1])

        else:

            merged_intervals.append(current)

   

    for pair in merged_intervals:

        fresh_total += (pair[1]+1 - pair[0])

    return (fresh_total)

main()