'''
Juissa Paramo
10 / 16 / 23
Function for finding the Max
'''

# functions
# lists

def find_max(listA):

  max = listA[0]

if len(listA) == 0:

  print('empty list')

else:
  
  for num in listA:
    
    if num > max:

      max = num

numlist = [-1,-2,0,4]

print(find_max(numlist))
