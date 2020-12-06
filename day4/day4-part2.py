import re
import string

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
    porperties = re.split('\s',passport)
    for i in porperties:
        if verify_propertie(i) == False:
            return False
    return True

def verify_propertie(propertie):
    identifier, value = propertie.split(':')
    result = {
    'byr': lambda x: 1920 <= int(x) <=2002,
    'iyr': lambda x: 2010 <= int(x) <=2020,
    'eyr': lambda x: 2020 <= int(x) <=2030,
    'hgt': lambda x: verify_height(x),
    'hcl': lambda x: verify_hair(x),
    'ecl': lambda x: verify_color(x),
    'pid': lambda x: len(x) == 9,
    'cid': lambda x: True
    }[identifier](value)
    return result

def verify_height(x):
    if 'cm' in x:
        return 150 <= int(''.join(list(filter(str.isdigit, x)))) <= 193
    elif 'in' in x:
        return 59 <= int(''.join(list(filter(str.isdigit, x)))) <= 76
    else:
        return False

def verify_hair(x):
    if x[0] == '#' and len(x) == 7:
        a = x.replace('#','0')
        return all(c in string.hexdigits for c in a)
    else:
        return False


def verify_color(x):
    color_field = ["amb", "blu", "brn", "gry" , "grn" , "hzl" , "oth"]
    for item in color_field:
        if item in x:
            return True
    return False

field = ["byr" ,"iyr" ,"eyr" ,"hgt" ,"hcl" ,"ecl" ,"pid"]
f = open_file_as_list()
count = 0
#check_all_items(f[2],field)
for passports in f:
    if check_all_items(passports,field):
        count = count + 1
print(count)