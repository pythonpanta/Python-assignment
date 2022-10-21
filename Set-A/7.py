'''

Given a string, return true if the first instance of 'x' in the string is immediately followed by another 'x'
example:
doubleX('axxbb')->true
doubleX('axaxax)->false
doubleX('xxxx')->true

'''

def doubleX(word):
  for i in range(len(word)-1):
      if word[i]+word[i+1]=='xx':
          return True
  return False
print(doubleX('axxbb'))
print(doubleX('axaxax'))
print(doubleX('xxxx'))
print(doubleX('aabbxccdd'))

