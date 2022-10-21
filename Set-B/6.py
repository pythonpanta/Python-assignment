#  Sum of the digit of number 
number=int(input('Enter Any Number -> '))
sum=0
num=number
while number!=0:
    digit=number%10
    sum+=digit
    number=number//10
print(f'\nSum of the digit of number {num} is {sum}')
'''
output:
Enter Any Number -> 987

Sum of the digit of number 987 is 24

'''
