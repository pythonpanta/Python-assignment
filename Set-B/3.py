'''
WAP to count the character in the string
'''


def countCharacter(mystring):
  count=0
  for i in mystring:
      count+=1
  return count
mystring=input('Enter any string -> ').replace(' ','')
print(f'Total Character is {countCharacter(mystring)}')
'''
output:
Enter any string -> python language
Total Character is 14
'''

