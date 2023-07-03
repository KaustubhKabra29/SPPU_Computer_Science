# Group A - 1 Write a Python program to store marks scored in subject “Fundamental of Data Structure”
# by N students in the class. Write functions to compute following:
# a) The average score of class
# b) Highest score and lowest score of class
# c) Count of students who were absent for the test
# d) Display mark with highest frequency

# Average Score Of Test :---


def average(l):
    sum = 0
    cnt = 0
    for i in range(len(l)):
        if l[i] != -999:
            sum += l[i]
            cnt += 1

    avg = sum / cnt
    print("Total Marks are : ", sum)
    print("Average Marks are : {:.2f}".format(avg))


# Highest Score In The Test :---


def Maximum(l):
    Max = l[0]
    for i in range(len(l)):
        if l[i] > Max:
            Max = l[i]
    return (Max)


# Lowest Score In The Test :---


def Minimum(l):
    for i in range(len(l)):
        if l[i] != -37:
            Min = l[i]
            break

    for j in range(i + 1, len(l)):
        if l[j] != -37 and l[j] < Min:
            Min = l[j]
    return (Min)


# Absent Number of Student For Test :---

def absentCnt(l):
    cnt = 0
    for i in range(len(l)):
        if l[i] == -37:
            cnt += 1
    return (cnt)


# Highest Frequency Of Marks :---


def maxFrequency(l):
    i = 0
    Max = 0
    print(" Marks ----> frequency count ")
    for ele in l:
        if l.index(ele) == i:
            print(ele, "---->", l.count(ele))
            if l.count(ele) > Max:
                Max = l.count(ele)
                mark = ele
        i += 1
    return (mark, Max)


# Input the Number of Students and Their Corresponding Marks :---


marksInFDS = []
noStudents = int(input("Enter total number of students : "))
for i in range(noStudents):
    marks = int(input("Enter marks of Student " + str(i + 1) + " : "))
    marksInFDS.append(marks)

flag = 1
while flag == 1:
    print("/*************MENU**************/")
    print("1. The average score of class ")
    print("2. Highest score and lowest score of class ")
    print("3. Count of students who were absent for the test ")
    print("4. Display mark with highest frequency ")
    print("5. Exit ")
    choice = int(input("Enter your choice : "))

    if choice == 1:
        average(marksInFDS)

    elif choice == 2:
        print("Highest score in the class is : ", Maximum(marksInFDS))
        print("Lowest score in the class is : ", Minimum(marksInFDS))

    elif choice == 3:
        print("Count of students who were absent for the test is : ", absentCnt(marksInFDS))

    elif choice == 4:
        mark, count = maxFrequency(marksInFDS)
        print("Highest frequency of marks {0} is {1} ".format(mark, count))

    else:
        print("Wrong Choice,Please Choose Another Option.")
        flag = 0
