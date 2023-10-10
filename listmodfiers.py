'''
Julissa Paramo
10 / 9 / 23
Modifying Lists
'''

nums = [1,2,3,4,5] 

popped_element = nums.pop() # returns the last element in the list



num_list = [1,1,2,3,4,5,3,3,8,4]

unique_nums = [] # empty list

for i in num_list: # goes through all elements

  if not in unique_nums: # if the element isn't in the list

    unique_nums.append(i) # it will get added to the end of the list
                          # this will skip any duplicates
print(unique_nums)
