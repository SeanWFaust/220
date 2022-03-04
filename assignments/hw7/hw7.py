"""
Name: Sean Faust
HW7.py

Problem: This homework has us going through text files and writing to text files while manipulating
the data stored within the files.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from encryption import encode, encode_better

def number_words(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    file = in_file.read()
    newfile = file.split()
    out_file = open(out_file_name, 'w')
    for word in newfile:
        print(str(newfile.index(word) + 1), str(word), file=out_file)
    in_file.close()
    out_file.close()

def hourly_wages(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    listfile = []
    file = in_file.readlines()
    out_file = open(out_file_name, 'w')
    for lines in file:
        listfile.append(lines.split())
    for list in listfile:
        wage = float(list[2])
        hours = float(list[3])
        total = (wage + 1.65) * hours
        formattedtotal = '{:.2f}'.format(total)
        print(list[0], list[1], formattedtotal, file=out_file)
    in_file.close()
    out_file.close()


def calc_check_sum(isbn):
    numbers = []
    intnum = []
    checksum = []
    checkl = []
    total = 0
    for i in isbn:
        numbers += i.replace('-', '')
    for i in numbers:
        intnum.append(int(i))
    for i in range(10, 0, -1):
        checkl.append(i)
    for i in range(0, len(intnum)):
        checksum.append(intnum[i] * checkl[i])
    for num in checksum:
        total += num
    return total

def send_message(file_name, friend_name):
    file = open(file_name, 'r')
    infile = file.readlines()
    outfilename = friend_name + '.txt'
    outfile = open(outfilename, 'w')
    for line in infile:
        print(line.strip(), file=outfile)
    file.close()
    outfile.close()

def send_safe_message(file_name, friend_name, key):
    file = open(file_name, 'r')
    infile = file.readlines()
    namefile = friend_name + '.txt'
    outfile = open(namefile, 'w')
    for line in infile:
        print(encode(line.strip(), key), file=outfile)
    file.close()
    outfile.close()

def send_uncrackable_message(file_name, friend_name, pad_file_name):
    file = open(file_name, 'r')
    infile = file.read()
    outfilename = friend_name + '.txt'
    pad = open(pad_file_name, 'r')
    key = pad.read()
    outfile = open(outfilename, 'w')
    print(encode_better(infile, key), file=outfile)
    file.close()
    outfile.close()

if __name__ == '__main__':
    pass
