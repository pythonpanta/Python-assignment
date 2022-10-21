'''
WAP to sort an array
'''

# sorting an array  in ascending order

def sortarray(myarray):
  for i in range(len(myarray)):
      for j in range(i+1,len(myarray)):
          if myarray[i]>myarray[j]:
              temp=myarray[i]
              myarray[i]=myarray[j]
              myarray[j]=temp
  return myarray

myarray=[45,555,7,9,0,2,3,5,100]
print(sortarray(myarray))
'''
output:
[0, 2, 3, 5, 7, 9, 45, 100, 555]
'''

