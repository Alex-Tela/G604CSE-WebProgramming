l = [2, 5, 5, 6, 2, 3, 7, 9, 5, 6, 6]
uniqueL = set(l)
max = 0

for score in uniqueL:
    if score > max:
        max = score

uniqueL.remove(max)

secondMax = 0

for score in uniqueL:
    if score > secondMax:
        secondMax = score

print(f"Score of runner-up is: {secondMax}")
    

