'''
Swap two number without using third variable

'''

def swapTwoNumber(x,y):
  x=x+y
  y=x-y
  x=x-y
  return x,y

num1=int(input('Enter num1 : -> '))
num2=int(input('Enter num2 : -> '))
print('Num1 and Num2 Before Swapping :')
print(f'Num1={num1} and Num2={num2}')

print('Num1 and Num2 After Swapping :')
num1,num2=swapTwoNumber(num1,num2)
print(f'Num1={num1} and Num2={num2}')

'''
you can simply swap two number 
num1,num2=num2,num1
'''
#output
'''
Enter num1 : -> 59
Enter num2 : -> 7
Num1 and Num2 Before Swapping :
Num1=59 and Num2=7
Num1 and Num2 After Swapping :
Num1=7 and Num2=59
'''


