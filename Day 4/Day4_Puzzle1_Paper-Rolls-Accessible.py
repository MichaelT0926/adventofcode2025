def main():
    #Init input and data needed to solve
    file = open('input')
    paper_grid_str = file.read()

    paper_grid_str_binarized = ascii_to_binary(paper_grid_str)

    accessible_total = 0

    paper_grid_list = string_to_list(paper_grid_str_binarized)

    coord_map = create_coord_map(paper_grid_list)

    print(check_surrounding(paper_grid_list, coord_map, accessible_total))

def ascii_to_binary(paper_grid_str):
    #Converting the ascii to binary for ease of count
    return (paper_grid_str.replace('.', '0').replace('@', '1'))

def string_to_list(paper_grid_str):
    #String to list
    return (paper_grid_str.split('\n'))

def create_coord_map(paper_grid_list):
    #Creating a tuple coord map to check surrounding points against
    coord_map =[]
    for y in range(len(paper_grid_list)):
        for x in range(len(paper_grid_list[0])):
            coord_map.append((x, y))
    return (coord_map)

def check_surrounding(paper_grid_list, coord_map, accessible_total):
    #Check each point against adjacent points to see if they are accessible
    for point in coord_map:
        total_adjacent = 0
        for adjacent_y in range(-1,2):
            for adjacent_x in range(-1,2):
                check_point = (adjacent_x + point[0], adjacent_y + point[1])
                if check_point[0] not in range(0, coord_map[-1][0]+1) or check_point[1] not in range(0, coord_map[-1][1]+1) or check_point == point:
                    total_adjacent += 0
                else:
                    total_adjacent += int(paper_grid_list[check_point[1]][check_point[0]])
        if total_adjacent <= 3 and int(paper_grid_list[point[1]][point[0]]) == 1:
            accessible_total += 1
    
    return(accessible_total)

main()