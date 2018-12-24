###################################################################################
#
#   Takes input(# of CSE help rooms & # of paths between help rooms)
#   Reads file for # of rooms and creates a matrix of adjacency
#   Finds all different combinations you can place x amount of TAs in x amount of rooms
#   Then test all the different combinations starting with 1 TA to see
#       if you can reach all rooms
#   When min amount of TAs are found and all rooms are reached, program stops checking combinations
#   Then prints amount of TAs needed and which rooms they are assigned to
#   The adjacency matrix is also printed
#
###################################################################################

import itertools

class Matrix(object):
    '''Add your docstring here.'''
    
    def __init__(self):  # no modification is needed for this method, but you may modify it if you wish to
        '''Create and initialize your class attributes.'''
        self._matrix = []
        self._rooms = 0
        
    def read_file(self,fp):  #fp is a file pointer
        '''Build an adjacency matrix that you read from a file fp.'''
        self._rooms = fp.readline()
        self._rooms = int(self._rooms)
        #Most of following code from proj07.py
        network = []
        for i in range(self._rooms): #Creates the # (of rooms) of empty lists
            network.append([])  
        for line in fp: #Creates network
            split = line.split()
            split = [int(i) for i in split]
            reverse = split[::-1]
            network[reverse[0] - 1].append(reverse[1])
            network[split[0] - 1].append(split[1])
        for i in network:
            i = set(i)
            self._matrix.append(i)
        return self._matrix
    
    def __str__(self):
        '''Return the matrix as a string.'''
        s = ''
        return_list = []
        for i in range(self._rooms): #Creates list of strings
            room = i + 1
            first = str(room) + " : "
            second = ' '.join(str(x) for x in list(self._matrix[i]))
            third = first + second
            return_list.append(third)
        s = "\n".join(return_list)
        return s  #__str__ always returns a string

    def __repr__(self):  # no modification need of this method
        '''Call __str__() to return a string for displaying in the shell'''
        return self.__str__()  
        
    def adjacent(self,index):
        '''Return the set of connecting rooms to room specified by index'''
        return self._matrix[index - 1]

    def rooms(self):
        '''Return the number of rooms'''
        return self._rooms


def open_file():
    ''' Prompts user for filename until valid name given. Returns file pointer'''
    while True:    
        try:
            file_name = input("Enter a filename: ") 
            fp = open(file_name, 'r') #Retrieves file desired
            return fp
        except:
           print("Error in filename.", end="")
def main():
    fp = open_file()
    matrix=Matrix()
    m = Matrix.read_file(matrix, fp)
    rooms = Matrix.rooms(matrix)
    list_of_rooms = []
    for i in range(rooms):
        list_of_rooms.append(i+1) # + 1 because i starts at 0
    num_TA = 0
    combo_sets = []
    done = False
    for i in range(3):
        num_TA += 1
        combos = list(itertools.combinations(list_of_rooms, num_TA)) #Creates all possible combinations
        for tup in combos:
            combo_sets.append(set(tup))
    for each_set in combo_sets:
        f = 0
        for num in each_set: #Finds the union of all sets in a combination
            if f == 0:
                my_set = matrix.adjacent(num)
            else:
                my_set = my_set | matrix.adjacent(num)
            my_set.add(num)
            f += 1
        if my_set == set(list_of_rooms):
            done = True
            if done == True:
                break
        if done == True:
            break
    TAs_needed = len(each_set)
    print("TAs needed: " + str(TAs_needed))
    TAs = list(each_set)
    TAs_assigned = str(TAs).strip('[]')
    print("TAs assigned to rooms: " + TAs_assigned + "\n")
    print("Adjacency Matrix")
    t = 1
    for i in m:
        i.discard(t)
        t+=1
    print(matrix)
    
if __name__ == "__main__":
    main()