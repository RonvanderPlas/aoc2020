def open_file_as_list():
    f = open('day8.txt')
    lines = f.readlines()
    file_list = list(lines)
    return file_list

def find_nop_indexes(f):
    nop_list = []
    index = 0
    for item in f:
        index+=1
        if "nop" in item:
            nop_list.append(index) 
    return nop_list

def find_jmp_indexes(f):
    jmp_list = []
    index = 0
    for item in f:
        index+=1
        if "jmp" in item:
            jmp_list.append(index) 
    return jmp_list

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

def run(f):
    index = 0
    accu = 0
    unique_indexes = []
    while not index in unique_indexes:
        unique_indexes.append(index)
        index, accu = next_jump(f,index, accu)
        if index == 647:
            return True, accu
        #print(str(index) + " " + str(accu))
    return False, accu

accu = 0
succes = False
nop_indexes = []
jmp_indexes = []

f = open_file_as_list()
nop_indexes = find_nop_indexes(f)
for item in nop_indexes:
    #Replace
    f[item-1] = f[item-1].replace("nop","jmp")
    #Run
    succes, accu = run(f)
    if succes == True:
        print("Succes " + str(accu))
    #restore
    f[item-1] = f[item-1].replace("jmp","nop")

jmp_indexes = find_jmp_indexes(f)
for item in jmp_indexes:
    #Replace
    f[item-1] = f[item-1].replace("jmp","nop")
    #Run
    succes, accu = run(f)
    if succes == True:
        print("Succes " + str(accu))
    #restore
    f[item-1] = f[item-1].replace("nop","jmp")


