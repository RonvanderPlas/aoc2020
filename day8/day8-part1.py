def open_file_as_list():
    f = open('day8.txt')
    lines = f.readlines()
    file_list = list(lines)
    return file_list

def split_cmd_value(f,line):
    value, cmd = f[line].split()
    return value, int(cmd)

def next_jump(f,index,accu):
    if "jmp" in split_cmd_value(f,index)[0]:
        return (index + split_cmd_value(f,index)[1]), accu
    elif "acc" in split_cmd_value(f,index)[0]:
        return index+1, (accu + split_cmd_value(f,index)[1])
    elif "nop" in split_cmd_value(f,index)[0]:
        return index+1, accu
    else:
        return index, accu

index = 0
accu = 0
unique_indexes = []
f = open_file_as_list()
while not index in unique_indexes:
    unique_indexes.append(index)
    index, accu = next_jump(f,index, accu)
    #print(str(index) + " " + str(accu))
print(accu)

