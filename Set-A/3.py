'''WAP to count number of word in string'''


sentence='Nepal Is The Most Beautiful Country In The World.'
# split a sentence into word 
words=sentence.split(' ')
# remove the duplicate word 
unique_word=[]
for word in words:
    if word not in unique_word:
        unique_word.append(word)
print(f'Number of Unique word in String is {len(unique_word)}')

# output 
'''
Number of Unique word in String is 8
'''

