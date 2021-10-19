list = [1, 10, 5, 24, 13, 0, 9, 18, 90]

n = int(input("Enter how many commands you want to perform: "))


for i in range(0, n):
    command = input()
    array = command.split(" ")
    length = len(array)
    if length == 3:
        list[int(array[1])] = array[2]
    elif length == 2 and array[0] == "remove":
        list.remove(int(array[1]))
    elif length == 2 and array[0] == "append":
        list.append(int(array[1]))
    elif length < 2 and array[0] == "print":
        print(list)
    elif length < 2 and array[0] == "pop":
        list.pop()
    elif length < 2 and array[0] == "sort":
        list.sort()
    elif length < 2 and array[0] == "reverse":
        list.reverse()
    else:
        print("Command not recognised")