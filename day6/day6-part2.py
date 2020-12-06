def open_file_as_list():
    f = open('day6.txt')
    content = f.read()
    lines = content.split("\n\n")
    file_list = list(lines)
    return file_list

def count_unique_character(group):
    intial_answer = []
    lines = group.split()
    for char in lines[0]:
        if char != '\n':
            intial_answer.append(char)
    for line in lines:
        i=0
        while i < len(intial_answer):
            if not intial_answer[i] in line:
                intial_answer.remove(intial_answer[i])
            else:
                i+=1
    return len(intial_answer)

f = open_file_as_list()
count = 0
for group in f:  
    count = count + count_unique_character(group)
print(count)