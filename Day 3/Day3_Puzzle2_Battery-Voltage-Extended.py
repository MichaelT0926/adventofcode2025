def main():
    #Init variables
    file = open('input')
    banks_string = file.read()
    total_voltage = 0

    #Convert string into list
    bank_list = string_to_list(banks_string)

    print(find_max_voltage(bank_list, total_voltage))

def string_to_list(banks_string):
    #Separate the banks into list elements
    return (banks_string.split('\n'))

def find_max_voltage(bank_list, total_voltage):
    #Loop through each bank, creating an initial 12-battery assembly of the last 12 batteries.
    for bank in bank_list:
        voltage = [int(bank_string) for bank_string in bank[-12:]]

        bank_length = -len(bank)-1
        i = -13
        #Loops through the rest of the battery in reverse, replacing the starting assembly battery if it finds a higher one
        while i != bank_length:
            if int(bank[i]) >= voltage[0]:
                replacement = voltage[0]
                voltage[0] = int(bank[i])

                #Take the replaced battery and move it down the line, repeating until it finds one that is higher than it's value
                for x in range(1,12):
                    if replacement >= voltage[x]:
                        temp = voltage[x]
                        voltage[x] = replacement
                        replacement = temp
                    else:
                        break
            
            i-=1
        total_voltage += int(''.join(map(str, voltage)))
    
    return total_voltage
main()
