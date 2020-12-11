total_count = 0

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


def explore_next_step(f, new_data, target):
    global total_count
    match_list = get_possible_matches(f, new_data)
    #print(match_list)
    if not match_list:
        return 0
    else:
        #match_list.sort()
        for item in match_list:  
            if int(item) == target:
                total_count += 1
            else:
                explore_next_step(f,int(item),target)     
    #return total_count

diff_list = []
f = open_file_as_list()
target = int(get_device_jolts(f)-3)
print("Target: " + str(target))
explore_next_step(f,0, target)
print(total_count)