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

def check_options_for_gold(f,options):
    amount = 0
    for element in options:
        if not "other" in element:    
            amount = element[1]
            kind_of_bag = element[3:]
            for character in characters_to_remove:
                kind_of_bag = kind_of_bag.replace(character, "")
                kind_of_bag = kind_of_bag.replace("bags", "bag")
            if "shiny gold" in kind_of_bag:
                return True
            else:
                new_options = extract_options_from_type(f,kind_of_bag)
                if new_options is not None:
                    if check_options_for_gold(f,new_options) == True:
                        return True
                #print(amount + " " + str(kind_of_bag) + " Options: " + str(new_options))
    return False


def count_gold_bags(f,count,kind_of_bag):
    print()

count = 0
failed = 0
f = open_file_as_list()
for line in f:
    if check_options_for_gold(f,extract_options_from_type(f,extract_type_from_line(line))) == True:
        count +=1
    else:
        failed+=1
print("Total: "+ str(count+failed) + " [" + str(count) + "-" + str(failed) + "]")
