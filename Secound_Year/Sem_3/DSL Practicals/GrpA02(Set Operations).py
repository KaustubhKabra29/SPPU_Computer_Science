# Group A - 2. In second year computer engineering class, group A student’s play cricket, group B students
# play badminton and group C students play football. Write a Python program using functions to compute following: -
# a) List of students who play both cricket and badminton
# b) List of students who play either cricket or badminton but not both
# c) Number of students who play neither cricket nor badminton
# d) Number of student who play cricket and football but not badminton.
# (Note- While realizing the group, duplicate entries should be avoided, Do not use SET built-in functions)

# List Of Student as per Games they Play

SeComp = ["Kaustubh Kabra", "Harsh Shah", "Onasvee Banarse", "Ankit Patil", "Virat Kohli", "MS Dhoni",
          "Ravindra Jadeja", "Smriti Mandhana", "Lionel Messi", "Cristiano Ronaldo", "Neymar Jr", "Saina Nehwal",
          "Shrikanth Kidambi", "PV Sindhu"]
Cricket = ["Kaustubh Kabra", "Ankit Patil", "Virat Kohil", "MS Dhoni", "Ravindra Jadeja", "Smriti Mandhana"]
Badminton = ["Kaustubh Kabra", "Harsh Shah", "PV Sindhu", "Shrikanth Kidambi", "Saina Nehwal", "Virat Kohli",
             "MS Dhoni"]
Football = ["Kaustubh Kabra", "Onasvee Banarse", "Lionel Messi", "Cristiano Ronaldo", "Neymar Jr", "Virat Kohli",
            "MS Dhoni", "Ravindra Jadeja"]

# Removal of Duplicates[Here in our Program there is no Duplicates]


def removeduplicate(t):

    l1 = []
    for i in t:
        if i not in l1:
            l1.append(i)
    return l1

# Union Set[ Union of Cricket Playing Student and Badminton Playing Student]


def union(lst1, lst2):
    lst3 = lst1.copy()
    for value in lst2:
        if value not in lst3:
            lst3.append(value)
    return lst3

# Intersection Set [We have no use of this in solving this Practical]


def intersection(lst1, lst2):
    lst3 = []
    for value in lst1:
        if value in lst2:
            lst3.append(value)
    return lst3

# Difference Set[ Difference of Union Set of Cricket and Badminton Playing Student from All Secomp Student ]


def difference(lst1, lst2):
    lst3 = []
    for value in lst1:
        if value not in lst2:
            lst3.append(value)
    return lst3

# Symmetric Difference Set[ Difference of Intersection of Cricket and Badminton Playing Student from
# Union of Cricket and Badminton Playing Student ]


def symmetricdiff(lst1, lst2):
    d1 = difference(lst1, lst2)
    d2 = difference(lst2, lst1)
    lst3 = union(d1, d2)
    return lst3

# Required Solution[ Difference of Union of Cricket and Badminton Playing Student from All SeComp Student ]


def ncnb(lst1, lst2, lst3):

    lst4 = difference(lst1, union(lst2, lst3))
    print(lst4)
    return lst4, len(lst4)


Cricket = removeduplicate(Cricket)
Badminton = removeduplicate(Badminton)
Football = removeduplicate(Football)

flag = 1
while flag == 1:
    print("/~~~~~~~MENU~~~~~~~/")
    print("1. List of students who played both Cricket and Badminton ")
    print("2. list of students who play either cricket or badminton but not both ")
    print("3. Number of students who play neither cricket nor badminton ")
    print("4. Number of student who play cricket and football but not badminton ")
    print("5. Exit")
    choice = int(input("Enter your choice : "))

    if choice == 1:
        print(" Cricket : ", Cricket)
        print(" Badminton : ", Badminton)
        print(" List of students who played both Cricket and Badminton : ")
        print(intersection(Cricket, Badminton))

    elif choice == 2:
        print(" Cricket : ", Cricket)
        print(" Badminton : ", Badminton)
        print(" list of students who play either cricket or badminton but not both ")
        print(symmetricdiff(Cricket, Badminton))

    elif choice == 3:
        print(" Class : ", SeComp)
        print(" Cricket : ", Cricket)
        print(" Badminton : ", Badminton)
        l, cnt = ncnb(SeComp, Cricket, Badminton)
        print("Number of students who play neither cricket nor badminton : ", cnt)
        print("List of students who play neither cricket nor badminton : ", l)
    elif choice == 4:
        print("Class :", SeComp)
        print("Cricket :", Cricket)
        print("Badminton", Badminton)
        print("Football", Football)
        print("List of students who play cricket and football but not badminton :")
        print(difference(SeComp, Badminton))
        print("Number of students who play cricket and football but not badminton :")
        print(len(difference(SeComp, Badminton)))
    else:
        print("Wrong Choice,Please Choose Another Option ")
        flag = 0
