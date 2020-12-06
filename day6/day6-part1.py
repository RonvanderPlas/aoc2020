def open_file_as_list():
    f = open('day6.txt')
    content = f.read()
    lines = content.split("\n\n")
    file_list = list(lines)
    return file_list

def count_unique_character(group):
    unique_chars = []
    for line in group:
        for char in line:
            if not char in unique_chars and char != '\n':
                unique_chars.append(char)
    return len(unique_chars)

f = open_file_as_list()
count = 0
for group in f:
    count = count + count_unique_character(group)
print(count)