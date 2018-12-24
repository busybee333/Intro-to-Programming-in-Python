############################################################################
#             User inputs code
#             Computer decodes until correct
############################################################################

def get_char(ch,shift):
     ''' takes ch, shifts it by shift and returns the shifted character'''
     alphabet = "abcdefghijklmnopqrstuvwxyz"
     new_string = ""
     if ch == " ":
         new_string += " "
     elif ch == ".":
         new_string += "."
     elif ch == ";":
         new_string += ";"
     elif ch == ",":
         new_string += ","
     elif ch == "'":
         new_string += "'"
     else:
         ch_pos = alphabet.index(ch.lower())
         new_pos = (ch_pos + shift) % 26
         new_char = alphabet[new_pos]
         new_string += new_char
     return new_string
       
def get_shift(s):
     ''' finds the shift from e'''
     alphabet = "abcdefghijklmnopqrstuvwxyz"
     global readable
     shift =  alphabet.index('e') - alphabet.index(s)
     return shift
          
def output_plaintext(s,shift):
     ''' prints the output in upper case'''
     print(s.upper(), end = "")

def get_ignore(letter, text):
     '''gets the list of letters that haven't been used as the max letter'''
     new = ""
     for i in text:
         if i == letter:
             new += letter.replace(letter,'')
         else:
             new += i
     return new

def main():
     alphabet = "abcdefghijklmnopqrstuvwxyz"
     
     #prompts user for input
     print("Cracking a Caesar cypher.")
     print('')
     ct = input("Input cipherText: ")
     cipherText = ct.lower()
     print('')
     #finds most common letter in string
     max_count = 0
     max_letter = ""
     for i in alphabet:
         if i == " ":
             pass
         elif cipherText.count(i) > max_count:
             max_letter = i
             max_count = cipherText.count(i)

     key = get_shift(max_letter)   
     for i in cipherText:
         ch = get_char(i, key)
         output_plaintext(ch, 0)
    
     print(" ")
     print("")
     readable = input("Is the plaintext readable as English? (yes/no): ")
     if readable.lower() == "yes":
         pass
     else:
         while readable == "no":
             ignored = get_ignore(max_letter, cipherText)
             alphabet = alphabet.replace(max_letter,'')
             max_count = 0
             max_letter = ""
             for i in alphabet:
                 if i == " ":
                     pass
                 elif ignored.count(i) > max_count:
                     max_letter = i
                     max_count = ignored.count(i)
                     
             key = get_shift(max_letter)   
             for i in cipherText:
                 ch = get_char(i, key)
                 output_plaintext(ch, 0)
             
             print("")
             print("")
             readable = input("Is the plaintext readable as English? (yes/no): ")
             if readable == "yes":
                 break
     
             
if __name__ == "__main__": 
     main()

