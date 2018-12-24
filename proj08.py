###############################################################
#   Opens a file the user inputs
#   Prompts user to choose region
#   Reads data in gather_data and creates dictionary with info
#   Displays the min and max GDP per capita and per capita income
#   Also displays the states in alphabetical order and info in colums
#   Then asks if user wants to plot data
#   If yes, then prompts user to choose what they want to plot
#   Plots data
###############################################################
   

import pylab

# Here are some constants that are optional to use -- feel free to modify them, if you wish
REGION_LIST = ['Far_West',
 'Great_Lakes',
 'Mideast',
 'New_England',
 'Plains',
 'Rocky_Mountain',
 'Southeast',
 'Southwest',
 'all']
lower_reg = []
for i in REGION_LIST:
    lower_reg.append(i.lower())
VALUES_LIST = ['Pop', 'GDP', 'PI', 'Sub', 'CE', 'TPI', 'GDPp', 'PIp']
VALUES_NAMES = ['Population(m)','GDP(b)','Income(b)','Subsidies(m)','Compensation(b)','Taxes(b)','GDP per capita','Income per capita']
PROMPT1 = "Specify a region from this list -- far_west,great_lakes,mideast,new_england,plains,rocky_mountain,southeast,southwest,all: "
PROMPT2 = "Specify x and y values, space separated from Pop, GDP, PI, Sub, CE, TPI, GDPp, PIp: "

def open_file():
    ''' Prompts user for filename until valid name given. Returns file pointer'''
    while True:    
        try:
            file_name = input("Input a file: ") 
            fp = open(file_name, 'r') #Retrieves file desired
            return fp
        except:
           print("Error opening file. Please try again.")

def gather_data(fp):
    '''Prompts user to choose region. Reads data from a file and returns selected region's
    data in a dictionary. Appends GDP per capita & per capita personal income'''
    all_dict = {}
    region_dict = {}
    global region
    region = input(PROMPT1) #Prompts user for region
    if region.lower() not in lower_reg:
                print("Error in region name. Please try again")
    while region.lower() not in lower_reg: #Keeps prompting user for region until correct region input
        try:
            region = input(PROMPT1)
            if region.lower() not in lower_reg:
                print("Error in region name. Please try again")
        except:
            pass
            
    fp.readline() #skips first line
    for line in fp: #Creates a dictionary with all states and with the specific region
        my_list = line.strip().split(',')
        state = my_list.pop(0) 
        gdp = float(my_list[2]) * (10**9) 
        income = float(my_list[3]) * (10**9)
        pop = float(my_list[1]) * (10**6)
        gdp_per_cap = gdp/pop
        my_list.append(gdp_per_cap) #Adds GDP per capita to list of keys
        income_per_cap = income/pop 
        my_list.append(income_per_cap) #Appends income per capita to list of keys
        all_dict[state] = my_list
        if region.lower() == all_dict[state][0].lower():
            region_dict[state] = my_list
    if region.lower() == "all":
        return all_dict
    else:
        return region_dict
    
def print_data(dictionary):
    '''Prints states with the highest and lowest GDP per capita and Per capita income with the values and then prints out
    all of the states in the region in alphabetical order with their data'''
    max_gdp = 0
    max_gdp_state = ""
    min_gdp = 99999999999999999999999999999999999999999
    min_gdp_state = ""
    max_income = 0
    max_income_state = ""
    min_income = 9999999999999999999999999999999999999999999
    min_income_state = ""
    for k,v in dictionary.items(): #finds the mins and maxes of gdp per capita and income per capita
        if dictionary[k][-2] > max_gdp:
            max_gdp = dictionary[k][-2]
            max_gdp_state = k
        elif dictionary[k][-2] < min_gdp:
            min_gdp = dictionary[k][-2]
            min_gdp_state = k
        else:
            pass
        if dictionary[k][-1] > max_income:
            max_income = dictionary[k][-1]
            max_income_state = k
        elif dictionary[k][-1] < min_income:
            min_income = dictionary[k][-1]
            min_income_state = k
        else:
            pass
    #prints all the formatted data
    print("{:20s} {:d} {:,.2f}".format("hello", 9, 99999.02))
    print()
    print("Data for the ", region.title(), "region:")
    print()
    print("{:s} {:s} ${:,.2f}".format(max_gdp_state, "has the highest GDP per capita at", dictionary[max_gdp_state][-2]))
    print("{:s} {:s} ${:,.2f}".format(min_gdp_state, "has the lowest GDP per capita at", dictionary[min_gdp_state][-2]))
    print()
    print("{:s} {:s} ${:,.2f}".format(max_income_state, "has the highest income per capita at", dictionary[max_income_state][-1]))
    print("{:s} {:s} ${:,.2f}".format(min_income_state, "has the lowest income per capita at", dictionary[min_income_state][-1]))
    print()
    print("Data for all states in the ", region.title(), "region:")
    print()
    #Spacing is to figure out how long each space of string should be
    spacing = []
    for i in VALUES_NAMES:
        length = len(i) + 3
        spacing.append(length)
    
    print("{:<15s} {:16s} {:9s} {:12s} {:15s} {:18s} {:11s} {:17s} {:20s}".format("State", VALUES_NAMES[0], VALUES_NAMES[1], VALUES_NAMES[2], 
          VALUES_NAMES[3], VALUES_NAMES[4], VALUES_NAMES[5], VALUES_NAMES[6], VALUES_NAMES[7]))
    for k,v in dictionary.items():
        dictionary[k].pop(0)
        for i in v:
            position = v.index(i)
            i = float(i)
            dictionary[k][position] = i
    for k,v in dictionary.items():
        print("{:<15s} {:13,.2f} {:9,.2f} {:12,.2f} {:15,.2f} {:18,.2f} {:11,.2f} {:17,.2f} {:20,.2f}".format(k, v[0], v[1], v[2], v[3], v[4],
                    v[5], v[6], v[7]))

def plot_regression(x,y):
    '''Draws a regression line for values in lists x and y.
       x and y must be the same length.'''
    xarr = pylab.array(x) #numpy array
    yarr = pylab.array(y) #numpy arry
    m,b = pylab.polyfit(xarr,yarr, deg = 1) #creates line, only takes numpy arrays
    #as parameters
    pylab.plot(xarr,m*xarr + b, '-') #plotting the regression line
    


def plot(dictionary):   # you need to replace pass with parameters
    '''Plots the values entered by the user.'''
    
    lower_values_list = []
    for i in VALUES_LIST:
        lower_values_list.append(i.lower())
        
    # prompt for which values to plot; these will be the x and y
    x_and_y = input(PROMPT2)
    my_list = x_and_y.split(" ")
    x_name = my_list[0]
    y_name = my_list[1]
    if x_name not in VALUES_LIST or y_name not in VALUES_LIST: #if x or y not in list, prompts again
        print("Error in x or y value. Please try again")
    while x_name not in VALUES_LIST or y_name not in VALUES_LIST:
        try:
            x_and_y = input(PROMPT2)
            my_list = x_and_y.split(" ")
            x_name = my_list[0]
            y_name = my_list[1]
            if x_name not in VALUES_LIST or y_name not in VALUES_LIST:
                print("Error in x or y value. Please try again")
        except:
            pass
        
    # build x, the list of x values
    x_old = []
    position_x = VALUES_LIST.index(x_name)
    for k,v in dictionary.items():
        x_old.append(dictionary[k][position_x])
    
    x_2 = [ '%.2f' % elem for elem in x_old ]
    x = []
    for i in x_2:
        x.append(float(i))
    
    # build y, the list of y values
    
    y_old = []
    state_names = []
    position_y = VALUES_LIST.index(y_name)
    for k,v in dictionary.items():
        y_old.append(dictionary[k][position_y])
        state_names.append(k)
    
    y_2 = [ '%.2f' % elem for elem in y_old ]
    y = []
    for i in y_2:
        y.append(float(i))
    
    x_title = VALUES_NAMES[position_x]
    y_title = VALUES_NAMES[position_y]

    pylab.title(x_title+ " vs. "+ y_title)   # plot title

    pylab.xlabel(x_title)   #label x axis
    pylab.ylabel(y_title)   #label y axis
          
    pylab.scatter(x,y)
    
    for i, txt in enumerate(state_names): 
       pylab.annotate(txt, (x[i],y[i]))
    
    plot_regression(x,y)
    
    #USE ONLY ONE OF THESE TWO
    pylab.show()                # displays the plot      
    #pylab.savefig("plot.png")   # saves the plot to file plot.png
    
def main():
    fp = open_file()
    dictionary = gather_data(fp)
    print_data(dictionary)
    answer = input("Do you want to create a plot? ")
    if answer.lower() == "yes":
        plot(dictionary)
    else:
        pass
    
if __name__ == "__main__": 
    main()