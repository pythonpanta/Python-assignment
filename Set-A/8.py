'''
the number 6 is a truly great number. 
Given two int values, a and b ,return true if either one is 6 or if their sum or diference is 6 
Note:
The function MAth.abs(num) computes the absolute value of a number

example:
love(6,4)->true
love(4,5)->false
love(1,5)->true
'''

def love(a,b):
  if a==6 or b==6 or a+b==6 or a-b==6:
      return True
  return False

  
print(love(6,4)) #True
print(love(4,6)) #True
print(love(5,1)) #True
print(love(1,5)) #True
print(love(100,94)) #True
print(love(10,4)) #True
print(love(4,5)) #False


