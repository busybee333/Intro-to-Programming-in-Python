# -*- coding: utf-8 -*-
##########################################################
#         Warns user about hacking
#         Prompts user for method of hacking
#         Uses method(s) user chooses & finds password
#         Repeats until user quits
###########################################################


import zipfile
from itertools import product
import time

def open_dict_file():
    '''Asks user for file name and returns file pointer to the dicitonary file'''
    dict_file_name = input("Enter dictionary file name: ")
    while True:    
        try:
            fp = open(dict_file_name, 'r')
            return fp
        except:
            dict_file_name = input("Enter dictionary file name: ")

def open_zip_file():
    '''Asks user for zip file name and returns a file pointer to the zip file'''
    zip_file_name = input("Enter zip file name: ")
    while True:
        try:
            z_file = zipfile.ZipFile(zip_file_name)
            return z_file
        except:
            zip_file_name = input("Enter zip file name: ")
    
def brute_force_attack(zip_file):
    '''Uses brute force to determine what the password is'''
    for items in product('abcdefghijklmnopqrstuvwxyz1234567890', repeat = 3):
        password = (''.join(items))
        try:
            zip_file.extractall(pwd=password.encode())
            print("Brute force password is " + password)
            break
        except:
            pass
    zip_file.close()
    
def dictionary_attack(zip_file, dict_file):
    '''Uses a text file to determine if the text file contains the password to open a zip file'''
    for line in dict_file:
        password = line.strip()
        try:
            zip_file.extractall(pwd=password.encode())
            print("Dictionary password is " + password)
            break
        except:
            pass
    try:
        zip_file.extractall(pwd=password.encode())
    except:
        print("No password found.")
        return False
    dict_file.close()
    zip_file.close()

print("Cracking zip files.")
print("Warning cracking passwords is illegal due to law 1029 and has a prison term of up to 20 years")

for i in range(100):
    crack_type = input("What type of cracking ('brute force', 'dictionary', 'both', 'q'): ")

    if crack_type.lower() == "brute force":
        print()
        print("Brute Force Cracking")
        zip_file = open_zip_file()
        start = time.process_time()
        brute_force_attack(zip_file)
        end = time.process_time()
        difference = end - start
        print("{:s} {:.4f}".format("Elapsed time (sec)", difference))
    
    elif crack_type.lower() == "dictionary":
        print()
        print("Dictionary Cracking")
        dict_file = open_dict_file()
        zip_file = open_zip_file()
        start = time.process_time()
        dictionary_attack(zip_file, dict_file)
        end = time.process_time()
        difference = end - start
        print("{:s} {:.4f}".format("Elapsed time (sec)", difference))
        
    elif crack_type.lower() == "both":
        print()
        print("Both Brute Force and Dictionary attack.")
        dict_file = open_dict_file()
        zip_file = open_zip_file()
        start = time.process_time()
        deter =  dictionary_attack(zip_file, dict_file)
        end = time.process_time()
        difference = end - start
        print("{:s} {:.4f}".format("Dictionary Elapsed time (sec)", difference))
        if deter == False:
            start = time.process_time()
            brute_force_attack(zip_file)
            end = time.process_time()
            difference = end - start
            print("{:s} {:.4f}".format("Brute Force Elapsed time (sec)", difference))
        else:
            pass
    elif crack_type.lower() == "q":
        break