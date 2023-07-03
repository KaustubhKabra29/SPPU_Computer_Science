import array as arr


def accept():
    a = arr.array('f', [])
    n = int(input("Enter number of students: "))
    for i in range(n):
        a.append(float(input("Enter first year percentage of student {}: ".format(i + 1))))
    return a


def print_per(arr):
    for i in range(0, len(arr)):
        print("\t {0:.2f}".format(arr[i]), end=" ")
    print()


def partition(arr, first, last):         # 25  57  48  37  12  92  86  33
    pivot = arr[first]                   # pivot=25
    i = first + 1                        # i=57
    j = last                             # j=33

    while True:

        while (i <= j and arr[i] <= pivot):
            i = i + 1

        while (i <= j and arr[j] >= pivot):
            j = j - 1

        if (i <= j):
            arr[i], arr[j] = arr[j], arr[i]

        else:
            break

    arr[first], arr[j] = arr[j], arr[first]
    return j


def quick_sort(arr, first, last):
    if (first >= last):
        return

    p = partition(arr, first, last)
    quick_sort(arr, first, p - 1)
    quick_sort(arr, p + 1, last)
    return arr


def top_five(arr):
    j = 0
    print("\nThe top scores are- ")
    for i in reversed(arr):
        print("\t {0:.2f}".format(i), end=" ")
        j = j + 1
        if (j == 5):
            break
    print()


A = arr.array('f', [])
sort_A = arr.array('f', [])

while True:

    print("\n1)Accept percentage \n2)Print percentage \n3)Sort and display top scores\n4)Exit \n")
    ch = int(input("Enter your choice: "))

    if (ch == 1):
        A = accept()

    elif (ch == 2):
        print_per(A)

    elif (ch == 3):
        print("Percentages after sorting-")
        sort_A = quick_sort(A, 0, len(A) - 1)
        print_per(sort_A)
        top_five(sort_A)

    elif (ch == 4):
        print("Thank you")
        break
    else:
        print("Wrong choice")
        break;