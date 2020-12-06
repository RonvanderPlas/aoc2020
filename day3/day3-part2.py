def open_file_as_list():
    f = open('day3.txt')
    lines = f.readlines()
    file_list = list(lines)
    return file_list

def count_trees(data,amount_right,amount_down):
    pos = 0
    num_lines = sum(1 for line in data)
    count = 0
    cur_line = 0
    while cur_line < (num_lines-1):
        pos = pos + amount_right
        cur_line = cur_line + amount_down
        length = len(f[cur_line])-2
        if pos > length:
            pos = (pos - length)-1
        #print("POS X-Y: [" + str(pos) + "-" + str(cur_line) + "] Length: [" + str(length) + "] Char: [" + f[cur_line][pos] + "]")
        if(data[cur_line][pos] == '#'):
            count = count + 1
    return count


f = open_file_as_list()

way_one =count_trees(f,1,1)
way_two =count_trees(f,3,1)
way_three =count_trees(f,5,1)
way_four =count_trees(f,7,1)
way_five =count_trees(f,1,2)

print("Total trees:" + str(way_one * way_two * way_three * way_four * way_five))