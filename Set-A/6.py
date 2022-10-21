'''
WAP To find the sum of the digit in number
'''


number=int(input('Enter Any Number -> '))
sum=0
num=number
while number!=0:
    digit=number%10
    sum+=digit
    number=number//10
print(f'\nSum of the digit of number {num} is {sum}')
# output:
'''
Enter Any Number -> 567

Sum of the digit of number 567 is 18
'''



  

