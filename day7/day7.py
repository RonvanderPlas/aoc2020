# Structure: [Kind of bag] Contain [Options],[Options]...
# Options: [Amount],[Kind of bag]

# For every color
#   extract the options
characters_to_remove = ".\n"

def open_file_as_list():
    f = open('temp.txt')
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

def extract_amount_and_kind_from_option(f,options):
    amount = 0
    gold_count = 0
    for element in options:
        amount = element[1]
        kind_of_bag = element[3:]
        for character in characters_to_remove:
            kind_of_bag = kind_of_bag.replace(character, "")

        if "gold" in kind_of_bag:
            return True
        else:
            new_options = extract_options_from_type(f,str(kind_of_bag))
            if new_options is not None:
                extract_amount_and_kind_from_option(f,new_options)
            #print(amount + " " + str(kind_of_bag) + " Options: " + str(new_options))
    return False


def count_gold_bags(f,count,kind_of_bag):
    print()


f = open_file_as_list()
for line in f:
    if extract_amount_and_kind_from_option(f,extract_options_from_type(f,extract_type_from_line(line))) == True:
        print("Found the gold!")
