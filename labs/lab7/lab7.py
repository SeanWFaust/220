"""
Name: Sean Faust
lAB7.py

Problem: This lab has us taking in a test file and maniplulating it to find the weighted average of different
students.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def weighted_average(in_file_name, out_file_name):
    with open(in_file_name, 'r') as file:
        newfile = []
        numfile = []
        namefile = []
        numberfile = []
        weightlist = []
        gradelist = []
        average = 0
        newweightlist = []
        averages = []
        infile = file.readlines()
        for item in infile: # strips the white space and newline tags
            newfile.append(item.strip())
        for item in newfile: #splits the list of strings into the name and the numbers
            namefile.append(item.split(': ')[0])
            numfile.append(item.split(': ')[1])
        for item in numfile: # splits the numbers into a list of strings
            numberfile.append(item.split())
        for item in numberfile: #separates the numbers into two lists, one for weights other for grades
            weightlist.append(item[0::2])
            gradelist.append(item[1::2])
        for weightnum in weightlist: #finds the total weighting.
            weight = 0
            for num in weightnum:
                weight += int(num)
            newweightlist.append(weight)

        for i in range(len(namefile)):
            if newweightlist[i] < 100:
                print(namefile[i] + "'s average: Error: The weights are less than 100.")
            elif newweightlist[i] > 100:
                print(namefile[i] + "'s average: Error: The weights are more than 100.")
            else:

                print(namefile[i] + "'s average:" + str(average / 100))
        print(averages)
        print(newweightlist)
        print(weightlist)
        print(gradelist)
        print(namefile)