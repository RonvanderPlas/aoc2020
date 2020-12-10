def open_file_as_list():
    f = open('temp.txt')
    lines = f.readlines()
    file_list = list(lines)
    return file_list

def check_for_sum(f,min,max,length,new_value):
    new_list = f[min-1:max-1]
    #print("Checking: " + str(int(f[new_value-1])) + " " + str(new_list))
    for value1 in new_list:
        for value2 in new_list:
            sum = int(value1)+int(value2)
            if sum == int(f[new_value-1]) and new_list.index(value1) != new_list.index(value2):
                #print("1: " + str(int(value1)) + " 2: "  + str(int(value2)) +" Sum: " + str(sum) + " Checking: " + f[new_value-1])
                return True
    return False

def check_for_contigues(f,line_index,match_value):
    summed_value = 0
    prev_value = 0
    summed_list = []
    while summed_value <= match_value:
        if int(f[line_index]) > prev_value:
            summed_value += int(f[line_index])
            summed_list.append(str(int(f[line_index])))
            prev_value = int(f[line_index])
            line_index += 1

            if len(summed_list) > 2 and summed_value == match_value:
                print("Found Match " + str(summed_list))

preamble_length = 5
index = 0
found_failed_value = 0
f = open_file_as_list()
for line in f:
    if index > preamble_length:
        if not (check_for_sum(f,(index-preamble_length),index,preamble_length,index)):
            print("Failed: " + f[index-1])
            found_failed_value = f[index-1]
            break
    index += 1

index = 0
sum = 0
for line in f:
    check_for_contigues(f,index,int(found_failed_value))
    index += 1
