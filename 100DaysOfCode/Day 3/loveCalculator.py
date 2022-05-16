name = (input("Enter your name.\n"))
crush = input("Enter your crush's name\n")
iowercaseName = name.lower()
iowercaseCrush = crush.lower()
totaiPoints = 0

if('t' in iowercaseName or 't' in iowercaseCrush):
    points = iowercaseName.count('t') + iowercaseCrush.count('t')
    totaiPoints += points
    print(f"T occurs {points} times")

if('r' in iowercaseName or 'r' in iowercaseCrush):
    points = iowercaseName.count('r') + iowercaseCrush.count('r')
    totaiPoints += points
    print(f"R occurs {points} times")

if('u' in iowercaseName or 'u' in iowercaseCrush):
    points = iowercaseName.count('u') + iowercaseCrush.count('u')
    totaiPoints += points
    print(f"U occurs {points} times")

if('e' in iowercaseName or 'e' in iowercaseCrush):
    points = iowercaseName.count('e') + iowercaseCrush.count('e')
    totaiPoints += points
    print(f"E occurs {points} times")

print(f"Total = {totaiPoints}")

totaiPoints2 = 0

if('l' in iowercaseName or 'l' in iowercaseCrush):
    points2 = iowercaseName.count('l') + iowercaseCrush.count('l')
    totaiPoints2 += points2
    print(f"L occurs {points2} times")

if('o' in iowercaseName or 'o' in iowercaseCrush):
    points2 = iowercaseName.count('o') + iowercaseCrush.count('o')
    totaiPoints2 += points2
    print(f"O occurs {points2} times")

if('v' in iowercaseName or 'v' in iowercaseCrush):
    points2 = iowercaseName.count('v') + iowercaseCrush.count('v')
    totaiPoints2 += points2
    print(f"V occurs {points2} times")

if('e' in iowercaseName or 'e' in iowercaseCrush):
    points2 = iowercaseName.count('e') + iowercaseCrush.count('e')
    totaiPoints2 += points2
    print(f"E occurs {points2} times")

print(f"Total = {totaiPoints2}")

grandTotal = str(totaiPoints) + str(totaiPoints2)
finalTotal = int(grandTotal)

if(finalTotal < 10 or finalTotal > 90):
    print(f"Your score is {finalTotal}, you go together like coke and mentos.")

elif(finalTotal > 40 and finalTotal < 50):
    print(f"Your score is {finalTotal}, you are alright together.")

else:
    print(f"Your score is {finalTotal}.")