#####################################################################
#   Prompts user for file name until valid name given and returns fp
#   Then reads each line in fp and adds each unique word to a dictionary
#   and adds appends the line number to a set as the value in the dictionary
#   Prompts user again to enter words to find co-occurance for
#   Finds lines where the word or words are and prints them
#   Keeps prompting for words until user quits
#####################################################################

import string

def open_file():
    ''' Prompts user for filename until valid name given. Returns file pointer'''
    while True:    
        try:
            file_name = input("Enter a file name: ") 
            fp = open(file_name, 'r') #Retrieves file desired
            return fp
        except:
           print('Error -- ')
           
def read_data(fp):
    ''' This function will read the contents of that file line by line, process them and store them in a dictionary.'''
    Data_dict = {}
    counter = 1
    for line in fp:
        line = line.replace('"', '').replace('-','').replace("'", "").replace(",", ""). replace(".","")
        my_list = line.lower().strip().strip(string.punctuation).split()
        for i in my_list:
            if len(i) > 1 and i.isalpha() and i not in Data_dict:
                Data_dict[i] = {counter}
            elif i in Data_dict and counter not in Data_dict[i]:
                Data_dict[i].add(counter)
        counter += 1
    return Data_dict
      
def find_cooccurance(D, inp_str):
    '''Finds the line numbers the word(s) appear(s) in and creates a list of the line numbers. Then
    if inp_str has 2 or more words, it will compare the sets and return a new list with lines with both words'''
    inp_str = inp_str.replace(',', '').replace('"', '').replace('-','').replace("'", "")
    words = inp_str.lower().strip().strip(string.punctuation).split()
    if len(words) == 1:
        if words[0].strip() == '':
            return "None"
        elif words[0] in D:
            set1 = D[words[0]]
            new_num_list = list(set1)
            new_num_list.sort()
            return new_num_list
        else:
            return "None"
    elif len(words) == 2:
        set1 = D[words[0]]
        set2 = D[words[1]]
        set3 = (set1 & set2)
        new_num_list = list(set3)
        new_num_list.sort()
        return new_num_list
    elif len(words) == 3:
        set1 = D[words[0]]
        set2 = D[words[1]]
        set3 = D[words[2]]
        new_num_list = list(set1 & set2 & set3)
        new_num_list.sort()
        return new_num_list
        
def main():       
    fp = open_file()
    my_dict = read_data(fp)
    words = input("Enter space-separated words: ")
    while words.lower() != 'q':
        print("The co-occurance for: " + words.lower())
        lines = find_cooccurance(my_dict, words)
        line_number = []
        if type(lines) is str:
            print("Lines: None")
        elif lines == "":
            print("Lines: None")
        else:
            try:
                for i in lines:
                    line_number.append(str(i))
                    for i in line_number:
                        new_list = ', '.join(line_number)
                print("Lines: " + new_list)
            except TypeError:
                print("Lines: None")
        words = input("Enter space-separated words: ")
        if words.lower() == 'q':
            fp.close()
            break
        
if __name__ == "__main__":
    main()