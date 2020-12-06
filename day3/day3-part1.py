def open_file_as_list():
    f = open('day3.txt')
    lines = f.readlines()
    file_list = list(lines)
    return file_list


f = open_file_as_list()
pos = 0
num_lines = sum(1 for line in f)
count = 0
cur_line = 0
while cur_line < (num_lines-1):
    pos = pos + 3
    cur_line = cur_line + 1
    length = len(f[cur_line])-2
    if pos > length:
        pos = (pos - length)-1
    print("POS X-Y: [" + str(pos) + "-" + str(cur_line) + "] Length: [" + str(length) + "] Char: [" + f[cur_line][pos] + "]")
    if(f[cur_line][pos] == '#'):
        count = count + 1
print("total trees: " + str(count))