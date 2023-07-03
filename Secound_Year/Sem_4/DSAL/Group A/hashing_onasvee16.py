"""
GROUP A-1
NAME: ONASVEE BANARSE
    SE COMP 1
ROLL NO: 09

Q>Consider telephone book database of N clients. Make use of a hash table implementation to
quickly look up client‘s telephone number. Make use of two collision handling techniques
and compare them using number of comparisons required to find a set of telephone numbers.
"""


class hashing_chaining:
    arr = []

    def __init__(self, num):
        self.MAX = num
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False

        for idx, elem in enumerate(self.arr[h]):
            if len(elem) == 2 and elem[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break

        if not found:
            self.arr[h].append((key, val))  # not exist

    def __getitem__(self, key):
        h = self.get_hash(key)
        for ele in self.arr[h]:
            if ele[0] == key:
                return ele[1]
        return None

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, key_val in enumerate(self.arr[h]):
            if key_val[0] == key:
                del self.arr[h][index]
                print('Item Deleted ')
                break
        else:
            print('Item Not Found ')


class hashing_addressing:
    def __init__(self, num):
        self.MAX = num
        self.arr = [None for i in range(self.MAX)]
        print(len(self.arr))

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, key):
        count_jump = 0
        h = self.get_hash(key)
        if self.arr[h] is None:
            return
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            count_jump += 1
            element = self.arr[prob_index]
            if element is None:
                return
            if element[0] == key:
                return element[1], count_jump

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key, val)
        else:
            new_h = self.find_slot(key, h)
            self.arr[new_h] = (key, val)
        # print(self.arr)

    def get_prob_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0, index)]

    def find_slot(self, key, index):
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return prob_index
            if self.arr[prob_index][0] == key:
                return prob_index
        raise Exception("Hashmap full")

    def __delitem__(self, key):
        h = self.get_hash(key)
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                print('Item Not Found ')
                break  # item not found so return. You can also throw exception
            if self.arr[prob_index][0] == key:
                self.arr[prob_index] = None
                print('Item Deleted ')
                break
        # print(self.arr)


if __name__ == '__main__':
    try:
        while True:
            userinput1 = int(input(
                '\nWelcome to Hashing Table \nEnter which hashing table type to apply\n1.CHAINING \n2.ADDRESSING \n3.EXIT\n==>'))

            if userinput1 == 1:
                size1 = int(input("ENTER SIZE OF TABLE :"))
                ch = hashing_chaining(size1)
                while True:
                    userinput2 = int(input("\n1.INSERT \n2.SEARCH\n3.Display HASHING TABLE\n4.DELETE\n5.EXIT\n>>>> "))
                    if userinput2 == 1:
                        numb = int(input("ENTER NUMBER OF CLIENT:"))
                        for i in range(numb):
                            name1 = input("ENTER NAME OF CLIENT:")
                            number1 = int(input("ENTER PHONE NUMBER OF CLIENT:"))
                            ch[name1] = number1
                    elif userinput2 == 2:
                        name1 = input("ENTER NAME OF CLIENT:")
                        print(ch[name1])
                    elif userinput2 == 3:
                        print(ch.arr)
                    elif userinput2 == 4:
                        name1 = input("ENTER NAME OF CLIENT:")
                        del ch[name1]

                    elif userinput2 == 5:
                        break
                    else:
                        print("WRONG INPUT")

            elif userinput1 == 2:
                size2 = int(input("ENTER SIZE OF TABLE :"))
                ah = hashing_addressing(size2)
                while True:
                    userinput2 = int(
                        input("\n1.INSERT\n2.SEARCH\n3.Display HASHING TABLE\n4.DELETE\n5.EXIT\n>>>> "))

                    if userinput2 == 1:
                        numb = int(input("ENTER NUMBER OF CLIENT:"))
                        for i in range(numb):
                            name1 = input("ENTER NAME OF CLIENT:")
                            number1 = int(input("ENTER PHONE NUMBER OF CLIENT:"))
                            ah[name1] = number1

                    elif userinput2 == 2:
                        name1 = input("ENTER NAME OF CLIENT:")
                        element, count = ah[name1]
                        print('Number is :', element, '\tRequired number of jumps:', count)

                    elif userinput2 == 3:
                        print(ah.arr)

                    elif userinput2 == 4:
                        name1 = input("ENTER NAME OF CLIENT:")
                        del ah[name1]

                    elif userinput2 == 5:
                        break
                    else:
                        print("WRONG INPUT")
            elif userinput1 == 3:
                break
            else:
                print('Wrong Input')
    except Exception as e:
        print('\nWrong input :', e)

"""
Algorithm:
1. Start / Run

2. selecting Chaining method .
3. Declare an array of a linked list with the hash table size.
4.Initialize an array of a linked list to NULL.

/// inserting :
5. Find hash key.
6. If chain[key] == NULL
     Make chain[key] points to the key node.
7.Otherwise(collision),
     Insert the key node at the end of the chain[key].
     
/// searching : 
8. Get the value
9. Compute the hash key.
10. Search the value in the entire chain. i.e. chain[key].
11. If found, print "Search Found"
12. Otherwise, print "Search Not Found"

///Removing :
13. Get the value
14. Compute the key.
15. Using linked list deletion algorithm, delete the element from the chain[key].
    Linked List Deletion Algorithm: Deleting a node in the linked list 
16. If unable to delete, print "Value Not Found"

17.selecting linear probing (addressing):
/// inserting 
18.use hash function to find index for a record
19.If that spot is already in use, we use next available spot in a "higher" index.
20. Treat the hash table as if it is round, if you hit the end of the hash table, go back to the front

///searching 
21.use hash function to find index of where an item should be.
22.If it isn't there search records that records after that hash location (remember to treat table as cicular) until 
    either it found, or until an empty record is found. If there is an empty spot in the table before record is found, 
    it means that the the record is not there.

/// removing :
23.determine the hash index of the record
24.find record and remove it making the spot empty

25. Stop 
"""

"""
Complexity :

Worst-Case Time Complexity (Linear Probing)
Find: O(n) 
Insert: O(n)
Remove: O(n)

Average-Case Time Complexity (Linear Probing)
Find: O(1)
Insert: O(1)
Remove: O(1)

Best-Case Time Complexity (Linear Probing)
Find: O(1) — No collisions
Insert: O(1) — No collisions
Remove: O(1) — No collisions

Space Complexity (Linear Probing)
O(n)
///////
Worst-Case Time Complexity (Separate Chaining)
Find: O(n) — If all the keys mapped to the same index (assuming Linked List)
Insert: O(n) — If all the keys mapped to the same index (assuming Linked List) and we check for duplicates
Remove: O(n) — If all the keys mapped to the same index (assuming Linked List)

Average-Case Time Complexity (Separate Chaining)
Find: O(1) 
Insert: O(1) 
Remove: O(1) 

Best-Case Time Complexity (Separate Chaining)
Find: O(1) — No collisions
Insert: O(1) — No collisions
Remove: O(1) — No collisions

Space Complexity (Separate Chaining)
O(n) — Hash Tables typically have a capacity that is at most some constant multiplied by n
        (the constant is predetermined), and each of our n nodes occupies O(1) space

"""

"""
Output:

Welcome to Hashing Table 
Enter which hashing table type to apply
1.CHAINING 
2.ADDRESSING 
3.EXIT
==>1
ENTER SIZE OF TABLE :10

1.INSERT 
2.SEARCH
3.Display HASHING TABLE
4.DELETE
5.EXIT
>>>> 1
ENTER NUMBER OF CLIENT:4
ENTER NAME OF CLIENT:Orion1
ENTER PHONE NUMBER OF CLIENT:111
ENTER NAME OF CLIENT:Orion2
ENTER PHONE NUMBER OF CLIENT:1234
ENTER NAME OF CLIENT:KK1
ENTER PHONE NUMBER OF CLIENT:9876
ENTER NAME OF CLIENT:KK2
ENTER PHONE NUMBER OF CLIENT:111

1.INSERT 
2.SEARCH
3.Display HASHING TABLE
4.DELETE
5.EXIT
>>>> 3
[[('KK2', 111)], [], [], [], [], [], [], [], [('Orion1', 111)], [('Orion2', 1234), ('KK1', 9876)]]

1.INSERT 
2.SEARCH
3.Display HASHING TABLE
4.DELETE
5.EXIT
>>>> 2
ENTER NAME OF CLIENT:KK2
111

1.INSERT 
2.SEARCH
3.Display HASHING TABLE
4.DELETE
5.EXIT
>>>> 2
ENTER NAME OF CLIENT:Orion2
1234

1.INSERT 
2.SEARCH
3.Display HASHING TABLE
4.DELETE
5.EXIT
>>>> 2
ENTER NAME OF CLIENT:abcd
None

1.INSERT 
2.SEARCH
3.Display HASHING TABLE
4.DELETE
5.EXIT
>>>> 4
ENTER NAME OF CLIENT:KK2
Item Deleted 

1.INSERT 
2.SEARCH
3.Display HASHING TABLE
4.DELETE
5.EXIT
>>>> 3
[[], [], [], [], [], [], [], [], [('Orion1', 111)], [('Orion2', 1234), ('KK1', 9876)]]

1.INSERT 
2.SEARCH
3.Display HASHING TABLE
4.DELETE
5.EXIT
>>>> 5

Welcome to Hashing Table 
Enter which hashing table type to apply
1.CHAINING 
2.ADDRESSING 
3.EXIT
==>2
ENTER SIZE OF TABLE :10
10

1.INSERT
2.SEARCH
3.Display HASHING TABLE
4.DELETE
5.EXIT
>>>> 1
ENTER NUMBER OF CLIENT:3
ENTER NAME OF CLIENT:KK1
ENTER PHONE NUMBER OF CLIENT:1234
ENTER NAME OF CLIENT:Orion
ENTER PHONE NUMBER OF CLIENT:9876
ENTER NAME OF CLIENT:HS1
ENTER PHONE NUMBER OF CLIENT:3456

1.INSERT
2.SEARCH
3.Display HASHING TABLE
4.DELETE
5.EXIT
>>>> 3
[('Orion', 9876), None, None, None, ('HS1', 3456), None, None, None, None, ('KK1', 1234)]

1.INSERT
2.SEARCH
3.Display HASHING TABLE
4.DELETE
5.EXIT
>>>> 2
ENTER NAME OF CLIENT:HS1
Number is : 3456 	Required number of jumps: 1


1.INSERT
2.SEARCH
3.Display HASHING TABLE
4.DELETE
5.EXIT
>>>> 5

Welcome to Hashing Table 
Enter which hashing table type to apply
1.CHAINING 
2.ADDRESSING 
3.EXIT
==>3

Process finished with exit code 0

"""