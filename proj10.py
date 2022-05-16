###########################################################
#  Computer Project #10
#
#  Algorithm
#    prompt for an input
#    input from list of options 
#    loop while choice returns None for error checking 
#       if choice is MTT
#       if choice is MTF
#       if choice is MFT
#       if choice is R 
#       if choice is U
#       if choice is H 
#       if choice is Q 
#    display closing message
###########################################################
#DO NOT DELETE THESE LINES
import cards, random
random.seed(100) #random number generator will always generate 
                 #the same 'random' number (needed to replicate tests)

MENU = '''     
Input options:
    MTT s d: Move card from Tableau pile s to Tableau pile d.
    MTF s d: Move card from Tableau pile s to Foundation d.
    MFT s d: Move card from Foundation s to Tableau pile d.
    U: Undo the last valid move.
    R: Restart the game (after shuffling)
    H: Display this menu of choices
    Q: Quit the game       
'''
                
def initialize():
    ''' function initilizes foundation and tableau
        
        the function creates foundation, a list of 4 empty lists, 
        and tableau, a list of 8 empty lists and then 
        calls the Deck class to create a deck of cards and then uses 
        the shuffle method to shuffle the deck and then uses multiple 
        for loops to add to the empty lists and then returns 
        tableau and foundation as a tuple
        
        Parameters: none 
        
        Returns: tableau, foundation (a tuple)'''
    foundation = [[], [], [], []]
    my_deck = cards.Deck()
    my_deck.shuffle()
    tableau = [[], [], [], [], [], [], [], []]
    for i in range(8):
        if i%2 ==0:
            for x in range(7):
                tableau[i].append(my_deck.deal())
        else: 
            for z in range(6):
                tableau[i].append(my_deck.deal())
    return (tableau, foundation)

def display(tableau, foundation):
    '''Each row of the display will have
       tableau - foundation - tableau
       Initially, even indexed tableaus have 7 cards; odds 6.
       The challenge is the get the left vertical bars
       to line up no matter the lengths of the even indexed piles.'''
    
    # To get the left bars to line up we need to
    # find the length of the longest even-indexed tableau list,
    #     i.e. those in the first, leftmost column
    # The "4*" accounts for a card plus 1 space having a width of 4
    max_tab = 4*max([len(lst) for i,lst in enumerate(tableau) if i%2==0])
    # display header
    print("{1:>{0}s} | {2} | {3}".format(max_tab+2,"Tableau","Foundation","Tableau"))
    # display tableau | foundation | tableau
    for i in range(4):
        left_lst = tableau[2*i] # even index
        right_lst = tableau[2*i + 1] # odd index
        # first build a string so we can format the even-index pile
        s = ''
        s += "{}: ".format(2*i)  # index
        for c in left_lst:  # cards in even-indexed pile
            s += "{} ".format(c)
        # display the even-indexed cards; the "+3" is for the index, colon and space
        # the "{1:<{0}s}" format allows us to incorporate the max_tab as the width
        # so the first vertical-bar lines up
        print("{1:<{0}s}".format(max_tab+3,s),end='')
        # next print the foundation
        # get foundation value or space if empty
        found = str(foundation[i][-1]) if foundation[i] else ' '
        print("|{:^12s}|".format(found),end="")
        # print the odd-indexed pile
        print("{:d}: ".format(2*i+1),end="") 
        for c in right_lst:
            print("{} ".format(c),end="") 
        print()  # end of line
    print()
    print("-"*80)
          
def valid_tableau_to_tableau(tableau,s,d):
    ''' function checks if move from tableau to tableau is valid
    
        the function uses try and except to check the rank 
        of the last card in source and if its equal to the 
        last card in desintation the function will return true 
        and if not it will return false and then the len of the
        destination deck is checked to see if its zero and if it
        is true will be returned and if not false will be returned
        
        Parameters: tableau (list of lists), s (list), d (list)
        
        Returns: True or False'''
    try: 
        if (tableau[s][-1].rank() + 1) == tableau[d][-1].rank():
            return True
        else: 
            return False       
    except: 
        if len(tableau[int(d)]) == 0:
            return True
        else: 
            return False
    
def move_tableau_to_tableau(tableau,s,d):
    ''' function moves card from tableau to tableau
        
        the function calls its corresponding valid function 
        and if the valid function is true it will take the last 
        card from the source deck and move it to the destination
        deck and remove it from the source deck 
        
        Parameters: tableau (list of lists), s (list), d (list)
        
        Returns: True or False'''
    valid_tt = valid_tableau_to_tableau(tableau,s,d)
    if valid_tt == True: 
        s_card = tableau[s][-1]
        tableau[s].pop(-1)
        tableau[d].append(s_card)
        return True 
    else: 
        return False 

def valid_foundation_to_tableau(tableau,foundation,s,d):
    ''' function checks if move from foundation to tableau is valid
    
        the function uses try and except to check the rank 
        of the last card in source and if its equal to the 
        last card in desintation the function will return true 
        and if not it will return false and then the len of the
        destination deck is checked to see if its zero and if it
        is true will be returned and if not false will be returned
        
        Parameters: tableau (list of lists), foundation (list of lists), 
        s (list), d (list)
        
        Returns: True or False'''
    try: 
        if (foundation[s][-1].rank() + 1) == tableau[d][-1].rank():
            return True
        else: 
            return False       
    except: 
        if len(tableau[d]) == 0:
            return True
        else: 
            return False

def move_foundation_to_tableau(tableau,foundation,s,d):
    ''' function moves card from tableau to tableau
        
        the function calls its corresponding valid function 
        and if the valid function is true it will take the last 
        card from the source deck and move it to the destination
        deck and remove it from the source deck 
        
        Parameters: tableau (list of lists),  foundation(list of lists),
        s (list), d (list)
        
        Returns: True or False'''
    valid_ft = valid_foundation_to_tableau(tableau,foundation,s,d)
    if valid_ft == True: 
        s2_card = foundation[s][-1]
        foundation[s].pop(-1)
        tableau[d].append(s2_card)
        return True 
    else: 
        return False 

def valid_tableau_to_foundation(tableau,foundation,s,d):
    ''' function checks if move from foundation to tableau is valid
    
        the function checks if the rouces and destination decks are empty
        and then the function uses try and except to check the rank 
        of the last card in source and if its equal to the 
        last card in desintation the function will return true 
        and if not it will return false and then the len of the
        destination deck is checked to see if its zero and if it
        is true will be returned and if not false will be returned
        
        Parameters: tableau (list of lists), foundation(list of lists), 
        s (list), d (list)
        
        Returns: True or False'''
    if len(tableau[int(s)]) > 0: 
        if len(foundation[int(d)]) == 0: 
            if tableau[int(s)][-1].rank() == 1:
                return True
            else: 
                return False
        else:
            try: 
                if foundation[int(d)][-1].suit() != tableau[int(s)][-1].suit():
                    return False 
                else: 
                    if foundation[int(d)][-1].rank() == (tableau[int(s)][-1].rank() - 1):
                        return True
                    else: 
                        return False       
            except: 
                if len(foundation[int(d)]) == 0:
                    
                    return True
                else: 
                    return False
    else: 
        return False
    
def move_tableau_to_foundation(tableau, foundation, s,d):
    ''' function moves card from tableau to tableau
        
        the function calls its corresponding valid function 
        and if the valid function is true it will take the last 
        card from the source deck and move it to the destination
        deck and remove it from the source deck 
        
        Parameters: tableau (list of lists),  foundation(list of lists),
        s (list), d (list)
        
        Returns: True or False'''
    valid_tf = valid_tableau_to_foundation(tableau,foundation,s,d)
    if valid_tf == True: 
        s3_card = tableau[int(s)][-1]
        tableau[int(s)].pop(-1)
        foundation[int(d)].append(s3_card)
        return True 
    else: 
        return False

def check_for_win(foundation):
    ''' function checks for win 
        
        the function uses a for loop to iterate through a
        range of 4 and then uses an if statement to go through all the
        foundations and if they are not equal to 13 if will return 
        false and if they are it will return true
        
        Parameters: foundatio (list of lists)
        
        Returns: True or False'''
    for i in range(4):
        if len(foundation[i]) != 13:
            return False
    return True

def get_option():
    ''' function asks user for input
        
        the function take a user input and if its not an
        m based element it will return the input and if it is m based it
        will make sure the s and d inputs are within the appropriate 
        bounds and if they are not it will return an error message 
        and if they are it will return the output and it repeats this for 
        any m based input for the first element 
        
        Parameters: None 
        
        Returns: None'''
    user_input = input("\nInput an option (MTT,MTF,MFT,U,R,H,Q): ").upper()
    user_input = user_input.split()
    if user_input[0] in ['R', 'U', 'H', 'Q']: 
        return user_input
    else:
        if len(user_input) == 3:
            s_valid = int(user_input[1])
            user_input[1] = int(user_input[1])
            d_valid = int(user_input[2])
            user_input[2] = int(user_input[2])
            if user_input[0] == "MFT":
                if 0 <= s_valid and s_valid <= 3:
                    if 0 <= d_valid and d_valid <= 7:
                        return user_input
                    else: 
                        print("Error in Destination")
                        return None
                else: 
                    print("Error in Source.")
                    return None
            if user_input[0] == "MTT":
                if 0 <= s_valid and s_valid <= 7:
                    if 0 <= d_valid and d_valid <= 7: 
                        return user_input
                    else: 
                        print("Error in Destination")
                        return None
                else: 
                    print("Error in Source.")
                    return None
            if user_input[0] == "MTF":
                if 0 <= s_valid and s_valid <= 7:
                    if 0 <= d_valid and d_valid <= 3:
                        return user_input
                    else: 
                        print("Error in Destination")
                        return None
                else: 
                    print("Error in Source.")
                    return None
        else:
             print("Error in option:", user_input)
             return None
        
def main():  
    print("\nWelcome to Streets and Alleys Solitaire.\n")
    tableau, foundation = initialize()
    display(tableau, foundation)
    print(MENU)
    undo_move = []
    while True:
        choice = get_option()
        while choice == None:
            choice = get_option()
        if choice[0] == 'MTT':
            MTT = move_tableau_to_tableau(tableau,choice[1],choice[2])
            if MTT == True: 
                w = check_for_win(foundation)
                if w == True:
                    print("You won!\n")
                    display(tableau, foundation)
                    print("\n- - - - New Game. - - - -\n")
                    tableau, foundation = initialize()
                    display(tableau, foundation)
                    print(MENU)
                else:
                    display(tableau, foundation)
                    undo_move.append(choice)
            else: 
                print("Error in move: {} , {} , {}".format(choice[0],choice[1],choice[2]))
        if choice[0] == 'MTF':
            MTF = move_tableau_to_foundation(tableau,foundation,choice[1],choice[2])
            if MTF == True: 
                w = check_for_win(foundation)
                if w == True:
                    print("You won!\n")
                    display(tableau, foundation)
                    print("\n- - - - New Game. - - - -\n")
                    tableau, foundation = initialize()
                    display(tableau, foundation)
                    print(MENU)
                else: 
                    display(tableau, foundation)
                    undo_move.append(choice)        
            else: 
                print("Error in move: {} , {} , {}".format(choice[0],choice[1],choice[2]))
        if choice[0] == 'MFT':
            MFT = move_foundation_to_tableau(tableau,foundation,choice[1],choice[2])
            if MFT == True: 
                w = check_for_win(foundation)
                if w == True:
                    print("You won!\n")
                    display(tableau, foundation)
                    print("\n- - - - New Game. - - - -\n")
                    tableau, foundation = initialize()
                    display(tableau, foundation)
                    print(MENU)
                else: 
                    display(tableau, foundation)
                    undo_move.append(choice)    
            else: 
                print("Error in move: {} , {} , {}".format(choice[0],choice[1],choice[2]))
        if choice[0] == 'U':
            if len(undo_move) == 0:
                print("No moves to undo.")
            else:
                print("Undo: ",undo_move[-1][0],undo_move[-1][1],undo_move[-1][2])
                if undo_move[-1][0] == 'MTT':
                    tableau[undo_move[-1][1]].append(tableau[undo_move[-1][2]][-1])
                    tableau[undo_move[-1][2]].pop()
                if undo_move[-1][0] == 'MTF':
                    tableau[undo_move[-1][1]].append(foundation[undo_move[-1][2]][-1])
                    foundation[undo_move[-1][2]].pop()
                if undo_move[-1][0] == 'MFT':
                    foundation[undo_move[-1][1]].append(tableau[undo_move[-1][2]][-1])
                    tableau[undo_move[-1][2]].pop()
                undo_move.pop()
                display(tableau, foundation)
        if choice[0] == 'R':
            print("\n- - - - New Game. - - - -\n")
            tableau, foundation = initialize()
            display(tableau, foundation)
            print(MENU)
        if choice[0] == 'H':
            print(MENU)
        if choice[0] == 'Q':
            print("Thank you for playing.")
            break

if __name__ == '__main__':
     main()