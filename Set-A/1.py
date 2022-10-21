'''
WAP to reverse a String

'''
'''method-1'''
def reverse(sen):
    reverse_string=''
    for i in sen:
        reverse_string=i+reverse_string
    return reverse_string
sen=input('Enter Any String \n -> ')
print(f'Reverse of {sen} is \n {reverse(sen)}')



'''
method-2
print(sen[::-1])

'''


    