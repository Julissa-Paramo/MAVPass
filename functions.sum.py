'''
Julissa Paramo
10 / 16 / 23
Function for sum of two numbers
'''

# Funtion , name , parameters
def add_numbers(num1,num2):

    return num1 + num2 # returns the sum of the two variables
  

user_num1 = int(input()) # first parameter

user_num2 = int(input()) # second parameter

sum = add_numbers(user_num1,user_num2) # new variable for invoking the function

print(sum) # prints the sum!
