list = [1, 10, 5, 24, 13, 0, 9, 18, 90]

n = int(input("Enter how many commands you want to perform: "))


for i in range(0, n):
    command = input()
    array = command.split(" ");
    length = len(array)
    if ( length == 3 ):
        list[int(array[1])] = array[2]
    elif (length == 2):
        if (array[0] == "remove"):
            list.remove(int(array[1]))
        else:
            list.append(int(array[1]))
    else:
        if (array[0] == "print"):
            print(list)
        elif (array[0] == "pop"):
            list.pop()
        elif (array[0] == "sort"):
            list.sort()
        else:
            list.reverse()