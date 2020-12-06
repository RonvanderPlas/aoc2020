def open_file_as_list():
    f = open('day4.txt')
    content = f.read()
    lines = content.split("\n\n")
    file_list = list(lines)
    return file_list

def check_all_items(passport,check_fields):
    for item in check_fields:
        if not item in passport:
            return 0
    return 1
        

field = ["byr" ,"iyr" ,"eyr" ,"hgt" ,"hcl" ,"ecl" ,"pid"]
f = open_file_as_list()
count = 0

for passports in f:
    if check_all_items(passports,field):
        #print(passports + "\n\n VALID! \n")
        count = count + 1
    else:
        print(passports + "\n\n INVALID! \n")

print(count)