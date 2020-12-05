def open_file_as_list():
    f = open('day1.txt')
    lines = f.readlines()
    file_list = list(lines)
    return file_list

f = open_file_as_list()
for line in f:
    value1 = int(line)
    for line in f:
        value2= int(line)
        for line in f:
            value3= int(line)
            if value1 + value2 + value3 == 2020:
                print("found match " + str(value1) + " " + str(value2) + " " + str(value3))
                print("multplied: " + str(value1*value2*value3))