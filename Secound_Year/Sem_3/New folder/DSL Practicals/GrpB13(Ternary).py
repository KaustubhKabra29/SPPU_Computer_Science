"""
Write a python program to maintain club members, sort on roll numbers 
in ascending order. Write function “Ternary_Search” to search 
whether particular student is member of club or not. 
Ternary search is modified binary search that divides 
array into 3 halves instead of two.
"""

import array as arr

def Ternary_Search(arr,ele):
    left=0
    right=len(arr)-1    
    while(left<=right):
        mid1=left+(right-left)//3
        mid2=left+2*(right-left)//3
        
        if(ele==arr[left]):
            return left
        elif(ele==arr[right]):
            return right
        elif(ele<arr[left] or ele>arr[right]):
            return -1
        elif(ele<=arr[mid1]):
            right=mid1
        elif(ele>=arr[mid2]):
            left=mid2
        elif(ele>arr[mid1] and ele<arr[mid2]):
            left=mid1+1
            right=mid2-1
    return -1
        
def Recursive_Ternary(arr,ele,left,right):
    
    if(left<=right):
        mid1=left+(right-left)//3
        mid2=right-(right-left)//3       
        if(ele==arr[mid1]):
            return mid1
        if(ele==arr[mid2]):
            return mid2
        
        if(ele<arr[mid1]):
            return Recursive_Ternary(arr, ele, left, mid1-1)
        elif(ele>arr[mid2]):
            return Recursive_Ternary(arr, ele, mid2+1, right)
        else:
            return Recursive_Ternary(arr, ele, mid1+1, mid2-1)
    return -1

def accept():
    A=arr.array('I',[])
    n=int(input("Enter number of students: "))
    for i in range(0,n):
        A.append(int(input("Enter roll number: ")))
    return A

def display(A):
    for i in range(0, len(A)):
        print("\t", A[i], end=" ")
    print()

def sel_sort(A):
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if(A[j]<A[i]):
               temp=A[i]
               A[i]=A[j]
               A[j]=temp
    return A

A=arr.array('I',[])
sort_A=arr.array('I',[])

while True:
    
    print("\n1)Accept roll number \n2)Print roll number \n3)sort roll numbers\n4)Non-recursive Ternary Search \n5)Recursive Ternary Search \n6)Exit")
    ch=int(input("Enter your choice: "))
    
    if(ch==1):
        A=accept()
    
    elif(ch==2):
        display(A)
        
    elif(ch==3):
        sort_A=sel_sort(A)
        print("The sorted roll numbers are:")
        display(sort_A)
        
    elif(ch==4):
        ele=int(input("Enter roll number to be searched: "))
        r=Ternary_Search(sort_A, ele)
        if(r==-1):
            print("Roll number not found!!")
        else:
            print("The roll number", ele, "is present at index", r)
    elif(ch==5):
        ele=int(input("Enter roll number to be searched: "))
        r=Recursive_Ternary(sort_A, ele, 0, len(sort_A)-1)
        if(r==-1):
            print("Roll number not found!!")
        else:
            print("The roll number", ele, "is present at index", r)
    elif(ch==6):
        print("Thank you")
        break
    else:
        print("Wrong choice")
        break