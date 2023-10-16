'''
Julissa Paramo 
10 / 16 / 23
Word Counter
'''

# dicitonaries
# counting how many words in a sentence
# functions

def word_counter(words): # parameter is user input

    words_list = words.split() # creates  a list from the input of words

    words_dict = {} # empty dictionary 

    for word in words_list: # for each element in the list

        if word in words_dict: 

            words_dict[word] = words_dict[word] + 1 # if the word reappears, the value increases by 1

        else:

            words_dict[word] = 1 # if the word is not in the dictionary the value is set to 1 ( 1 occurence of the word )

    return words_dict

sentence = input()

print(word_counter(sentence))
