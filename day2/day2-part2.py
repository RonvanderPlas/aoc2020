def open_file_as_list():
    f = open('day2.txt')
    lines = f.readlines()
    file_list = list(lines)
    return file_list

def check_char(password,char,first_pos,second_pos):
    if password[first_pos-1] == char and password[second_pos-1] != char:
        print("Valid pass: [" + password + "] Char: [" + char + "] POS: [" + str(first_pos-1) + "-" + str(second_pos-1) + "]")
        return 1
    elif password[first_pos-1] != char and password[second_pos-1] == char:
        print("Valid pass: [" + password + "] Char: [" + char + "] POS: [" + str(first_pos-1) + "-" + str(second_pos-1) + "]")
        return 1
    else:
        return 0

total_count = 0
f = open_file_as_list()
for line in f:
    splitted_string = line.split()
    values = splitted_string[0].split("-")
    #print("values: " + values[0] + ":" + values[1] + " char: " + splitted_string[1][0] + " pass: " + splitted_string[2])
    if check_char(splitted_string[2],splitted_string[1][0],int(values[0]) ,int(values[1])) == 1:
        total_count = total_count + 1
print("Total valid passwords:" + str(total_count))