#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 13:34:58 2022

@author: ishitasaripalle
"""
import math

num_rods = input('Input rods: ')
num_rods = float(num_rods)
print("You input", num_rods, "rods.")
print("\n")
print("Conversions")

num_meters = 5.0292 * num_rods
print("Meters:", round(num_meters, 3))


num_feet = num_meters/0.3048
print("Feet: ", round(num_feet, 3))


num_miles = num_meters/1609.34
print("Miles:", round(num_miles, 3))


num_furlongs = num_rods/40
print("Furlongs:", round(num_furlongs, 3))


num_walk = (num_miles/3.1) * 60
print("Minutes to walk", num_rods, "rods:", round(num_walk, 3))




