#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 18:01:26 2022

@author: ishitasaripalle
"""
import math 

print("Welcome to Horizons car rentals")
print("At the prompts, please enter the following: ")
print("Customer's classificiation code (a character: BD, D, W) ")
print("Number of days the vehicle was rented (int) ")
print("Odometer reading at the start of the rental period (int) ")
print("Odometer reading at the end of the rental period (int)")

answer = (input("Would you like to continue (A/B)?"))


while answer == 'A':
    code = (input("Customer code (BD, D, W): "))
    days = (int(input("Number of days: ")))
    start = (int(input("Odometer reading at the start of the rental period: ")))
    end = (int(input("Odometer reading at the end of the rental period: ")))
    miles_travelled = end - start
    
    if miles_travelled < 0: 
        miles_travelled += 100000
        miles_travelled = round(miles_travelled, 1)
    
    if code == 'BD':
       base_charge = (days * 40) + (0.25*(miles_travelled))
       base_charge = round(base_charge, 2)
       
    elif code == 'D':
       base_charge = 60 * days
       mileage = (miles_travelled/days)
       if mileage <= 100:
          amount_due = float(round(base_charge))
       if miles_travelled > 100:
           f_mileage = mileage - 100
           amount_due = float(round(base_charge + (days * 0.25 * f_mileage)))
        
    elif code == 'W':      
        weeks = math.ceil(days/7) + (days%7/days%7)
        weekly_price = weeks * 190
        avg_miles = miles_travelled/weeks
        if avg_miles<= 900:
            amount_due = round(weekly_price, 2)
            amount_due = float(amount_due)
        elif avg_miles > 900 and avg_miles <= 1500:
            amount_due = round(weekly_price + (weeks * 100), 2)
            amount_due = float(amount_due)
        elif avg_miles > 1500: 
            amount_due = (weekly_price + (200 * weeks) * ((miles_travelled-(1500 * (weeks))) * 0.25))
            amount_due = float(round(amount_due, 2)) 
   
    print("Customer summary")
    print("classificiation code: ", code)
    print("odometer reading at start: ", start)
    print("odometer reading at start: ", end)
    print("number of miles driven: ", miles_travelled)
    print("amount due: $", amount_due)

if answer == 'B':
    print("Thank you for your loyalty.")
   
    
        
    