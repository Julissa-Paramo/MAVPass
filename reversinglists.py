'''
Julissa Paramo
10 / 9 / 23
Reversing a List
'''

#reversing a list without using reverse() method

words = ['apple','banana','cherry', 'date']

reversed_words = []

for i in words.pop():

  reversed_words.append(i)

print(reversed_words)
