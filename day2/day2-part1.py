def open_file_as_list():
    f = open('day2.txt')
    lines = f.readlines()
    file_list = list(lines)
    return file_list

def check_char(password,char,min_count,max_count):
    count = 0
    for i in password:
        if i == char:
            count = count + 1
    if count >= min_count and count <= max_count:
        print("Valid pass: [" + password + "] Char: [" + char + "] MIN-MAX: [" + str(min_count) + "-" + str(max_count) + "] Count: " + str(count))
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