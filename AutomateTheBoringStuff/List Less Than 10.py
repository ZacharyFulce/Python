list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newList = []
b = int(input('Please enter a number.'))
for a in list:
    if(a < b):
        newList.append(a)
print(newList)
