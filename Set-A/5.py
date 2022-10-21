'''
WAP to find largest and smallest number in an array

'''



def max_and_min_value(array):
  smallest=array[0]
  largest=array[0]
  for num in array:
      if num<smallest:
          smallest=num
      if num>largest:
          largest=num
  return largest,smallest

array=[555,68,90,12,44,56,435]
max,min=max_and_min_value(array)
print(f'Largest Number in array={max}\nSmallest Number in array={min}')
# output 
'''
Largest Number in array=555
Smallest Number in array=12
'''
