####################################################################
#   Baker's Game:
#   For each move, the valid_... function will check if the move is valid
#   If the move is valid, then move will be made       
#   Play until the game has been won
####################################################################

import cards #This is necessary for the project


BANNER = """
    __        _____ _   _ _   _ _____ ____  _ _ _ 
    \ \      / /_ _| \ | | \ | | ____|  _ \| | | |
     \ \ /\ / / | ||  \| |  \| |  _| | |_) | | | |
      \ V  V /  | || |\  | |\  | |___|  _ <|_|_|_|
       \_/\_/  |___|_| \_|_| \_|_____|_| \_(_|_|_)

"""


RULES = """
     ____        _             _        ____
    | __ )  __ _| | _____ _ __( )___   / ___| __ _ _ __ ___   ___
    |  _ \ / _` | |/ / _ \ '__|// __| | |  _ / _` | '_ ` _ \ / _ \\
    | |_) | (_| |   <  __/ |    \__ \ | |_| | (_| | | | | | |  __/
    |____/ \__,_|_|\_\___|_|    |___/  \____|\__,_|_| |_| |_|\___|

    Cells:       Cells are numbered 1 through 4. They can hold a
                 single card each.

    Foundations: Foundations are numbered 1 through 4. They are
                 built up by rank from Ace to King for each suit.
                 All cards must be in the foundations to win.

    Tableaus:    Tableaus are numbered 1 through 8. They are dealt
                 to at the start of the game from left to right
                 until all cards are dealt. Cards can be moved one
                 at a time from tableaus to cells, foundations, or
                 other tableaus. Tableaus are built down by rank
                 and cards must be of the same suit.

"""


MENU = """

    Game commands:
    
    TC x y    Move card from tableau x to cell y
    TF x y    Move card from tableau x to foundation y
    TT x y    Move card from tableau x to tableau y
    CF x y    Move card from cell x to foundation y
    CT x y    Move card from cell x to tableau y
    R         Restart the game with a re-shuffle
    H         Display this menu of commands
    Q         Quit the game
    
"""
   
     
def valid_fnd_move(src_card, dest_card = None):
    """
    This function is used to decide whether a movement from a 
    tableau or a cell to a foundation is valid or not
    """
    # Tells if card is an Ace and if the foundation is empty
    if dest_card == None and src_card.rank() == 1:
        return True
    #Returns error if the foundation is empty and the src_card isn't an ace
    elif dest_card == None and src_card.rank() != 1:
        raise RuntimeError("Invalid move: Source card is not an Ace")
    elif dest_card != None: 
        if (dest_card.suit() == src_card.suit()): #Tells whether or not the suits are the same
            if ((src_card.rank() - 1) == dest_card.rank()): #Determines whether the ranks are valid
                return True
            else:
                raise RuntimeError("Wrong rank")
        else:
            raise RuntimeError("Wrong suit")
    else:
        raise RuntimeError("Error")
      
def valid_tab_move(src_card = None, dest_card = None):
    """
    This function is used to decide whether a movement from a cell, 
    foundation, or another tableau to a tableau is valid or not
    """    
    #Tells if tableau is empty
    if dest_card == None:
        return True
    elif dest_card != None:
        if dest_card.suit() == src_card.suit(): #Tells whether or not the suits are the same
            if ((src_card.rank() + 1) == dest_card.rank()): #Determines whether the ranks are valid
                return True
            else:
                raise RuntimeError("Wrong rank")
        else:
            raise RuntimeError("Wrong suit")
    else:
        raise RuntimeError("Error")
    
def tableau_to_cell(tab = None, cell = None):
    """
    This function will implement a movement of a card from a tableau to a cell
    """ 
    if not tab:
        raise RuntimeError("Cannot move empty card because nothing is there. Choose a different tableau")
    else:
        src_card = tab[-1]  #Takes last element of list as src_card
    if not cell: #If the cell list is empty, the value of the dest_Card = None
        dest_card = None
    else:
        dest_card = cell
    #If the cell is empty and the move is valid, the function will implement of a card from a tableau to a cell
    if not cell and valid_tab_move(src_card, dest_card) == True: 
        src_card = tab.pop()
        cell.append(src_card)
    else:
        raise RuntimeError("Cell already has a card")
            
def tableau_to_foundation(tab = None, fnd = None):
    """
    This function will implement a movement of a card from a 
    tableau to a foundation
    """    
    if not tab:
        raise RuntimeError("Cannot move empty card because nothing is there. Choose a different tableau")
    else:
        src_card = tab[-1]  #Takes last element of list as src_card
    if not fnd: #If the foundation list is empty, the value of the dest_Card = None
        dest_card = None
    else:
        dest_card = fnd[-1]
    if valid_fnd_move(src_card, dest_card) == True: #If the move is valid, the card will move
        src_card = tab.pop()
        fnd.append(src_card)
        return fnd

def tableau_to_tableau(tab1, tab2):
    """
    This function will implement a movement of a card from one tableau
    column to another tableau column
    """    
    if not tab1:
        raise RuntimeError("Cannot move empty card because nothing is there. Choose a different tableau")
    else:
        src_card = tab1[-1]  #Takes last element of list as src_card
    if not tab2: #If the tableau list is empty, the value of the dest_Card = None
        dest_card = None
    else:
        dest_card = tab2[-1]
    if valid_tab_move(src_card, dest_card) == True: #If the move is valid, the card will move
        src_card = tab1.pop()
        tab2.append(src_card)
        return tab2

def cell_to_foundation(cell, fnd):
    """
    This function will implement a movement of a card from a cell to a foundation
    """
    if not cell:
        raise RuntimeError("Cannot move empty cell")
    else:
        src_card = cell[0] #Takes the only element of list as src_card
    if not fnd: #If the foundation list is empty, the value of the dest_Card = None
        dest_card = None
    else:
        dest_card = fnd[-1]
    if valid_fnd_move(src_card, dest_card) == True: #If the move is valid, the card will move
        src_card = cell.pop()
        fnd.append(src_card)
        return fnd

def cell_to_tableau(cell, tab):
    """
    This function will implement a movement of a card from a cell to a tableau column
    """    
    if not cell:
        raise RuntimeError("Cannot move empty cell")
    else:
        src_card = cell[0] #Takes the only element of list as src_card
    if not tab: #If the tableau list is empty, the value of the dest_Card = None
        dest_card = None
    else:
        dest_card = tab[-1]
    if valid_tab_move(src_card, dest_card) == True: #If the move is valid, the card will move
        src_card = cell.pop()
        tab.append(src_card)
        return tab
              
def is_winner(foundations):
    """
    This function will be used to decide if the user won the game
    """   
    string = ""
    for i in range(4):
        if len(foundations[i]) == 13 and foundations[i][-1].rank() == 13: #Checks if all foundations have 13 cards and the last card is a king
            string += "a"
        else:
            pass
    if len(string) == 4:
        return True
    else:
        return False


def setup_game():
    """
    The game setup function. It has 4 cells, 4 foundations, and 8 tableaus. All
    of these are currently empty. This function populates the tableaus from a
    standard card deck. 

    Tableaus: All cards are dealt out from left to right (meaning from tableau
    1 to 8). Thus we will end up with 7 cards in tableaus 1 through 4, and 6
    cards in tableaus 5 through 8 (52/8 = 6 with remainder 4).

    This function will return a tuple: (cells, foundations, tableaus)
    """
    
    #You must use this deck for the entire game.
    #We are using our cards.py file, so use the Deck class from it.
    stock = cards.Deck()
    #The game piles are here, you must use these.
    cells = [[], [], [], []]                    #list of 4 lists
    foundations = [[], [], [], []]              #list of 4 lists
    tableaus = [[], [], [], [], [], [], [], []] #list of 8 lists
    
    """ YOUR SETUP CODE GOES HERE """
    stock.shuffle()
    count = 0
    for i in range(52):
        dealt = stock.deal()
        if count > 7:
            count = 0
            tableaus[count].append(dealt)
            count += 1
        else:
            tableaus[count].append(dealt)
            count += 1

    return cells, foundations, tableaus


def display_game(cells, foundations, tableaus):
    """
    Displays all the cells, foundations, and tableaus
    """
    #Labels for cells and foundations
    print("    =======Cells========  ====Foundations=====")
    print("     --1----2----3----4--  --1----2----3----4--")
    
    #Printing Cells
    print("     ", end = "")
    for i in range(4):
        try:
            print("[{:3s}]".format(str(cells[i][-1])), end = "" )
        except:
            print("[{:3s}]".format(" "), end = "" )
        
    #Printing Foundations
    print("  ", end = "")
    for i in range(4):
        try:
            print("[{:3s}]".format(str(foundations[i][-1])), end = "" )
        except:
            print("[{:3s}]".format(" "), end = "" )

    # to print a card using formatting, convert it to string:
    # print("{}".format(str(card)))

    print()
    #Labels for tableaus
    print("    =================Tableaus=================")
    print("    ---1----2----3----4----5----6----7----8---")
    
    #Printing tableaus
    for i in range(3): #Removes any 'None's from the list
        for lst in tableaus:
            for i in lst:
                if i == None:
                    lst.remove(i)
    max = 0 
    for i in tableaus: #Finds max length of all tableaus
        if len(i) > max:
            max = len(i)
            
    for y in range(max):
        try:
            print("       ", end = "")
        except:
            pass
        for x in range(8):
            try:
                print("{:4s}".format(str(tableaus[x][y])), end = " " )
            except:
                print("{:4s}".format(" "), end = " ")
        print("")
    return cells, foundations, tableaus

#HERE IS THE MAIN BODY OF OUR CODE
print(RULES)
cells, fnds, tabs = setup_game()
cells, foundations, tableaus = display_game(cells, fnds, tabs)
print(MENU)
command = input("prompt :> ").strip().lower()
while command != 'q':
    try:
        if command == 'r':
            print(RULES)
            cells, fnds, tabs = setup_game()
            print(MENU)
        elif command == 'h':
            print(MENU)
        else:
            if "tc" in command:
                my_lst = command.split(" ")
                if len(my_lst) < 3:
                    raise RuntimeError("Missing value(s)")
                    break
                if len(my_lst) > 3:
                    raise RuntimeError("Too many values")
                    break
                my_lst.pop(0)
                try:
                    try:
                        my_lst[0] = int(my_lst[0])
                    except:
                        raise RuntimeError("Invalid x or y")
                    tab = tableaus[my_lst[0] - 1]
                except IndexError:
                    try:
                        try:
                            my_lst[0] = int(my_lst[0])
                        except:
                            raise RuntimeError("Invalid x or y")
                        tab = tableaus[my_lst[0] - 1]
                    except IndexError:
                        raise RuntimeError("Invalid x and y")
                        break
                try:
                    my_lst[0] = int(my_lst[0])
                    tab = tableaus[my_lst[0] - 1]
                except IndexError:
                    raise RuntimeError("Invalid range. Choose a tableau from 1-8")
                    break
                try:
                    my_lst[1] = int(my_lst[1])
                    cell = cells[my_lst[1] - 1]
                except IndexError:
                    raise RuntimeError("Invalid range. Choose a cell from 1-4")
                    break
                tableau_to_cell(tab, cell)
            elif "tf" in command:
                my_lst = command.split(" ")
                if len(my_lst) < 3:
                    raise RuntimeError("Missing value(s)")
                    break
                if len(my_lst) > 3:
                    raise RuntimeError("Too many values")
                    break
                my_lst.pop(0)
                try:
                    try:
                        my_lst[0] = int(my_lst[0])
                    except:
                        raise RuntimeError("Invalid x or y")
                    tab = tableaus[my_lst[0] - 1]
                except IndexError:
                    try:
                        try:
                            my_lst[1] = int(my_lst[1])
                        except:
                            raise RuntimeError("Invalid x or y")
                        fnd = foundations[my_lst[1] - 1]
                    except IndexError:
                        raise RuntimeError("Invalid x and y")
                        break
                try:
                    my_lst[0] = int(my_lst[0])
                    tab = tableaus[my_lst[0] - 1]
                except IndexError:
                    raise RuntimeError("Invalid range. Choose a tableau from 1-8")
                    break
                try:
                    my_lst[1] = int(my_lst[1])
                    fnd = foundations[my_lst[1] - 1]
                except IndexError:
                    raise RuntimeError("Invalid range. Choose a foundation from 1-4")
                    break
                tableau_to_foundation(tab, fnd)
            elif "tt" in command:
                my_lst = command.split(" ")
                if len(my_lst) < 3:
                    raise RuntimeError("Missing value(s)")
                    break
                if len(my_lst) > 3:
                    raise RuntimeError("Too many values")
                    break
                my_lst.pop(0)
                try:
                    try:
                        my_lst[0] = int(my_lst[0])
                    except:
                        raise RuntimeError("Invalid x or y")
                    tab1 = tableaus[my_lst[0] - 1]
                except IndexError:
                    try:
                        try:
                            my_lst[1] = int(my_lst[1])
                        except:
                            raise RuntimeError("Invalid x or y")
                        tab2 = tableaus[my_lst[1] - 1]
                    except IndexError:
                        raise RuntimeError("Invalid x and y")
                        break
                try:
                    my_lst[0] = int(my_lst[0])
                    tab1 = tableaus[my_lst[0] - 1]
                except IndexError:
                    raise RuntimeError("Invalid range. Choose a tableau from 1-8")
                    break
                try:
                    my_lst[1] = int(my_lst[1])
                    tab2 = tableaus[my_lst[1] - 1]
                except IndexError:
                    raise RuntimeError("Invalid range. Choose a tableau from 1-8")
                    break
                tableau_to_tableau(tab1, tab2)
            elif "cf" in command:
                my_lst = command.split(" ")
                if len(my_lst) < 3:
                    raise RuntimeError("Missing value(s)")
                    break
                if len(my_lst) > 3:
                    raise RuntimeError("Too many values")
                    break
                my_lst.pop(0)
                try:
                    try:
                        my_lst[0] = int(my_lst[0])
                    except:
                        raise RuntimeError("Invalid x or y")
                    cell = cells[my_lst[0] - 1]
                except IndexError:
                    try:
                        try:
                            my_lst[1] = int(my_lst[1])
                        except:
                            raise RuntimeError("Invalid x or y")
                        fnd = foundations[my_lst[1] - 1]
                    except IndexError:
                        raise RuntimeError("Invalid x and y")
                        break
                try:
                    my_lst[0] = int(my_lst[0])
                    cell = cells[my_lst[0] - 1]
                except IndexError:
                    raise RuntimeError("Invalid range. Choose a cell from 1-4")
                    break
                try:
                    my_lst[1] = int(my_lst[1])
                    fnd = foundations[my_lst[1] - 1]
                except IndexError:
                    raise RuntimeError("Invalid range. Choose a foundation from 1-4")
                    break
                cell_to_foundation(cell, fnd)
            elif "ct" in command:
                my_lst = command.split(" ")
                if len(my_lst) < 3:
                    raise RuntimeError("Missing value(s)")
                    break
                if len(my_lst) > 3:
                    raise RuntimeError("Too many values")
                    break
                my_lst.pop(0)
                try:
                    try:
                        my_lst[0] = int(my_lst[0])
                    except:
                        raise RuntimeError("Invalid x or y")
                        break
                    cell = cells[my_lst[0] - 1]
                except IndexError:
                    try:
                        try:
                            my_lst[1] = int(my_lst[1])
                        except:
                            raise RuntimeError("Invalid x or y")
                        tab = tableaus[my_lst[1] - 1]
                    except IndexError:
                        raise RuntimeError("Invalid x and y")
                        break
                try:
                    my_lst[0] = int(my_lst[0])
                    cell = cells[my_lst[0] - 1]
                except IndexError:
                    raise RuntimeError("Invalid range. Choose a cell from 1-4")
                    break
                try:
                    my_lst[1] = int(my_lst[1])
                    tab = tableaus[my_lst[1] - 1]
                except IndexError:
                    raise RuntimeError("Invalid range. Choose a tableau from 1-8")
                    break
                cell_to_tableau(cell, tab)
            elif not command:
                raise RuntimeError("Error: Empty input")
            else:
                raise RuntimeError("Error: invalid command. Try valid command")
        
    #Any RuntimeError you raise lands here
    except RuntimeError as error_message:
        print("{:s}\nTry again.".format(str(error_message)))
    if is_winner(foundations) == True:
        print("You Win")
        break
    else:
        pass
    
    display_game(cells, fnds, tabs)                
    command = input("prompt :> ").strip().lower()


