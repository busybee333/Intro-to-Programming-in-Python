#######################################################################
#
#   Takes a number of users from a file
#   Creates list of lists of who's friends with who
#   Finds number of mutual friends each user has
#   Creates similarity matrix
#   Uses similarity matrix to find friend suggestion,
#       excluding self and current friends
#   Keeps suggesting friends for input user until "no" is input
#
########################################################################

def open_file():
    ''' Prompts user for filename until valid name given. Returns file pointer'''
    while True:    
        try:
            file_name = input("Enter a filename: ") 
            fp = open(file_name, 'r') #Retrieves file desired
            return fp
        except:
           print("Error in filename.", end="")


def read_file(fp):  
    ''' Reads file and returns the network with the position of the list in the network is the friend and the list contains the friend'''
    n = fp.readline()
    n = int(n)
    network = []
    for i in range(n):
        network.append([])  
    for line in fp: #Creates network
        split = line.split()
        split = [int(i) for i in split]
        network[split[0]].append(split[1])
        reverse = split[::-1]
        if reverse[1] not in network[reverse[0]]:
            network[reverse[0]].append(reverse[1])
    return network

def num_in_common_between_lists(list1, list2):
    ''' Finds the number of friends n has in common'''
    count = 0
    for i in list1:
        if i in list2:
            count += 1 #Counts how many mutual friends 2 users have
    return count

def init_matrix(n):
    '''Create an nxn matrix, initialize with zeros, and return the matrix.'''
    matrix = []
    for row in range(n):  # for each of the n rows
        matrix.append([])  # create the row and initialize as empty
        for column in range(n):
            matrix[row].append(0)  # append a 0 for each of the n columns
    return matrix
    
def calc_similarity_scores(network):  
    ''' Creates a similarity matrix of the number of friends that any pair of users have in common'''
    n = len(network)
    similarity_matrix = init_matrix(n)
    for i in range(n):
        for j in range(n):
            num_in_common = num_in_common_between_lists(network[i],network[j])
            similarity_matrix[i][j] = num_in_common
            similarity_matrix[j][i] = num_in_common
    return similarity_matrix
            
def recommend(user_id,network,similarity_matrix):
    ''' Finds which friend to recommend by eliminating self and current friends from list'''
    user_list = similarity_matrix[user_id]
    top = max(user_list)
    index = user_list.index(top)
    user_list[index] = 0 #Takes user out of suggestion choices
    top = max(user_list)
    index = user_list.index(top)
    while True:
        if index not in network[user_id]: #If the suggested friend isn't in network, index is suggested
            return index
            break
        else: #If suggested friend is in network, new index is found
            user_list[index] = 0
            top = max(user_list)
            maxlist = [i for i, j in enumerate(user_list) if j == top]
            index = min(maxlist)
    
def main():
    print("Facebook friend recommendation.")
    file_pointer = open_file()
    network = read_file(file_pointer)
    matrix = calc_similarity_scores(network)
    n = len(network)
    o = []
    for i in range(n): #Creates list of values that user_id can be
        o.append(i)
    while True:
        try:
            user = input("Enter an integer in the range 0 to " + str(n-1) + ": ")
            user_id = int(user)
            if user_id in o:
                recommendation = recommend(user_id, network, matrix)
                print("The suggested friend for " + user + " is " + str(recommendation))
                r = input("Do you want to continue (yes/no)? ")
                response = r.lower() 
                if response == "no":
                    break
                else:
                    pass
            else:
                print("Input must be an int between 0 and " + str(n-1), end="")
        except:
            print("Input must be an int between 0 and " + str(n-1), end="")
    
if __name__ == "__main__":
    main()
