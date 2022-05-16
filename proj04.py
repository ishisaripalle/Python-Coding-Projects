#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 21:30:25 2022

@author: ishitasaripalle
"""
'''this program has 4 functions, 2 of which are use the tridecimal system to rewrite a given input. then the zeta function uses an input to calculate a sum. the main function uses all these functions to create an overall program that takes inputs and converts them to the desired output'''


DELTA = 10**-7  # used for the zeta function

PROMPT = "Enter Z for Zeta, C for Conway, Q to quit: "

def int_to_base13(n):
    '''converts inputted number to a base 13 number by dividing with a constant of 13 and replacing any remainder of 10,11 or 12 with A, B, or C to create a new string'''
    n_quotient = n // 13  
    n_remainder = n % 13 
    n_str = ''
    if int(n) < 10 :
       return str(n)
    else:
        while n_quotient > 0:
            if n_remainder < 10:
                n_str += str(n_remainder)
            elif  n_remainder == 10: 
                n_str += 'A'
            elif  n_remainder == 11:
                n_str += 'B' 
            elif  n_remainder == 12:
                n_str += 'C'
            n_remainder = n_quotient % 13 
            if n_quotient < 10: 
               n_str += str(n_remainder)
            elif n_quotient == 10:
                n_str += 'A'
            elif n_quotient == 11:
                n_str += 'B'
            elif n_quotient == 12:
                n_str += 'C'
            n_quotient = n_quotient // 13
        return n_str[::-1]

def tridecimal_expansion(n_str):
    '''same as int_to_base13 except 10,11,and 12 are replaced with +,-, and .'''
    n_str = str(n_str)
    for i in range(len(n_str)):
        if n_str[i] == 'A':
            n_str = n_str.replace("A", "+")
        elif n_str[i] == 'B':
            n_str = n_str.replace("B", "-")
        elif n_str[i] == 'C':
            n_str =n_str.replace("C", ".")
    return n_str
        
def tridecimal_to_conway(n_str):
    '''this function takes the tridecimal expansion result and looks for a string that resembles a decimal and converts that string to a float'''
    #n = int(n_str)  
    #print(n_str)
    j = 0
    count = 0
    n_str_1 = ''
    n_str_2 = ''
    if n_str[-1].isnumeric() is False :
        return 0 
    else : 
        while (j < len(n_str) -1):
          if (n_str[j] == '.' and n_str[j+1] != '+' and n_str[j+1] != '-'):
            j = j
            count +=1
            break
          j += 1
        if count == 0 or j == len(n_str) - 1:
          return 0
        else :
          for i in range (j) : 
              if (n_str[j-i] == '+'):
                n_str_1 = n_str[j-i:j]
                break
              elif (n_str[j-i] == '-'):
                n_str_1 = n_str[j-i:j]
                break
              else  :
                n_str_1 = n_str[:j]
              
          for h in range (j+1,len(n_str)) :
            if n_str[h] == '+' or '-' or '.':
              n_str_2 = n_str[j:h+1]
            elif h == len(n_str)-1:
              n_str_2 = n_str[j:]
              break
            else: 
                n_str_2 = n_str[j:]

          return float(n_str_1 + n_str_2)

def zeta(s):
    '''this function takes an integer s and uses the infinite series expression to get a sum'''
    DELTA = 10 ** -7 
    sum = 1 
    n = 2
    if s <= 0: 
        return None
    elif s > 0: 
        while abs(1/(n ** s) - 1/((n-1) ** s)) > DELTA:
            sum += (1/(n**s))
            n += 1
        return sum

def main():
    print("Functions")
    function = input("Enter Z for Zeta, C for Conway, Q to quit: ").lower()
    while function != 'q':
            if function == 'z':
                print("Zeta")
                s = input("Input a number: ")
                if s[0] == '-' and s[1:].isnumeric() is True :
                    print(zeta(int(s)))
                    function = input("Enter Z for Zeta, C for Conway, Q to quit: ").lower()  
                else :
                    while s.isalpha() is True:
                        print("Error in input. Please try again.")
                        s = input("Input a number: ")
                    print(zeta(int(s)))
                    function = input("Enter Z for Zeta, C for Conway, Q to quit: ").lower()   
            elif function == 'c':
                print("Conway")
                n = input("Input a positive integer: ")
                while n.isnumeric() is False:
                    print("Error in input.  Please try again.")
                    n = input("Input a positive integer: ")
                #n_str = n 
                n = int(n)
                print("Base 13: ", int_to_base13(n))
                #n_str = str(n)
                print("Tridecimal: ",tridecimal_expansion(int_to_base13(n)))
                print("Conway float: ",tridecimal_to_conway(tridecimal_expansion(int_to_base13(n))))
                function = input("Enter Z for Zeta, C for Conway, Q to quit: ").lower()
            else:
              print("Error in input.  Please try again.")
              function = input("Enter Z for Zeta, C for Conway, Q to quit: ").lower() 
    print("\nThank you for playing.")
        
        
# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__": 
    main()
