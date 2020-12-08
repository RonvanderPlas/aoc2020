# Structure: [Kind of bag] Contain [Options],[Options]...
# Options: [Amount],[Kind of bag]

# For every color
#   extract the options
characters_to_remove = ".\n"

def open_file_as_list():
    f = open('day7.txt')
    lines = f.readlines()
    file_list = list(lines)
    return file_list

def extract_type_from_line(line):
    return line.split("contain")[0]

def extract_options_from_line(line):
    option_list = []
    kind_of_bag, options = line.split("contain")
    option_list = options.split(',')
    return option_list

def extract_options_from_type(f,kind_of_bag):
    for line in f:
        if kind_of_bag in extract_type_from_line(line):
            return(extract_options_from_line(line))

def count_in_gold(f,options):
    amount = 0
    rv_amount = 0
    for element in options:
        if not "other" in element:    
            amount = element[1]
            kind_of_bag = element[3:]
            for character in characters_to_remove:
                kind_of_bag = kind_of_bag.replace(character, "")
                kind_of_bag = kind_of_bag.replace("bags", "bag")

            new_options = extract_options_from_type(f,kind_of_bag)
            if new_options is not None:
                rv_amount += int(amount) + (int(amount) * count_in_gold(f,new_options))
        else:
            return 0
    return rv_amount

count = 0
failed = 0
f = open_file_as_list()
print(count_in_gold(f,extract_options_from_type(f,"shiny gold")))
