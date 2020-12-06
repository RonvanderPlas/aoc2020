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
highest_seat = 0
for line in f:
    row_dec = int(replace_all(line[:7],d),2)
    seat_dec = int(replace_all(line[7:],d),2)
    seat_id = (row_dec*8)+seat_dec
    #print("ROW: [" + str(row_dec) + "] Seat: [" + str(seat_dec) + "] ID: [" + str(seat_id) + "]")
    if seat_id > highest_seat:
        highest_seat = seat_id
print(highest_seat)