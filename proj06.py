#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 18:38:23 2022

@author: ishitasaripalle
"""

import csv
from operator import itemgetter

# Keywords used to find christmas songs in get_christmas_songs()
CHRISTMAS_WORDS = ['christmas', 'navidad', 'jingle', 'sleigh', 'snow',\
                   'wonderful time', 'santa', 'reindeer']

# Titles of the columns of the csv file. used in print_data()
TITLES = ['Song', 'Artist', 'Rank', 'Last Week', 'Peak Rank', 'Weeks On']

# ranking parameters -- listed here for easy manipulation
A,B,C,D = 1.5, -5, 5, 3

#The options that should be displayed
OPTIONS = "\nOptions:\n\t\
        a - display Christmas songs\n\t\
        b - display songs by peak rank\n\t\
        c - display songs by weeks on the charts\n\t\
        d - display scores by calculated rank\n\t\
        q - terminate the program \n"

#the prompt to ask the user for an option
PROMPT = "Enter one of the listed options: "

def get_option():
    '''this function prompts the user for an input to display a list of songs. if the user 
    inputs anything other than a,b,c,d, or q, they will be prompted to input a differnet input because they 
    will receive an error message. the options are listed so the user knows to input a,b,c,d, or q. q will
    end the function. there are no parameters for this function, but the user input is a string and stays a string. 
    the output of this function can be reflected in the main because it is called.'''
    print("\nOptions:\n\t\
        a - display Christmas songs\n\t\
        b - display songs by peak rank\n\t\
        c - display songs by weeks on the charts\n\t\
        d - display scores by calculated rank\n\t\
        q - terminate the program \n")
    option = input(PROMPT).lower()
    while not(option == "a" or option == "b" or option == "c" or option == "d" or option == "q"):
            print("Invalid option!")
            print("Try again")
            option = input("Enter one of the listed options: ").lower()
    return option 
                      
def open_file():
    '''this function prompts the user to enter a file name. the files hold all the song information that the
    program aims to sort. the user must input a file name, and if the file does not exist they will be given an error 
    message due to the except, and the user must enter another input. There are no parameters, and the output
    is one of the given files being opened and read.'''
    while True: 
        try: 
            filename = input("Enter a file name: ")
            fp = open(filename, "r")
            return fp
        except FileNotFoundError: 
            print("Invalid file name; please try again.")
        
def read_file(fp):
    '''this function reads the file by using try and except to establish any spaces in the list with a -1 value. 
    the only parameter in this function is fp which is assigned to the file opened. '''
    reader = csv.reader(fp)
    master_list = []
    next(reader,None)
    for line in reader:
        song = line[0]
        artist = line[1]
        rank = line[2]
        last_week = line[3]
        peak = line[4]
        weeks = line[5]
        try: 
             rank = int(line[2])
        except ValueError: 
             rank = -1
        try: 
             last_week = int(line[3])
        except ValueError: 
             last_week = -1
        try: 
             peak = int(line[4])
        except ValueError: 
             peak = -1
        try: 
             weeks = int(line[5])
        except ValueError: 
             weeks = -1
        temp_list = [song, artist, rank, last_week, peak, weeks]
        master_list.append(temp_list)
    return master_list


def print_data(song_list):
    '''
    This function is provided to you. Do not change it
    It Prints a list of song lists.
    '''
    if not song_list:
        print("\nSong list is empty -- nothing to print.")
        return
    # String that the data will be formatted to. allocates space
    # and alignment of text
    format_string = "{:>3d}. "+"{:<45.40s} {:<20.18s} "+"{:>11d} "*4
    
    # Prints an empty line and the header formatted as the entries will be
    print()
    print(" "*5 + ("{:<45.40s} {:<20.18s} "+"{:>11.9s} "*4+'\n'+'-'*120).format(*TITLES))

    # Prints the formatted contents of every entry
    for i, sublist in enumerate(song_list, 1):
        #print(i,sublist)
        print(format_string.format(i, *sublist).replace('-1', '- '))

def get_christmas_songs(master_list):
    '''this function has one parameter, master_list, and the function appends the master_list to return 
    all the christmas songs within the list. the output is a list of all the christmas songs.'''
    christmas_songs = []
    for line in master_list:
        song = line[0].lower()
        for word in CHRISTMAS_WORDS:
            if word in song:
                christmas_songs.append(line)
                break
    christmas_songs.sort()
    return christmas_songs
            
def sort_by_peak(master_list):
    '''this function has one parameter, master_list, and the function creates a new list called my_list,
    to which it appends lines from the master_list, eventually returning a new list sorted by peak.'''
    my_list = []
    for line in master_list: 
        if line[4] != -1:
            my_list.append(line)
    my_list.sort(key = itemgetter(4))
    return my_list

def sort_by_weeks_on_list(master_list):
    '''this function has one parameter, master_list, and the function created a new list called my_list
    to which is appends lines from master_list, eventually returning a new sorted list but in descending order
    which is why reversed = True is used.'''
    my_list = []
    for line in master_list: 
        if line[5] != -1:
            my_list.append(line)
    my_list.sort(key = itemgetter(5), reverse = True)
    return my_list
        
def song_score(song):
    '''this function calculates the score of a song based on its change between weeks. this function has one 
    parameter, song. the function returns the calcualted score which is used in the function below. '''
    curr_rank = 100 - song[2]
    peak_rank = 100 - song[4]
    if song[2] == -1:
        curr_rank = -100
    if song[4] == -1: 
        peak_rank = -100
    weeks_on_chart = song[5]
    rank_delta = song[2] - song[3]
    score = A * peak_rank + B * rank_delta + C*weeks_on_chart+ D*curr_rank
    return score

def sort_by_score(master_list):
    '''this function has one parameter, master_list, and the function creates four new lists. the first list is appended 
    by the second list, and then the third list is appended by the fourth list. this function returns songs by score
    in descending order, from highest to lowest'''
    new_list = []
    for value in master_list:
        another_list = [value[0], value[1], value[2], value[3], value[4], value[5], song_score(value)]
        new_list.append(another_list)
    new_list.sort(key = itemgetter(6, 0), reverse = True)
    return_list = [] 
    for value in new_list:
        temp = [value[0],value[1],value[2],value[3],value[4],value[5]]
        return_list.append(temp)
    return return_list

def main():
    #the main function does not have a doc string
    print("Billboard Top 100")
    fp = open_file()
    master_list = read_file(fp)
    print_data(master_list)
    option = get_option()
    while option != 'q':
        if option == "a":
            list_christmas_songs = get_christmas_songs(master_list)
            print_data(list_christmas_songs)
            if len(list_christmas_songs) > 0: 
                percent = (len(list_christmas_songs)/len(master_list)) * 100 
                print("\n{:d}% of the top 100 songs are Christmas songs.".format(int(percent)))
            else: 
                print("None of the top 100 songs are Christmas songs.")
        elif option == "b":
            peak_list = sort_by_peak(master_list)
            print_data(peak_list)
        elif option == "c":
            week_list = sort_by_weeks_on_list(master_list)
            print_data(week_list)
        elif option == "d":
            score_list = sort_by_score(master_list)
            print_data(score_list)
        print("\nOptions:\n\t\
        a - display Christmas songs\n\t\
        b - display songs by peak rank\n\t\
        c - display songs by weeks on the charts\n\t\
        d - display scores by calculated rank\n\t\
        q - terminate the program \n")
        option = input("Enter one of the listed options: ")
    print("\nThanks for using this program!\nHave a good day!")

# Calls main() if this modules is called by name
if __name__ == "__main__":
    main()                     