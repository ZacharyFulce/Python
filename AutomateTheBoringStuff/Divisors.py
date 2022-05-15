try:
    print('Please enter a number.')
    num = int(input())
    if(num > 0):
        list = []
        for i in range(1, num):
            if(num % i == 0):
                list.append(i)
        print(list)
    else:
        raise Exception

except:
    print('Please enter an integer larger than 0.')