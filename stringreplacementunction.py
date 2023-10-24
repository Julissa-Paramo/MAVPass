'''
Julissa Paramo 
10 / 23 / 23
Replacing vowel with #
'''

# functions
# strings

user_input = input() # get in put from user

new_string = '' # new empty string to change vowel characters

for char in user_input: # for each character in the string
  
  if char in 'aeiou': # if char is in the string containing a,e,i,o,u . . .
    
    new_string += '#' # replaced with symbol
    
  else:
    
    new_string += char # if not a vowel just gets added to new string as itself
    
