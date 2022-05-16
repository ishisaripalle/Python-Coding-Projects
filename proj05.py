#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 18:00:29 2022

@author: ishitasaripalle
"""


def open_file():
    '''the user input determines the wave data file opened and if there is no file 
    there is an error and a error statement prompts the user to choose another year. there are no
    parameters for this function because it is a file pointer function'''
    while True:      
        try: 
            year = input("Input a year: ")
            fp = open("wave_data_" + year + ".txt", "r")
            return fp
        except FileNotFoundError:
            print("File does not exist. Please try again.")
           
        
def get_month_str(num):
    '''the user input for num will determine the month returned and this is used in the main function.
    the parameter is num'''
    if num == '01':
       return 'Jan'
    if num == '02':
       return 'Feb'
    if num == '03':
       return 'Mar'
    if num == '04':
       return 'Apr'
    if num == '05':
       return 'May'
    if num == '06':
       return 'Jun' 
    if num == '07': 
       return 'Jul'
    if num == '08':
       return 'Aug'
    if num == '09':
       return 'Sep'
    if num == '10':
       return 'Oct'
    if num == '11':
       return 'Nov'
    if num == '12':
       return 'Dec'

def best_surf(mm,dd,hr,wvht,dpd,best_mm,best_dd,best_hr,best_wvht,best_dpd):
    '''this function compares the best wave data to the given wave data between 6am and 7 pm and 
    returns the data based on whether the current wave height is greater than the best wave height, 
    if its less than, or equal to, which is where dpd is considered too. the parameters are mm,dd,hr,wvht,dpd,
    best_mm,best_dd,best_hr,best_wvht,best_dpd which represents the month, day, hours, wave height, dpd'''
    if hr > 6 and hr < 19:       
        if wvht > best_wvht or (wvht == best_wvht and dpd > best_dpd): 
            return mm, dd, hr, wvht, dpd
        else: 
            return best_mm,best_dd,best_hr,best_wvht,best_dpd
    else: 
        return best_mm,best_dd,best_hr,best_wvht,best_dpd
    

def main():  
    print("Wave Data") 
    best_mm = 0
    best_dd = 0 
    best_hr = 0 
    best_wvht = 0 
    best_dpd = 0 
    
    max_wvht = 0 
    min_wvht = 10 ** 6 
    
    total = 0 
    count = 0 
    
    fp = open_file()
    fp.readline() 
    fp.readline() 
    
    for line in fp: 
        wvht = float(line[30:36].strip())
        dd = line[8:10].strip()
        mm = line[5:7].strip()
        hr = int(line[11:13].strip())
        dpd = float(line[37:42].strip())

        if wvht == 99 or dpd == 99:
            continue
        best_mm, best_dd, best_hr,best_wvht,best_dpd = best_surf(mm,dd,hr,wvht,dpd,best_mm,best_dd,best_hr,best_wvht,best_dpd)
        
        if max_wvht < wvht:
            max_wvht = wvht
    
        elif min_wvht > wvht:
            min_wvht = wvht
    
        total += wvht
        count += 1
    
    average_wvht = total/count
    print("\nWave Height in meters.")
    print("{:7s}: {:4.2f} m".format("average", average_wvht))
    print("{:7s}: {:4.2f} m".format("max", max_wvht))
    print("{:7s}: {:4.2f} m".format("min", min_wvht))
    
    print("\nBest Surfing Time:")
    print("{:3s} {:3s} {:2s} {:>6s} {:>6s}".format("MTH","DAY","HR","WVHT","DPD"))
    best_mm = get_month_str(best_mm)
    print("{:3s} {:>3s} {:2d} {:5.2f}m {:5.2f}s".format(best_mm, best_dd, best_hr, best_wvht, best_dpd))

# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__": 
    main()