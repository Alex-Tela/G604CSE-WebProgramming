l = []
n = int(input("Enter number of elements: "))

for x in range(n):
    num = int(input())
    l.append(num)

t = tuple(l)
print(t)

print("Hash: " + str(hash(t)))
