'''
WAP thet should take input from the user and it should accept input onlt if the number is between 0 and 100
 output:
 Enter any  number
 125
 please enter again
 -100
 please enter again
 50 
 Your number is 50

'''


num=int(input('Enter any Number\n'))
while True:
    if num>0 and num <100:
        print(f'Your Number is {num}')
        break
    else:
        num=int(input('Please enter again \n'))

'''
output:
Enter any  number
125
please enter again
-100
please enter again
50 
Your number is 50
'''



'''
 output:
 Enter any  number
 125
 please enter again
 -100
 please enter again
 50 
 Your number is 50
'''