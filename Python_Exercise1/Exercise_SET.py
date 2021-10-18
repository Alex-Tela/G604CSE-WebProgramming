n = int(input("Number of heights: "))
l = []

for i in range(n):
    num = int(input())
    l.append(num)

s = set(l)
distinctList = list(s)
sum = 0

for i in range(len(distinctList)):
    sum += distinctList[i]

print("Average of distinct heights: " + str(sum/len(distinctList)))