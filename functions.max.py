'''
Juissa Paramo
10 / 16 / 23
Function for finding the Max
'''

# functions
# lists

def find_max(listA): # function name and parameters

  max = listA[0] # assigns the first element in the list as the max automatically
  
  if len(listA) == 0: # if the length is 0, prints an error

    print('empty list')

  else: # if there is data in the list
  
    for num in listA: # iterates through all the numbers in the list
    
        if num > max: # if number is greater than the previosly assigned num

            max = num # that num will be the new max

    return max # returns the max


numlist = [-1,-2,0,-3] # function in action

print(find_max(numlist)) # returns 0
