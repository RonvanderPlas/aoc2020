def open_file_as_list():
    f = open('day10.txt')
    lines = f.readlines()
    file_list = list(lines)
    return file_list

def get_device_jolts(f):
    highest_jolt = 0
    for line in f:
        if int(line) > highest_jolt:
            highest_jolt = int(line)
    return highest_jolt+3

def get_possible_matches(f,current_value):
    match_list = []
    for line in f:
        if int(line) > current_value and int(line) <= current_value+3:
            match_list.append(int(line))
    return match_list


def explore_next_step(f, new_data, diff_list):
    match_list = get_possible_matches(f, new_data)
    if(match_list):
        match_list.sort()
        explore_next_step(f,int(match_list[0]),diff_list)
        diff_list.append(int(match_list[0])-new_data)
        #print(str(int(match_list[0])-new_data))
    else:
        return new_data

diff_list = []
f = open_file_as_list()
explore_next_step(f,0, diff_list)
diff1 = diff_list.count(1)
diff3 = diff_list.count(3)+1
print("Amount of 1: " + str(diff1) + " Amount of 3: " + str(diff3) + " Multiplied: " + str(diff1*diff3))
