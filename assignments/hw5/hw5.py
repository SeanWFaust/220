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
    spname = name.split() # Split input into a list
    print(spname[1] + ', ' + spname[0]) # printing out the user input in the correct order.


def company_name():
    url = input("Enter a companies URL:")
    comp_name = url.split('.') #splits the entered sentence into a list by .'s
    print(comp_name[1]) # prints the second thing in the list


def initials():
    num_stud = eval(input("How many students are in the class?"))
    for i in range(1, num_stud + 1):# Loops through the number of students.
                                    # Starts at 1 for the correct print statement.
        stud_name = input("What is the name of student " + str(i) + "?")
        listnames = stud_name.split() # splits the name into a list of 2
        fname = listnames[0]#sets the first thing in the list to a variable
        lname = listnames[1]#sets the seoncd thing in the list to a variable
        print(fname[0] + lname[0]) #prints the first character of the first and second
                                   #thing in the list respectively


def names():
    enterednames = input("Enter a list of names:")
    listnames = enterednames.split(',') #splits listed names into a list by ,'s
    for name in listnames:#loops through the names
        spltname = name.split()#splits each name into their own list
        fname = spltname[0]#same as my initials function
        lname = spltname[1]#same as my initlals function
        print(fname[0] + lname[0], end=' ')#same as initials but with the anded end to print on
                                           #the same line


def thirds():
    splt = []
    num_sen = eval(input("Enter the number of sentences:"))
    for i in range(1, num_sen + 1):#loops through number of sentences starting at 1
        sentence = input("What is sentence " + str(i) + "?")
        spltsen = sentence[0:len(sentence):3]#splits the sentence starting at the first character
        splt = splt + [spltsen]              #stepping by 3
    print(''.join(splt))


def word_average():
    totalchar = 0 #initalizing the variable
    sentence = input("Enter a sentence:")
    lsen = sentence.split()#spliting the entered sentence into a list of words
    for word in lsen:
        totalchar += len(word)#adding the length of the words together
    avg = totalchar / len(lsen)#dividing the total length of the words by the number of words
    print("The average word length is: " + str(avg))


def pig_latin():
    piglist = []#initializing an empty set to save to.
    sentence = input("Enter a sentence:")
    spltsentence = sentence.split()#spliting the sentence into a list of words
    for word in spltsentence:
        pigword = (word[1:len(word)] + word[0] + 'ay')#splicing the words, taking the
        piglist.append(pigword)                       #first character and adding it to
    print(' '.join(piglist).lower())                  #the end then adding ay to the end



if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
