###########################################################
#  Computer Project #9
#
#  Algorithm
#    prompt for a json file 
#    prompt for a category file 
#    while loop if option is not q 
#       if option is c 
#       if option is f 
#       if option is i 
#       if option is m
#       if option is w 
#    if option is q 
#    display closing message
###########################################################
import json,string

STOP_WORDS = ['a','an','the','in','on','of','is','was','am','I','me','you','and','or','not','this','that','to','with','his','hers','out','it','as','by','are','he','her','at','its']

MENU = '''
    Select from the menu:
        c: display categories
        f: find images by category
        i: find max instances of categories
        m: find max number of images of categories
        w: display the top ten words in captions
        q: quit
        
    Choice: '''

def get_option():
   ''' function asks user for input and returns their choice
       
       the function asks the user for an input and checks 
       whether their input matches one of the letters in 
       choice_list and if it isn't they are prompted to input 
       a different input and when they finally have an input 
       that is in the list 
       
       Paramters: none
       
       Returns: user_choice (the input from the user)'''
   user_choice = input(MENU).lower()
   choice_list = ['c', 'f', 'i', 'm', 'w', 'q']
   while user_choice not in choice_list:
       print("Incorrect choice.  Please try again.")
       user_choice = input(MENU).lower() 
   return user_choice
    
def open_file(s):
   ''' function opens file based on user input
       
       the function takes a user input and opens the 
       accoridng file if it exists an if it doesn't it 
       throws a FileNotFoundError prompting the user to 
       make another input 
       
       Parameters: s (constant input of either json or 
       category)
       
       Returns: fp (file pointer)'''
   while True: 
       try: 
           filename = input("Enter a {} file name: ".format(s))
           fp = open(filename)
           return fp 
       except FileNotFoundError: 
           print("File not found.  Try again.")
        
def read_annot_file(fp1):
   ''' function returns json file
       
       Paramters: fp1 (file pointer)
       
       Returns: json.load(fp1)'''
   return json.load(fp1)

def read_category_file(fp2):
   ''' function returns a dictionary of values from fp2
   
       the function creates an empty dictionary and then 
       goes through lines of fp2 and creates a list that is 
       the elements in the line and then initilizes key 
       and value with the first and and second indices of the list 
       and then appends them to the dictionary and returns the
       dictionary
       
       Parameters: fp2 (file pointer)
       
       Returns: D (dictionary)'''
   D = {}
   for line in fp2: 
       list_1 = line.split(" ")
       key = int(list_1[0]) 
       value = str(list_1[1]).strip()
       D.update({key: value})
   return D 

def collect_catogory_set(D_annot,D_cat):
   ''' function returns a set with all the categories from the dictionaries
       
       the function creates a set and then itereates 
       through D_annot and adds its values to set_1 and 
       then creates a second set, set_2 and then iterates 
       through the first set, which was created into a list, and 
       appends those values to set_2 and then returns set_2 
       
       Parameters: D_annot (dictionary), D_cat (dictionary)
       
       Returns: set_2 (set of categories)'''
   set_1 = set()
   for image in D_annot:
       for i in D_annot[image]['bbox_category_label']:
           set_1.add(i)
   set_2 = set()
   set_1_lst = list(set_1)
   for num in set_1_lst:
       set_2.add(D_cat[num]) 
   return set_2

def collect_img_list_for_categories(D_annot,D_cat,cat_set):
   ''' function returns a dictionary with list of all 
       image numbers for certain categories
       
       the function creates an empty dictionary and 
       then iterates through cat_set and D_annot and appends the 
       values from D_annot to the empty dictionary and then 
       sorts through it and returns it 
       
       Paramters: D_annot (dictionary), D_cat (dictionary), cat_set (set)
       
       Returns: D_1 (dictionary with key as categories and list 
       of images category appears in as values) '''
   D_1 = {} 
   for x in cat_set:
       D_1[x] = []
   for image in D_annot:
       for i in D_annot[image]['bbox_category_label']:
           var_1  = D_cat[int(i)]
           D_1[var_1].append(image)
   for x in D_1:
        D_1[x].sort()
   return D_1

def max_instances_for_item(D_image):
   ''' function returns max amount of times a category appears in an image
       
       the function initilizes max_instances and max_key 
       to empty values and itereates through D_images (dictionary) 
       and then if the length of the values is greater than 
       0 it becomes the new max instances and this goes on 
       until the end of the values
       
       Parameters: D_image (dictionary)
       
       Returns: max_instances (int), max_key (category)'''
   max_instances = 0
   max_key = ' '
   for image in D_image: 
       if len(D_image[image]) >  max_instances: 
           max_instances = len(D_image[image])
           max_key = image
   return max_instances, max_key

def max_images_for_item(D_image):
   ''' function returns max amount of times a category appears in an image
       
      the function initilizes max_instances and max_key 
       to empty values and itereates through D_images (dictionary) 
       and then if the length of the values is greater than 
       0 it becomes the new max instances and this goes on 
       until the end of the values
       
       Parameters: D_image (dictionary)
       
       Returns: max_instances (int), max_key (category)'''
   max_instances = 0
   max_key = ' '
   for image in D_image: 
       uniques = set(D_image[image])
       if len(uniques) >  max_instances: 
           max_instances = len(uniques)
           max_key = image
   return max_instances, max_key

def count_words(D_annot):
   ''' function returns a list of tuples with the amount of 
       times a category appears in an image as (3, 'dog') 
       
       the function creates an empty list and dictionary 
       and then iterates through D_annot and then through 
       values and then checks if the key is equal to 'cap_list'
       and then iterates through 'cap_list' values and checks if 
       the value is a stop words, an actual word, and if it is it is 
       appended to the list and the list is sorted and 
       reversed and returned
       
       Parameters: D_annot (dictionary)
       
       Returns: list_3 (list of tuples)'''
   list_3 = []
   D_3 = {}
   for key, value in D_annot.items():
       for i,j in value.items():
           if i == 'cap_list':
               for x in j: 
                  list_4 = x.split()
                  for z in list_4:
                      word = z.strip(string.punctuation).strip()
                      if word not in STOP_WORDS:
                          if word.isdigit() == False: 
                              if word not in D_3: 
                                  D_3[word] = 1
                              else: 
                                  D_3[word] += 1
   for key_1, value_1 in D_3.items():
       list_3.append((value_1, key_1))
       list_3.sort(reverse=True)
   return list_3
                      
def main():  
    print("Images\n")
    fp1 = open_file("JSON image")
    fp2 = open_file("category")
    D_annot = read_annot_file(fp1)
    D_cat = read_category_file(fp2)
    set_2 = collect_catogory_set(D_annot, D_cat)
    D_1 = collect_img_list_for_categories(D_annot,D_cat,set_2)
    D_image = collect_img_list_for_categories(D_annot,D_cat,set_2)
    max_instances = max_instances_for_item(D_image)
    max_key = max_instances_for_item(D_image)
    max_instances_2 = max_images_for_item(D_image)
    max_key_2 = max_images_for_item(D_image)
    list_3 = count_words(D_annot)
    choice = get_option()
    while choice != 'q':
        if choice == 'c': 
            print("\nCategories:")
            set_2_list = []
            for i in set_2:
                set_2_list.append(i)
            set_2_list.sort()
            for x in set_2_list[:-1]:
                print(x, end = ", ")
            print(set_2_list[-1])
            choice = get_option()
        if choice == 'f':
            print("\nCategories:")
            set_2_list = []
            for i in set_2:
                set_2_list.append(i)
            set_2_list.sort()
            for x in set_2_list[:-1]:
                print(x, end = ", ")
            print(set_2_list[-1])
            category_choice = input("Choose a category from the list above: ")
            while category_choice not in set_2:
                print("Incorrect category choice.")
                category_choice = input("Choose a category from the list above: ")
            print("\nThe category {} appears in the following images:".format(category_choice))
            new_list = D_1[category_choice]
            new_list.sort()
            new_list_2 = []
            for j in new_list: 
                if int(j) not in new_list_2:
                    new_list_2.append(int(j))
            new_list_2.sort()
            for z in new_list_2[:-1]:
                print(z, end = ", ")
            print(new_list_2[-1])
            choice = get_option()
        if choice == 'i': 
           print("\nMax instances: the category {} appears {} times in images.".format(max_key[1],max_instances[0]))
           choice = get_option()
        if choice == 'm': 
           print("\nMax images: the category {} appears in {} images.".format(max_key_2[1],max_instances_2[0]))
           choice = get_option()
        if choice == 'w':
            num_words = int(input("\nEnter number of desired words: "))
            while int(num_words) < 0:
                print("Error: input must be a positive integer: ")
                num_words = int(input("\nEnter number of desired words: "))
            print("\nTop {} words in captions.".format(num_words))
            print("{:<14s}{:>6s}".format("word","count"))
            for i in list_3[:num_words]:
                print("{:<14s}{:>6s}".format(str(i[1]), str(i[0])))
            choice = get_option()
    while choice not in ['c', 'f', 'i', 'm', 'w', 'q']:
        print("Incorrect choice.  Please try again.")
    print("\nThank you for running my code.") 

# Calls main() if this modules is called by name
if __name__ == "__main__":
    main()     