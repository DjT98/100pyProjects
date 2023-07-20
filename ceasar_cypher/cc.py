#let's import string
import string

# Let's create a list of alphabets which we'll use for encryption
alphabets = list((string.ascii_lowercase + string.ascii_uppercase)*2)

#let's create the main function that will run this program
def ceasar_cypher():

    #let's get user's intention, whether they want to encrypt or decrypt
    crypt = input("Do you wish to encrypt or decrypt?\n").lower

    #let's creat a list of keywords we expect from users
    crypt_response = ['decrypt', 'encrypt']

    
    #let's force the user to put only the information we need
    while crypt not in crypt_response:
        crypt = input('Please enter the right keyword❗, type in "encrypt" to encrypt or type in "decrypt" to decrypt\n')
    
    
#     let's get the user shift key which will use in encrypting and decrypting
#     and also capture and eliminate possible errors when the user tries putting anything else but integer
    while True:
        try:
            shift = int(input("Type the shift number:\n"))
        except:
            print('Please make sure you only typed in an integer for your encrypt/decrypt shift number:\n')
            continue
        else:
            print('Great that is an integer\n')
            break
            
            
    #let's mod the user preferred shift number by half the alphabets total number to avoid running out of range when the users uses a high shift number    
    shift %= 52  
    shift += 3
    
    #let's put a code that will convert the shift number to a negative shift number so that we can run decryption when user chooses decryption
    if crypt == 'decrypt':
        shift = shift *-1

    #let's get user's text which is to be encrypted or decrypted
    message = input('Please type in or paste the text you want to encrypt or decrypt:\n')

    # let's create an empty string where we will add all the encrypted/decrypted characters
    end_result = ''


    #let's make the encryption/decryption
    for char in message:
        if char in alphabets:
            position = alphabets.index(char)
            end_position = position + shift
            end_result += alphabets[end_position]
        else:
            end_result += char

    #print out the encrypted/decrypted texts accordingly
    print(f'\nYour {crypt}ed texts are as follows⤵:\n{end_result}')
    
    
# run the function    
ceasar_cypher()


#let's create a list of keywords we expect from users in other for them to run or quit the program
rerun_response = ['yes', 'no']


#let's make automate the running and quitting
rerun = True
while rerun:
    cypher_rerun = input('\nHey! would you like to use this program again🙃? type "yes" to continue or "no" to discontinue\n').lower()

    while cypher_rerun not in rerun_response:
        cypher_rerun = input('\nPlease use the right keyword to use this program again😐, type "yes" to continue or "no" to discontinue\n').lower()
    if cypher_rerun == 'yes':
        ceasar_cypher()
    else:
        print('Thank you for using Ceasar Cypher program.\n')
        rerun = False
