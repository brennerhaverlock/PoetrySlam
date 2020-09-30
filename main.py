import random
import os

#Create a function called get_file_lines()

def get_file_lines(filename):
    return open(filename, 'r').read()#.strip().split('\n')

#print(get_file_lines('poem.txt'))
#Create a function called lines_printed_backwards()

def lines_printed_backwords(lines_list):
    textfile = open("poem.txt")
    lines = textfile.readlines()
    for line in reversed(lines):
        return line

print(lines_printed_backwords(get_file_lines('poem.txt')))

#Create a function called lines_printed_random():

#Create a function called lines_printed_custom()