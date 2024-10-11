import math
while True:
    number=int(input('number: '))
    for i in range(2,int(math.sqrt(number))+1):
        if number%i==0:
            print('composite_number ')
            break
    else:
        if number!=1:
            print("prime_number")
        else:
            print('none')
