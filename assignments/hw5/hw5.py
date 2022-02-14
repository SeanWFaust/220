"""
Name: Sean Faust
HW5.py

Problem: This homework focuses on the different string methods
within python.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def name_reverse():
    name = input("Enter your first then last name:")
    spname = name.split()
    print(spname[1] + ', ' + spname[0])


def company_name():
    url = input("Enter a companies URL:")
    comp_name = url.split('.')
    print(comp_name[1])


def initials():
    num_stud = eval(input("How many students are in the class?"))
    for i in range(1, num_stud + 1):
        stud_name = input("What is the name of student " + str(i) + "?")
        listnames = stud_name.split()
        fname = listnames[0]
        lname = listnames[1]
        print(fname[0] + lname[0])


def names():
    enterednames = input("Enter a list of names:")
    listnames = enterednames.split(',')
    for name in listnames:
        spltname = name.split()
        fname = spltname[0]
        lname = spltname[1]
        print(fname[0] + lname[0], end=' ')


def thirds():
    splt = []
    num_sen = eval(input("Enter the number of sentences:"))
    for i in range(1, num_sen + 1):
        sentence = input("What is sentence " + str(i) + "?")
        spltsen = sentence[0:len(sentence):3]
        splt = splt + [spltsen]
    print(''.join(splt))


def word_average():
    totalchar = 0
    sentence = input("Enter a sentence:")
    lsen = sentence.split()
    for word in lsen:
        totalchar += len(word)
    avg = totalchar / len(lsen)
    print("The average word length is: " + str(avg))


def pig_latin():
    piglist = []
    sentence = input("Enter a sentence:")
    spltsentence = sentence.split()
    for word in spltsentence:
        pigword = (word[1:len(word)] + word[0] + 'ay')
        piglist.append(pigword)
    print(' '.join(piglist).lower())



if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
