n = int(input("Enter number of students for which you want to add details: "))
while (n < 2 or n > 10):
    n = int(input("Number too high or too small. Enter again: "))

d = {}

for i in range(n):
    incorrect = 3
    while (incorrect != 0):
        line = input()
        details = line.split(" ")
        for x in range(1, len(details)):
            if (int(details[x]) >= 0 or int(details[x]) <= 100):
                incorrect -= 1

    l = []
    for i in range(1, len(details)):
        l.append(int(details[i]))
    d[details[0]] = l

print(d)


