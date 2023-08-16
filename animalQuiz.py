"""
Authors: Yuneydy Paredes
Consulted: -----
Date: 2023-2-23
""" 
def boolFromResponse(word):
    '''
    Takes a word and determines whether it begins with the letter y. The function
    returns a boolean value depending on the word:
    True for y and False for anything else
    '''
    return word.startswith('Y')or word.startswith('Y'.lower())

def boolFromUser(prompt):
    '''
    Takes a prompt and retrieves an answer. Using boolFromReponse, it determines
    if the answer is true or false according to boolFromResponse.
    '''
    answer= input(prompt)
    return boolFromResponse(answer)

def chooseAnimal(q1,q2,q3):
    '''
    The parameters can take boolean values that will determine the animal the
    function should return. Depending on the order, there is a potential for 8
    different outputs.
    '''
    if q1==True and q2==True and q3==True:
        return 'polar bear'
    elif q1==True and q2==True and q3==False:
        return 'orca'
    elif q1==True and q2==False and q3==True:
        return 'tiger'
    elif q1==True and q2==False and q3==False:
        return 'komodo dragon'
    elif q1==False and q2==True and q3==True:
        return 'yak'
    elif q1==False and q2==True and q3==False:
        return 'clam'
    elif q1==False and q2==False and q3==True:
        return 'bunny'
    elif q1==False and q2==False and q3==False:
        return 'tortoise'

def animalQuiz():
    '''
    Stores the answer of boolFromUser into three different variables relating to the
    question asked. Based on the boolean values retrieved from boolFromUser, we then
    use another variable to store what exactly the animal should be. The variables named
    before, meat, cold, and fuzzy, will go in order accordingly to make sure
    chooseAnimal() runs to give the correct answer
    '''
    print("What animal are you? Let's find out!")
    meat= boolFromUser('Do you like to eat meat? ')
    cold= boolFromUser('Do you like cold weather? ')
    fuzzy= boolFromUser('Do you like fuzzy things? ')
    animal = chooseAnimal(meat, cold, fuzzy)
    print(' ')
    print('Your animal is the ' + animal)