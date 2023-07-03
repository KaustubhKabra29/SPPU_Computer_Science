comparison = 0 # Global Variable

class Chaining(object):
    def push(self, name, TeleNumber):
        hashCode = hash(name) % num
        lis = [(name, TeleNumber)]
        if hashTable[hashCode] == None:
            hashTable[hashCode] = lis

        else:
            tup = (name, TeleNumber)
            i = 0
            for j in range(num):
                if hashTable[hashCode][i][0] == name:
                    hashTable[hashCode][i] = tup
                    i += 1
                    return

            else:
                hashTable[hashCode].append(tup)

    def get(self, key):
        global comparison
        comparison = 0
        hashCode = hash(key) % num
        i = 0
        if hashTable[hashCode] == None:
            return -1
        
        elif hashTable[hashCode][i][0] == key:
            comparison += 1
            return hashTable[hashCode][i][1]

        else:
            i += 1
            for j in range(num):
                comparison += 1
                if hashTable[hashCode][i][0] == key:
                    return hashTable[hashCode][i][1]

            else:
                return -1

class Addressing(object):
    def push(self, name, TeleNumber):
        hashCode = hash(name) % size
        lis = [name, TeleNumber]
        if hashTable[hashCode] == None:
            hashTable[hashCode] = lis

        else:
            for i in range(num):
                hashCode = (hashCode + 1) % size
                if hashTable[hashCode] == None:
                    hashTable[hashCode] = lis
                    return

    def get(self, key):
        global comparison
        comparison = 0
        hashCode = hash(key) % size
        if hashTable[hashCode] == None:
            return -1

        elif hashTable[hashCode][0] == key:
            comparison += 1
            return hashTable[hashCode][1]
        else:
            for i in range(num):
                comparison += 1
                hashCode = (hashCode + 1) % size
                if hashTable[hashCode][0] == key:
                    return hashTable[hashCode][1]
            else:
                return -1

if __name__ == '__main__':
    try:
        size = int(input("\nEnter The Size of Telephone Book: "))
        ch = Chaining()
        ad = Addressing()

        while True:
            userInput = int(input("\n1. Press 1 For Chaining\n2. Press 2 For Addressing\n3. Press 3 To Exit\n>>>> "))
            if userInput == 1:
                hashTable = [None] * size
                while True:
                    userInput = int(input("\n1. Press 1 To Push Data\n2. Press 2 To Get Data\n3. Press 3 To Go Back\n>>>> "))
                    if userInput == 1:
                        num = int(input("\nEnter The Number of Clients: "))
                        for i in range(num):
                            name = input("\nEnter The Name: ")
                            TeleNumber = int(
                                input("\nEnter The Telephone Number: "))
                            ch.push(name, TeleNumber)

                    elif userInput == 2:
                        name = input("\nEnter The Name of Client: ")
                        print(ch.get(name))
                        print("\nNo. of Comparisons:", comparison)

                    elif userInput == 3:
                        break

                    else:
                        print("\nPlease Enter Correct Input!!")

            elif userInput == 2:
                hashTable = [None] * size
                while True:
                    userInput = int(input(
                        "\n1. Press 1 To Push Data\n2. Press 2 To Get Data\n3. Press 3 To Go Back\n>>>> "))
                    if userInput == 1:
                        num = int(input("\nEnter The Number of Clients: "))
                        for i in range(num):
                            name = input("\nEnter The Name: ")
                            TeleNumber = int(input("\nEnter The Telephone Number: "))
                            ad.push(name, TeleNumber)

                    elif userInput == 2:
                        name = input("\nEnter The Name of Client: ")
                        print(ad.get(name))
                        print("\nNo. of Comparisons:", comparison)

                    elif userInput == 3:
                        break

                    else:
                        print("\nPlease Enter Correct Input!!")

            elif userInput == 3:
                exit()

            else:
                print("\nPlease Enter Correct Input!!")

    except Exception as e:
        print("\nWrong Input,", e)

