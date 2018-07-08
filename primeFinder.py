#array declaration
primeArray = []

check = 2

#incrementing while loop
while True:
    print(check, end = '')
    prime = True
    for x in primeArray:
        if(check % x == 0):
            prime = False

    if(prime):
        print(' is Prime!')
        primeArray.append(check)
    else:
        #new line
        print()

    check += 1
