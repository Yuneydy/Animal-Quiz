"""
Authors: Yuneydy Paredes
Consulted: -----
Date: 2023-3-23
"""
def printInventory(trains):
    '''
    Prints car # with all contents inside: lists weight (w/ kg) and item, with each item
    on separate lines
    '''
    for i in range(len(trains)):
        print( 'Car #' + str(i))
        for n in range(len(trains[i])):
            print('  ' + str(trains[i][n][1]) + ' kg ' + str(trains[i][n][0]))

def totalWeightOf(train, item):
    '''
    Adds the weight of tuples containing the item given as an argument.
    '''
    weight = 0
    for i in range(len(train)):
        for n in range(len(train[i])):
           if train[i][n][0] == item:
               weight += train[i][n][1]
    return weight

def listItems(train, item):
    '''
    Appends tuples to list items that contain the item given as an argument.
    Returns items list containing all instances of the listed item.
    '''
    items = []
    for i in range(len(train)):
        for n in range(len(train[i])):
           if train[i][n][0] == item:
               items.append(train[i][n])
    return items

def listWeights(train):
    '''
    For each 'Train car' in train, the weights are added up and then have their final
    sum added to a new list, weightList.
    '''
    weightsList = []
    summedUp = 0
    for i in range(len(train)):
        for n in range(len(train[i])):
            summedUp += train[i][n][1]
        weightsList.append(summedUp)
        summedUp = 0
    return weightsList

def heaviestCar(train):
    '''
    Using the listWeights function, it stores the results in a variable 'weights'
    and then compares each value in the list to the max in order to find the largest value,
    whose index it will return.
    
    '''
    weights = listWeights(train)
    for i in range(len(weights)):
        if weights[i] == max(weights):
            return i
    else:
        heaviest = heaviest

# Inventory by weight
def itemWeight(item):
    '''
    returns the weight of the item, index = 1
    '''
    return item[1]

def inventoryByWeight(train):
    '''
    Returns a list of tuples sorted by their 
    '''
    sortedlist = []
    for i in range(1, len(train)):
        if train[i][1] > train[i-1]:
            sortedlist.append(train[i])
        else:
            sortedlist.insert(0, train[i])
    return sortedlist
    
    
    
    
    
    