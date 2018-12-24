    ###########################################################
    #  Computer Project #1
    #
    #  Algorithm
    #    prompt for an integer
    #    input an integer
    #    print given integer
    #       convert integer to different units
    #    output the different units and their values
    ###########################################################

#Asks user for number of rods and gives back number of rods in decimal form, if not already in decimal form
num_str = input( "Input rods: " )
num_float = float( num_str )
print( "You input " + str( num_float ) + " rods." )

#Variables that have all the math done within the variable
meters = str( num_float * 5.0292 )                                              #Converts rods to meters
feet = str( float( meters ) / 0.3048 )                                          #Converts meters to feet
miles = str( float( meters ) / 1609.34 )                                        #Converts meters to miles
furlongs = str( num_float / 40 )                                                #Converts rods to furlongs
minutes = str( float( miles ) * ( 60 / 3.1 ) )                                  #Converts miles to minutes

#Prints all the calculations
print( "Conversions" )
print( "Meters: " + meters )
print( "Feet: " + feet )
print( "Miles: " + miles )
print( "Furlongs: " + furlongs )
print( "Minutes to walk " + str( num_float ) + " rods: " + minutes )