"""
Write a python program to store first year percentage of students in array. 
Write function for sorting array of floating point numbers in ascending 
order using a) Selection Sort b) Bubble sort and display top five scores.
"""
import array as arr

def accept():
    a=arr.array('f',[])
    n=int(input("Enter number of students: "))
    for i in range(n):
        a.append(float(input("Enter first year percentage of student {}: ".format(i+1))))
    return a

def print_per(arr):
    for i in range(0, len(arr)):
        print("\t {0:.2f}".format(arr[i]), end=" ")
    print()

def bubble_sort(arr):
    flg=0
    for i in range(len(arr)):
        for j in range(0,(len(arr)-i-1)):
            if(arr[j]>=arr[j+1]):
                flg=1
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
        if(flg==0):
            break
    print("\nElements after sorting are-\n")
    print_per(arr)
    top_five(arr)
    
def selection_sort(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[j]<=arr[i]):
               temp=arr[i]
               arr[i]=arr[j]
               arr[j]=temp
    print("\nElements after sorting are-\n")
    print_per(arr)
    top_five(arr)

def top_five(arr):
    j=0
    print("\nThe top scores are- ")
    for i in reversed(arr):
        print("\t {0:.2f}".format(i), end=" ")
        j=j+1
        if(j==5):
            break
    print()
        
A=arr.array('f',[])
sort_A=arr.array('f',[])

while(True):
    print("\n***********MENU**********")
    print("Enter 1 to accept percentage")
    print("Enter 2 to display percentage")
    print("Enter 3 to sort using bubble sort technique")
    print("Enter 4 to sort using selection sort technique")
    print("Enter 5 to exit")
    c=int(input("Enter your choice: "))
    if(c==1):
        A=accept()
    elif(c==2):
        print_per(A)
    elif(c==3):
        bubble_sort(A)
    elif(c==4):
        selection_sort(A)
    elif(c==5):
        print("Thank you")
        break
    else:
        print("Enter correct choice")