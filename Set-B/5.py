'''
WAP to find the first prime number in array
'''



# function to check whether number is prime or not 
def isPrime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True

myarray=[100,21,33,19,2,4,7,4,5,9,11]
# myarray=[4,6,8]

for i in myarray:
    if isPrime(i):
        print(f'First Prime Number in array is {i}')
        break
else:
    print('Not any prime number in array')
'''
output:
First Prime Number in array is 19
'''
