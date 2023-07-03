"""
Group A _2
Name: Onasvee Banarse
Se comp 1
Roll no : 09

Implement all the functions of a dictionary (ADT) using hashing and handle collisions using
chaining with / without replacement.
Data: Set of (key, value) pairs, keys are mapped to values, keys must be comparable, keys must
be unique.
Standard operations: insert (key, value), Find (key), Delete (key).
"""

class Dictionary(object):
    def __init__(self, size):
        self.dict = [None] * size
        self.length = 0

    def __del__(self):
        pass

    def insert(self, key, value):
        hashCode = hash(key) % size
        lis = [(key, value)]

        if self.dict[hashCode] is None:
            self.dict[hashCode] = lis
            self.length += 1

        else:
            tup = (key, value)
            i = 0
            for j in range(size):
                if i == len(self.dict[hashCode]):
                    self.length += 1
                    self.dict[hashCode].append(tup)
                    return

                if self.dict[hashCode][i][0] == key:
                    self.dict[hashCode][i] = tup
                    return
                i += 1

            else:
                self.length += 1
                self.dict[hashCode].append(tup)

    def find(self, key):
        hashCode = hash(key) % size
        i = 0

        if self.dict[hashCode] == None:
            return -1

        elif self.dict[hashCode][i][0] == key:
            return self.dict[hashCode][i][1]

        else:
            i += 1
            for j in range(size):
                if i == len(self.dict[hashCode]):
                    return -1

                if self.dict[hashCode][i][0] == key:
                    return self.dict[hashCode][i][1]
                i += 1

            else:
                return -1

    def delete(self, key):
        hashCode = hash(key) % size
        i = 0

        if self.dict[hashCode] == None:
            return -1

        elif self.dict[hashCode][i][0] == key:
            if len(self.dict[hashCode]) == 1:
                self.length -= 1
                self.dict[hashCode] = None

            else:
                self.length -= 1
                self.dict[hashCode].remove(self.dict[hashCode][i])

        else:
            i += 1
            for j in range(size):
                if i == len(self.dict[hashCode]):
                    return -1

                if self.dict[hashCode][i][0] == key:
                    if len(self.dict[hashCode]) == 1:
                        self.length -= 1
                        self.dict[hashCode] = None

                    else:
                        self.length -= 1
                        self.dict[hashCode].remove(self.dict[hashCode][i])
                    return
                i += 1

            else:
                return -1

    def printDict(self):
        print("\n{ ", end="")
        i = 1
        for lis in self.dict:
            if lis != None:
                for ele in lis:
                    if i == self.length:
                        print(f"{ele[0]} : {ele[1]}", end="")
                    else:
                        print(f"{ele[0]} : {ele[1]}, ", end="")
                    i += 1
        print(" }")


if __name__ == '__main__':
    try:
        size = int(input("\nEnter The Size of Dictionary: "))
        dt = Dictionary(size)

        while True:
            userInput = int(input("\n1. Press 1 To Insert(Key, Value)\n2. Press 2 To Find(Key)\n3. Press 3 To Delete("
                                  "Key)\n4. Press 4 To Print Dictionary\n5. Press 5 To Exit\n>>>> "))
            if userInput == 1:
                while True:
                    selectKey = int(input("\nSelect The Data Type of Key: \n1. String\n2. Integer\n3. Float\n>>>> "))
                    selectValue = int(
                        input("\nSelect The Data Type of Value: \n1. String\n2. Integer\n3. Float\n>>>> "))

                    if selectKey == 1 and selectValue == 1:
                        key = input("\nEnter The Key: ")
                        value = input("\nEnter The Value: ")
                        dt.insert(key, value)
                        break

                    elif selectKey == 1 and selectValue == 2:
                        key = input("\nEnter The Key: ")
                        value = int(input("\nEnter The Value: "))
                        dt.insert(key, value)
                        break

                    elif selectKey == 1 and selectValue == 3:
                        key = input("\nEnter The Key: ")
                        value = float(input("\nEnter The Value: "))
                        dt.insert(key, value)
                        break

                    elif selectKey == 2 and selectValue == 1:
                        key = int(input("\nEnter The Key: "))
                        value = input("\nEnter The Value: ")
                        dt.insert(key, value)
                        break

                    elif selectKey == 2 and selectValue == 2:
                        key = int(input("\nEnter The Key: "))
                        value = int(input("\nEnter The Value: "))
                        dt.insert(key, value)
                        break

                    elif selectKey == 2 and selectValue == 3:
                        key = int(input("\nEnter The Key: "))
                        value = float(input("\nEnter The Value: "))
                        dt.insert(key, value)
                        break

                    elif selectKey == 3 and selectValue == 1:
                        key = float(input("\nEnter The Key: "))
                        value = input("\nEnter The Value: ")
                        dt.insert(key, value)
                        break

                    elif selectKey == 3 and selectValue == 2:
                        key = float(input("\nEnter The Key: "))
                        value = int(input("\nEnter The Value: "))
                        dt.insert(key, value)
                        break

                    elif selectKey == 3 and selectValue == 3:
                        key = float(input("\nEnter The Key: "))
                        value = float(input("\nEnter The Value: "))
                        dt.insert(key, value)
                        break

                    else:
                        print("\nPlease Enter Correct Input!!")
                        continue

            elif userInput == 2:
                selectKey = int(input("\nSelect The Data Type of Key: \n1. String\n2. Integer\n3. Float\n>>>> "))
                while True:
                    if selectKey == 1:
                        key = input("\nEnter The Key: ")
                        if dt.find(key) != -1:
                            print("\n{", f"{key} : {dt.find(key)}", "}")
                        else:
                            print(dt.find(key))
                        break

                    elif selectKey == 2:
                        key = int(input("\nEnter The Key: "))
                        if dt.find(key) != -1:
                            print("\n{", f"{key} : {dt.find(key)}", "}")
                        else:
                            print(dt.find(key))
                        break

                    elif selectKey == 3:
                        key = float(input("\nEnter The Key: "))
                        if dt.find(key) != -1:
                            print("\n{", f"{key} : {dt.find(key)}", "}")
                        else:
                            print(dt.find(key))
                        break

                    else:
                        print("\nPlease Enter Correct Input!!")
                        continue

            elif userInput == 3:
                selectKey = int(input("\nSelect The Data Type of Key: \n1. String\n2. Integer\n3. Float\n>>>> "))
                while True:
                    if selectKey == 1:
                        key = input("\nEnter The Key: ")
                        dt.delete(key)
                        break

                    elif selectKey == 2:
                        key = int(input("\nEnter The Key: "))
                        dt.delete(key)
                        break

                    elif selectKey == 3:
                        key = float(input("\nEnter The Key: "))
                        dt.delete(key)
                        break

                    else:
                        print("\nPlease Enter Correct Input!!")
                        continue

            elif userInput == 4:
                dt.printDict()

            elif userInput == 5:
                exit()

            else:
                print("\nPlease Enter Correct Input!!")

    except Exception as e:
        print("\nWrong Input,", e)

"""
Algorithm:
1.Start 
2. Taking user input 
3.setting dictionary size and creating empty list 
4.
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

17. using for loop for printing the dict
18. Stop
"""

"""
time complexity 
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