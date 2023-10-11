'''
Julissa Paramo
10 / 10 / 23
Fall Activities Dictionaries
'''
# dictionary containing lists
# for loops

dict = {'Pumpkin Carving': [25,30], # keys are fall activites
        'Haunted House': [15,120], # index 0 is the cost
        'Apple Picking': [15,20], # index 1 is the duration of the activity in minutes
        'Ghost Stories': [1.99,5]
        }

def find_longest_activity(dict):

    max = 0

    for key, value in dict.items():

        if dict[key][1] > max:

            max = dict[key][1]

            name = key
            
    return name

print(find_longest_activity(dict))
