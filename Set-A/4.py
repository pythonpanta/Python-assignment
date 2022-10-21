'''
WAP to check whether number is prime or not

'''

def checkPrime(number):
  for i in range(2,number):
      if number%i==0:
          return False
  return True


number=int(input('Enter Number for checking prime or not -> '))
result=checkPrime(number)
if result:
  print(f'{number} is Prime Number')
else:
  print(f'{number} is Not Prime Number')
# output
'''
Enter Number for checking prime or not -> 77
77 is Not Prime Number

Enter Number for checking prime or not -> 19
19 is Prime Number
'''