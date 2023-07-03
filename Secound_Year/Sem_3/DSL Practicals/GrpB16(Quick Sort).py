"""
Write a python program to store first year percentage of students in array.
Write function for sorting array of floating point numbers in ascending 
order using quick sort and display top five scores.
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
    
def partition(arr,start,end):
    pivot=arr[start]
    low=start+1
    high=end
    
    while True:
        
        while(low<=high and arr[low]<=pivot):
            low=low+1
            
        while(low<=high and arr[high]>=pivot):
            high=high-1
            
        if(low<=high):
            arr[low],arr[high]=arr[high],arr[low]
            
        else:
            break
        
    arr[start],arr[high]=arr[high],arr[start]
    return high

def quick_sort(arr,start,end):
    if(start>=end):
        return

    p=partition(arr,start,end)
    quick_sort(arr,start,p-1)
    quick_sort(arr,p+1,end)
    return arr

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

while True:
    
    print("\n1)Accept percentage \n2)Print percentage \n3)Sort and display top scores\n4)Exit \n")
    ch=int(input("Enter your choice: "))
    
    if(ch==1):
        A=accept()
    
    elif(ch==2):
        print_per(A)
        
    elif(ch==3):
        print("Percentages after sorting-")
        sort_A=quick_sort(A,0,len(A)-1)
        print_per(sort_A)
        top_five(sort_A)
        
    elif(ch==4):
        print("Thank you")
        break
    else:
        print("Wrong choice")
        break;