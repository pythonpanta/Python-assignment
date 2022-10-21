'''

WAP to sum all elements in the array.
it should sum only the numbers which are greater than zero
'''


def sum(array):
  sum=0
  for num in array:
      if num>0:
          sum+=num
  return sum
myarray=[45,555,7,9,0,2,-3, -100,3,5,100]
print(sum(myarray))
'''
output:
726
'''


