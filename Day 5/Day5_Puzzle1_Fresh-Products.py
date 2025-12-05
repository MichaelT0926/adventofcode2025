def main():
    file = open('input')
    input_str = file.read()

    input_ranges, input_available = str_to_list(input_str)

    fresh_total = 0

    print(check(input_ranges, input_available, fresh_total))

   

def str_to_list(input_str):

    temp = input_str.split('\n')

    split = temp.index('')

    return temp[:split], temp[split+1:]

   

def check(input_ranges, input_available, fresh_total):

    for each in input_available:

        for ranges in input_ranges:

            range_conversion_str = ranges.split('-')

            range_conversion = range(int(range_conversion_str[0]), int(range_conversion_str[1]) +1)

            if int(each) in range_conversion:

                fresh_total +=1

                break

               

    return(fresh_total)

main()