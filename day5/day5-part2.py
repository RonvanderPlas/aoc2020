import re
import string

def open_file_as_list():
    f = open('day5.txt')
    lines = f.readlines()
    file_list = list(lines)
    return file_list

def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

d = { "F": "0", "B": "1", "R":"1","L":"0"}
f = open_file_as_list()
seat_id_list = []
for line in f:
    row_dec = int(replace_all(line[:7],d),2)
    seat_dec = int(replace_all(line[7:],d),2)
    seat_id = (row_dec*8)+seat_dec
    seat_id_list.append(seat_id)
    seat_id_list.sort()

prev_seat_id = seat_id_list[0]
for item in seat_id_list:
    if (item-prev_seat_id) > 1:
        print("Seat ID: " + str(item-1))
    prev_seat_id = item
# print(seat_id_list)