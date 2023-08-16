# -*- coding: utf-8 -*-
"""
Author(s): Yuneydy Paredes
Consulted:
Date: 4/24/2023
Purpose: Yelp task: Working with dictionaries and tuples and
    real world data. YELP data set covers different metropolitan areas
    in 4 countries (not including Boston).
"""

#---------#
# Imports #
#---------#

# This will be needed to access JSON loading and storing functions.
import json

#---------------------------#
# Write your functions here #
#---------------------------#

def loadData(fileName):
    '''
    This function accepts a single parameter as the fileName and
    loads the content of the given file into a python object.
    '''
    with open(fileName, 'r', encoding="utf-8") as f:
        opened = json.load(f)
    return opened

def getBusinessCount(yelpDict, businessName):
    '''
    This function accepts a dict and a business name as parameters
    (which ignores the case). It then returns an integer count of
    how many times the business is mentioned.
    '''
    num = 0
    businessNames = []
    for bizID in yelpDict:
        businessNames.append(yelpDict[bizID]['name'].lower())
    for name in businessNames:
        if businessName.lower() == name:
            num+=1
        else:
            num = num
    return num

def uniqueCities(yelpDict):
    '''
    This function accepts a dict and puts all the cities into a list.
    If the city is already in the list, it will not be added. Once all
    unique cities are added, the list is returned sorted.
    '''
    listOfCities = []
    for bizID in yelpDict:
        if yelpDict[bizID]['city'] in listOfCities:
            listOfCities = listOfCities
        else:
            listOfCities.append(yelpDict[bizID]['city'])
    return sorted(listOfCities)

def findBusinesses(yelpDict, category, city, starLimit, minReview, outFilename):
    '''
    This function gathers all the businesses in a given city and category
    that meet the minimum star limit and minimum number of reviews within
    a given dictionary.
    '''
    bizes = []
    for bizID in yelpDict:
    # appending values
        if yelpDict[bizID]['city'] == city and category in yelpDict[bizID]['categories'] and yelpDict[bizID]['stars'] >= starLimit and yelpDict[bizID]['review_count'] >= minReview:
            bizes.append(yelpDict[bizID])
    print(bizes)
    print('')
    # helper function for star count and Business name
    def starsAndNames(biz):
       return (biz['stars'], biz['name'])
    # sorting values by stars helper function
    bizes = sorted(bizes, key = starsAndNames)
    print(bizes)
    with open(outFilename, 'w', encoding="utf-8") as f:
        new = json.dump(bizes, f, indent=2, sort_keys=True) 
    return new


def findCategories(yelpDict, threshold):
    '''
    This function  returns a dictionary, where the keys are category names
    that appear in yelpDict and the values are the number of businesses
    in that category.
    '''
    newCategoriesDict ={}
    for bizID in yelpDict:
        for cat in yelpDict[bizID]['categories']:
            if cat in newCategoriesDict:
                newCategoriesDict[cat] += 1
            else:
                newCategoriesDict[cat] = 1
    print(newCategoriesDict)
    print('')
    # Implement threshhold
    for cat in list(newCategoriesDict.keys()):
        if newCategoriesDict[cat] < threshold:
            newCategoriesDict.pop(cat)
    print(newCategoriesDict)
    return newCategoriesDict

def bestPizzaPlace(yelpDict):
    '''
    This function  returns a list containing one or more business dictionaries
    from the given yelpDict with 'Pizza' as a category that have the highest
    star rating.
    '''
    pizzaPlaces = []
    for bizID in yelpDict:
        for cat in yelpDict[bizID]['categories']:
            if cat.lower() == 'pizza':
                pizzaPlaces.append(yelpDict[bizID])
    print(pizzaPlaces)
    # stars threshold
    best = []
    for biz in pizzaPlaces:
        if biz['stars'] >= 5:
            best.append(biz)
    print(best)
    return best
#--------------#
# Testing data #
#--------------#

soloYelp = {
  "XguKrY0dAuaK1W6HUlUQ1Q": {"state": "OH", "address": "547 Sackett Ave", "review_count": 29, "stars": 3.5, "name": "Retz's Laconi's II", "city": "Cuyahoga Falls", "categories": ["Italian", "Restaurants", "Pizza"]}
}

microYelp = {
  "PMH4oUa-bWELKogdtkWewg": {'state': 'ON', 'address': '100 City Centre Dr', 'review_count': 16, 'stars': 2.0, 'name': 'GoodLife Fitness', 'city': 'Mississauga', 'categories': ['Fitness & Instruction', 'Sports Clubs', 'Gyms', 'Trainers', 'Active Life']},
  "XguKrY0dAuaK1W6HUlUQ1Q": {'state': 'OH', 'address': '547 Sackett Ave', 'review_count': 29, 'stars': 3.5, 'name': "Retz's Laconi's II", 'city': 'Cuyahoga Falls', 'categories': ['Italian', 'Restaurants', 'Pizza']},
  "Wpt0sFHcPtV5MO9He7yMKQ": {'state': 'NV', 'address': '3020 E Desert Inn Rd', 'review_count': 20, 'stars': 2.0, 'name': "McDonald's", 'city': 'Las Vegas', 'categories': ['Restaurants', 'Fast Food', 'Burgers']},
  "1K4qrnfyzKzGgJPBEcJaNQ": {'state': 'ON', 'address': '1058 Gerrard Street E', 'review_count': 39, 'stars': 3.5, 'name': 'Chula Taberna Mexicana', 'city': 'Toronto', 'categories': ['Tiki Bars', 'Nightlife', 'Mexican', 'Restaurants', 'Bars']},
  "7gquCdaFoHZCcLYDttpHtw": {'state': 'SC', 'address': '8439 Charlotte Hwy', 'review_count': 17, 'stars': 4.0, 'name': 'Bubbly Nails', 'city': 'Fort Mill', 'categories': ['Nail Salons', 'Beauty & Spas']},
  "Mmh4w2g2bSAkdSAFd_MH_g": {'state': 'SC', 'address': '845 Stockbridge Dr', 'review_count': 77, 'stars': 3.0, 'name': 'Red Bowl', 'city': 'Fort Mill', 'categories': ['Restaurants', 'Asian Fusion']},
  "vMO2vNyWLuxumso7t3rbYw": {'state': 'ON', 'address': '300 Borough Drive', 'review_count': 5, 'stars': 4.0, 'name': "Pablo's Grill It Up", 'city': 'Scarborough', 'categories': ['Food Court', 'Restaurants', 'Barbeque']},
  "h2XsV6mR6c7QURhlsi0RqA": {'state': 'AZ', 'address': '211 E 10th Dr, Ste 2', 'review_count': 26, 'stars': 4.5, 'name': "John's Refrigeration Heating and Cooling", 'city': 'Mesa', 'categories': ['Home Services', 'Air Duct Cleaning', 'Local Services', 'Heating & Air Conditioning/HVAC']},
  "c6Q3HP4cmWZbD9GX8kr4IA": {'state': 'NC', 'address': '4837 N Tryon St', 'review_count': 8, 'stars': 3.5, 'name': 'Pep Boys', 'city': 'Charlotte', 'categories': ['Auto Parts & Supplies', 'Auto Repair', 'Tires', 'Automotive']},
  "1EuqKW-JC-Fm3RSWRqKdrg": {'state': 'NV', 'address': '2075 E Warm Springs Rd', 'review_count': 5, 'stars': 5.0, 'name': 'Life Springs Christian Church', 'city': 'Las Vegas', 'categories': ['Religious Organizations', 'Churches']},
  "VZ37HCZVruFm-w_Mkl1aEQ": {'state': 'AZ', 'address': '13637 N Tatum Blvd, Ste 8', 'review_count': 16, 'stars': 5.0, 'name': 'Conservatory of Dance', 'city': 'Phoenix', 'categories': ['Education', 'Dance Schools', 'Arts & Entertainment', 'Fitness & Instruction', 'Specialty Schools', 'Active Life', 'Dance Studios', 'Performing Arts']},
  "htKaC4cHY4wlB4Wqb8CDnQ": {'state': 'PA', 'address': '4730 Liberty Ave', 'review_count': 4, 'stars': 4.0, 'name': 'Allure', 'city': 'Pittsburgh', 'categories': ['Accessories', "Women's Clothing", 'Fashion', 'Shopping']},
  "7fiIMBxbOYdAv3XMcmWivw": {'state': 'OH', 'address': '850 Euclid Ave', 'review_count': 3, 'stars': 3.0, 'name': "Renee's Relaxation and Body Mechanics", 'city': 'Cleveland', 'categories': ['Massage', 'Beauty & Spas']},
  "4SBY4CHiMD8YOCEU9_fdnw": {'state': 'ON', 'address': '123 Queen Street W', 'review_count': 3, 'stars': 4.0, 'name': 'Fidora Salon and Spa', 'city': 'Toronto', 'categories': ['Day Spas', 'Hair Salons', 'Beauty & Spas']},
  "6aFAEeJ3nS-iWGt7Tn7S0Q": {'state': 'NC', 'address': '19925 Jetton Rd, Ste 100', 'review_count': 5, 'stars': 5.0, 'name': 'KS Audio Video', 'city': 'Cornelius', 'categories': ['Home Services', 'Television Service Providers', 'Home Automation', 'Home Theatre Installation', 'Professional Services']},
}
bestPizzaPlace(microYelp)