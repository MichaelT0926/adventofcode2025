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
    #For each bank of batteries, looks for highest and second highest voltage. If the highest voltage is at the final index, mark it as the 2nd highest. Otherwise, remove leading batteries and find the 2nd highest from the remainder
    #Add each bank's max voltage to the total
    for bank in bank_list:
        battery_list = [int(battery) for battery in bank]
        highest_volt_battery = max(battery_list)
        if highest_volt_battery == battery_list[-1]:
            second_highest_volt_battery = highest_volt_battery
            battery_list.pop()
            highest_volt_battery = max(battery_list)
            total_voltage += int(str(highest_volt_battery) + str(second_highest_volt_battery))
        else:
            new_battery_list = battery_list[battery_list.index(highest_volt_battery)+1:]
            second_highest_volt_battery = max(new_battery_list)
            total_voltage += int(str(highest_volt_battery) + str(second_highest_volt_battery))
        
    return total_voltage

main()
