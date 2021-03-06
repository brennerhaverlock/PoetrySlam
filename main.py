import random
import os

#Create a function called get_file_lines()

def get_file_lines(filename):
    filename = open(filename, 'r')
    return filename.readlines()

#print(get_file_lines('poem.txt'))

#Create a function called lines_printed_backwards()
def lines_printed_backwards(lines_list):
    lines_list_reverse = lines_list[::-1] # reverses the list of lines and assigned it to another varible
    for string in lines_list_reverse:
        line_number = lines_list.index(string) + 1 # assigned a varible the index of the string containing the line
        print(line_number, string)

#Create a function called lines_printed_random():
def lines_printed_random(lines_list):
    list_num = range(len(lines_list))
    list_num = list(list_num)
    for i in list_num:
        rnum = random.randrange(26)
        print(lines_list[rnum])

#Create a function called lines_printed_custom()

def lines_printed_custom(lines_list):
    ask = input(
        'Do you want a random line? (Y/n) ')
    if ask == "Y":
        print(f'Your new line is: {random.choice(lines_list)}')
    else:
        return

#print(get_file_lines('poem.txt'))
#lines_printed_backwards(get_file_lines('poem.txt'))
#lines_printed_random(get_file_lines('poem.txt'))
lines_printed_custom(get_file_lines('poem.txt'))


