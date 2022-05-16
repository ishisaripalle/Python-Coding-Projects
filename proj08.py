#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###########################################################
#  Computer Project #8
#
#  Algorithm
#    display headers
#       loop through dictionary to get country equal to region 
#    display header again
#       loop through dictionary to print all countries for region 
#    print maximum capita with max function 
#    print minimum capita with min function
#    print dashed lins to indicate table is complete 
#    display closing message
###########################################################

import csv
from operator import itemgetter

def open_file():
    ''' function opens file based on user input. 
        
        the function utilizes try and except to take the user 
        input and open the according file and if the file does 
        not exist an error message will be displayed. 
        
        Parameters: none
        
        Returns: file pointer'''   
    while True: 
        try: 
            filename = input("Input a file: ")
            fp = open(filename)
            return fp
        except FileNotFoundError:
            print("Error: file does not exist. Please try again.")
           
def read_file(fp):
    ''' function prints dictionary with list of lists as the values.
        
        the function iterates through each line of the file specified
        in open_file() and checks whether the first value is in the 
        dicionary and it won't be because the dictionary is empty so 
        an empty list is created and a list with the country, diabetes, 
        and population values is created and appened to the empty list 
        to create a list of lists that is then sorted and returned. 
        
        Parameters: fp (file pointer)
        
        Returns: region_data (dictionary with list of lists as values)'''
    file = csv.reader(fp)
    next(file, None)
    region_data = {}
    for line in file:
        try:
            region = line[1]
            if region not in region_data:
                region_data[region] = []
            value_list = [line[2], float(line [9]), float(line[5].replace(',', ''))]
            region_data[region].append(value_list)
        except: 
            continue
    for i in region_data:
        region_data[i].sort()
    return region_data
  
def add_per_capita(D):
    ''' function appends capita value to list of lists values 
        
        the function creates a for loop and sets countries_data
        equal to the values in D (the dictionary) and then 
        uses try and except to divide the 2nd and 3rd elements of 
        every smaller lists within the list of lists to create a 
        capita value which is then appended to the smaller 
        list and if there is a zero division error 0.0 is appended 
        and finally the dictionary is returned. 
        
        Parameters: D (dictionary)
        
        Returns: D (dictionary)'''
    for key in D:  
        countries_data = D[key]
        for i in countries_data:
            try:
                capita_value = (i[1])/(i[2])
                i.append(capita_value)
            except ZeroDivisionError:
                countries_data.append(0.0)
    return D
    
def max_in_region(D,region):
    ''' function returns largest capita value for region 
        
        the function intilizes two values, max_capita and 
        max_country, and then iterates through countries_data 
        which is the values of D (the dictionary) and if the
        fourth element in the smaller lists within the bigger 
        list is larger than 0 and afterward larger than the 
        previous fourth it becomes the new max_capita and the 
        country is the first element of that same list and those 
        values are returned as a tuple.
        
        Parameters: D (the dictionary), region(the key for the D)
        
        Returns: max_country (first element of list with the largest 
        capita value), max_capita (largest capita value)'''
    countries_data = D[region]
    max_capita = 0 
    max_country = ''
    for i in countries_data:
        if i[3] > max_capita:
            max_capita = i[3] 
            max_country = i[0]
    return max_country, max_capita
                
    '''Insert Docstring here'''
    pass   # replace this line with your cod
def min_in_region(D,region):
    ''' function returns smallest capita value for region 
    
        the function intilizes two values, min_capita and 
        min_country, and then iterates through countries_data 
        which is the values of D (the dictionary) and if the
        fourth element in the smaller lists within the bigger 
        list is less than 1000000000000000000 and afterward smaller
        than the previous fourth it becomes the new min_capita and the 
        country is the first element of that same list and those 
        values are returned as a tuple.
        
        Parameters: D (the dictionary), region(the key for the D)
        
        Returns: min_country (first element of list with the smallest 
        capita value), min_capita (smallest capita value)'''
    countries_data = D[region]
    min_capita = 1000000000000000000
    min_country = ''
    for i in countries_data:
        if i[3] < min_capita and i[3] != 0:
            min_capita = i[3] 
            min_country = i[0]
    return min_country, min_capita

def display_region(D,region):
    ''' function displays the data from file in table format
        
        the function prints two headers and then uses a for loop to 
        see if the first element of a smaller list is eequal to the key 
        and if it is the values are printed in table format and then 
        another for loop is used if the value isn't equal to the region 
        and a new header is printed with country, diabetes, and population 
        values printed in table format followed by maxiumum and miniumum 
        per capita values printed in table format 
        
        Paramters: D (the dictionary), region (the key for the D)
        
        Returns: displays all the values within the dicitonary in 
        table format and the maximum and minimum per capita vlaues 
        in table format'''
    print("Type1 Diabetes Data (in thousands)")
    print("{:<37s} {:>9s} {:>12s} {:>11s}".format("Region","Cases","Population","Per Capita"))
    region_data = sorted(D[region], key=itemgetter(3), reverse=True)
    for i in region_data:
        if i[0] == region:
            print("{:<37s} {:>9.0f} {:>12,.0f} {:>11.5f}".format(i[0], i[1], i[2], i[3]))
    print("{:<37s} {:>9s} {:>12s} {:>11s}".format("Country","Cases","Population","Per Capita"))
    region_data = sorted(D[region], key=itemgetter(3), reverse=True)
    for i in region_data:
        if i[0] != region:
            print("{:<37s} {:>9.1f} {:>12,.0f} {:>11.5f}".format(i[0], i[1], i[2], i[3]))
    print("\nMaximum per-capita in the {} region".format(region))
    print("{:<37s} {:>11s}".format("Country","Per Capita"))
    print("{:<37s} {:>11.5f}".format(max_in_region(D,region)[0], max_in_region(D,region)[1]))
    print("\nMinimum per-capita in the {} region".format(region))
    print("{:<37s} {:>11s}".format("Country","Per Capita"))
    print("{:<37s} {:>11.5f}".format(min_in_region(D,region)[0], min_in_region(D,region)[1]))
    print("-"*72)
 
def main():
    fp = open_file()
    D = read_file(fp)
    add_per_capita(D)
    for key in D.keys(): 
        display_region(D,key)
    print('\n Thanks for using this program!\nHave a good day!')

# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__": 
    main()