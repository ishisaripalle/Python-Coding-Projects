#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###########################################################
#  Computer Project #7
#
#  Algorithm
#    prompt for an option 
#    execute while loop for option input
#       display error messgae if input not valid 
#       prompt for country, regime, or display if input is valid 
#       call to function based on option 
#       run function 
#       if input is q quit program 
#    display closing message
###########################################################

import csv
from operator import itemgetter

REGIME=["Closed autocracy","Electoral autocracy","Electoral democracy","Liberal democracy"]
MENU='''\nRegime Options:
            (1) Display regime history
            (2) Display allies
            (3) Display chaotic regimes        
    '''

def open_file():
    ''' function opens file based on user input. 
        
        the function utilizes try and except to take the user 
        input and open the according file and if the file does 
        not exist an error message will be displayed. 
        
        Parameters: none
        
        Returns: file point'''
    while True:
        try:
            filename = input("Enter a file: ")
            fp = open(filename)
            return fp
        except FileNotFoundError:
            print("File not found. Please try again.")
        
def read_file(fp):
    ''' function reads the file accessed in open_file(). 
        
        the function uses a for loop to access elements in 
        the file and checks to see if an element is equilvent 
        to the next elemnt in the list and if they are 
        different the second elemnt will be appened to the list of 
        country names
        
        Parameters: fp (file pointer)
        
        Returns: country_names (list), list_of_regime_lists (list of lists )'''
    country_names = []
    list_of_regime_lists = []
    file = csv.reader(fp)
    next(file, None)
    first_line = next(file,None)
    previous_country = first_line[1]
    country_names.append(previous_country)
    regimes = [int(first_line[4])]
    for i in file:
        country_name = i[1]
        regime = int(i[4])
        if country_name != previous_country:
            previous_country = country_name
            list_of_regime_lists.append(regimes)
            regimes = [regime]
            country_names.append(country_name)
        else: 
            regimes.append(regime)
    list_of_regime_lists.append(regimes)
    return country_names, list_of_regime_lists
        
        
def history_of_country(country,country_names,list_of_regime_lists):
    ''' function return regime type based on dominant reigme type 
        
        the function counts how many times 0,1,2, or 3 appear in 
        lists within list_of_regime_lists and returns the 
        approprate regimate by using the max function to see 
        which regime appears the most
        
        Paramaters: country (element), country_names (list), 
        list_of_regime_lists (list of lists)
        
        Returns: REGIME (elements from list)'''
    i = country_names.index(country)
    dominant_regime = max(list_of_regime_lists[i].count(0), list_of_regime_lists[i].count(1), list_of_regime_lists[i].count(2), list_of_regime_lists[i].count(3))
    if dominant_regime == list_of_regime_lists[i].count(0):
        return REGIME[0]
    if dominant_regime == list_of_regime_lists[i].count(1):
        return REGIME[1]
    if dominant_regime == list_of_regime_lists[i].count(2):
        return REGIME[2]
    if dominant_regime == list_of_regime_lists[i].count(3):
        return REGIME[3]
    
def historical_allies(regime,country_names,list_of_regime_lists):
    ''' function creates list of all the countries under one regime 
        
        the function creates an empty list and accesses country_names 
        list through a for loop and accesses the previous function by 
        calling it and seeing if the return value is equivalent 
        to regime and if it is it will append the country to the empty list
        
        Parameters: regime (element), country_names (list),
        list_of_regime_lists (list of list)
        
        Returns: list_of_allies'''
    list_of_allies = []
    for country in country_names:
        if history_of_country(country,country_names,list_of_regime_lists) == regime:
            list_of_allies.append(country)
        list_of_allies.sort()    
    return list_of_allies

def top_coup_detat_count(top, country_names,list_of_regime_lists):          
    ''' function coutns how many times regimes chnage in list_of_regime_lists 
        
        the function creates a count and uses to for loops to accces 
        the elements within list_of_regime_lists and every time the 
        current element is different from the previous elemnt 
        one of added to the count until the for loops are 
        cone iterating and return a spliced version of the list
        
        Parameters: top (int), country_names (list),
        list_of_regime_lists (list of lists)
        
        Returns: new_list (list)'''
    num_of_coups = 0 
    new_list = []
    for i in range(len(list_of_regime_lists)):
        for x in range(len(list_of_regime_lists[i])-1):
            if list_of_regime_lists[i][x] != list_of_regime_lists[i][x+1]:
                num_of_coups += 1
        tuple1 = (country_names[i], num_of_coups)  
        new_list.append(tuple1)
        num_of_coups = 0 
        new_list.sort()
        new_list.sort(key = itemgetter(1), reverse = True) 
    return new_list[:top] 

def main():
    # by convention "main" doesn't need a docstring
    fp = open_file()
    country_names, list_of_regime_lists = read_file(fp)
    print(MENU)
    option_input = input("Input an option (Q to quit): ").lower()
    while option_input not in ['q', '1', '2', '3']:
        print("Invalid choice. Please try again.")
        option_input = input("Input an option (Q to quit): ").lower()
    
    while option_input != 'q':
        if option_input == '1':
            country_input = input("Enter a country: ")
            while country_input not in country_names:
                print("Invalid country. Please try again.")
                country_input = input("Enter a country: ")
            regime_type = history_of_country(country_input, country_names, list_of_regime_lists)
            if regime_type[0].lower() in ['a', 'e', 'i', 'o', 'u']:
                print("\nHistorically {} has mostly been an {}".format(country_input, regime_type))
            else: 
                print("\nHistorically {} has mostly been a {}".format(country_input, regime_type))
        if option_input == '2':
            regime_input = input("Enter a regime: ")
            while regime_input not in REGIME: 
                print("Invalid regime. Please try again.")
                regime_input = input("Enter a regime: ")
            if regime_input in REGIME:
                print("\nHistorically these countries are allies of type: {}\n".format(regime_input))
                for i,j in enumerate(historical_allies(regime_input, country_names, list_of_regime_lists)):
                    if i == len(historical_allies(regime_input, country_names, list_of_regime_lists)) - 1:
                        print(j)
                    else:
                        print(j, end = ", ")
        if option_input == '3':
            display_input = input("Enter how many to display: ")
            while display_input.isdigit() == False: 
                print("Invalid number. Please try again.")
                display_input = input("Enter how many to display: ")
            if display_input.isdigit() == True:
                display_input = int(display_input)
                print("\n{: >25} {: >8}".format('Country', 'Changes'))
                top_coup_list = top_coup_detat_count(display_input, country_names, list_of_regime_lists)
                for i in top_coup_list:  
                    print("{: >25} {: >8}".format(i[0], i[1]))
        print(MENU)
        option_input = input("Input an option (Q to quit): ").lower()
        while option_input not in ['q', '1', '2', '3']:
            print("Invalid choice. Please try again.")
            option_input = input("Input an option (Q to quit): ").lower()
    print("The end.")
    
# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__": 
    main() 