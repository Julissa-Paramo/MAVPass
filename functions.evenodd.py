'''
Juissa Paramo
10 / 16 / 23
T or F for even and odd
'''
# print True for even and False for odd
# boolean statements
# functions

def is_even(num):

    if num % 2 == 0: # checks for even

        return True
    
    else: # if not even, then odd

        return False
    

def is_even_simplified(num): # simplified function for ^^^
    
    return num % 2 == 0 # will return the boolean
