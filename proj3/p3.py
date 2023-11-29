import os # allows me to interact w/ the OS - https://www.edureka.co/blog/os-module-in-python#:~:text=The%20OS%20module%20in%20Python%20is%20a%20part%20of%20the,in%20day%20to%20day%20programming.
import random # module of functions for generating / manipulating random ints - https://www.toppr.com/guides/python-guide/tutorials/modules/modules/random/use-random-module-to-generate-random-numbers-in-python/#:~:text=Q1.-,What%20is%20import%20random%20in%20Python%3F,random%20number%20generation%2Drelated%20functions.
import string # module containing constants, utility functions and classes for string manipulation - https://www.digitalocean.com/community/tutorials/python-string-module

def generate_password(length, include_characters=True, include_numbers=True, include_symbols=True, exclude_characters=""): # defines a function taking parameters for length of password and optional parameters to include characters, numbers, symbols and exclude specific characters
    characters = string.ascii_letters if include_characters else "" #creates variable called characters including ascii letters - https://docs.python.org/3/library/string.html
    characters += string.digits if include_numbers else "" #creates variable called characters including digits - https://docs.python.org/3/library/string.html
    characters += string.punctuation if include_symbols else "" #creates variable called characters including symbols - https://docs.python.org/3/library/string.html

    # Removes characters which are set in the 'exclude_characters' from function generate_password - https://www.w3schools.com/python/ref_string_join.asp
    characters = ''.join(char for char in characters if char not in exclude_characters) #.join joins characters into new string

    if not characters: #checks if characters string is empty - https://www.geeksforgeeks.org/python-if-with-not-operator/
        print "Select at least one option for password generation." #prints if empty
        return None # returns none otherwise

    password = ''.join(random.choice(characters) for _ in range(length)) #generates a password of the length requested by selecting random characters and joined together - https://www.geeksforgeeks.org/random-choices-method-in-python/
    return password #returns the created password

def generate_username(keyword, length, include_characters=True, include_numbers=True, include_symbols=True, exclude_characters=""): # defines a function taking parameters for length of password and optional parameters to include characters, numbers, symbols and exclude specific characters
    characters = string.ascii_letters if include_characters else "" #creates variable called characters including ascii letters - https://docs.python.org/3/library/string.html
    characters += string.digits if include_numbers else "" #creates variable called characters including digits - https://docs.python.org/3/library/string.html
    characters += string.punctuation if include_symbols else "" #creates variable called characters including symbols - https://docs.python.org/3/library/string.html

    # Removes characters which are set in the 'exclude_characters' from function generate_password - https://www.w3schools.com/python/ref_string_join.asp
    characters = ''.join(char for char in characters if char not in exclude_characters) #.join joins characters into new string

    if not characters: #checks if characters string is empty -  https://www.geeksforgeeks.org/python-if-with-not-operator/
        print "Select at least one option for username generation." #prints if empty
        return None # returns none otherwise

    username = keyword[:min(length, len(keyword))]  
    remaining_length = length - len(username) # username variable is assigned keyword taking the min length between the requested length and the keyword input and remaining length is used to see how many more characters are needed - https://www.w3schools.com/python/ref_func_min.asp & https://www.w3schools.com/python/ref_func_len.asp

    if remaining_length > 0:
        username += ''.join(random.choice(characters) for _ in range(remaining_length)) #remaining_length checks if there is still remaining length needed for the password and if there is, random characters are selected and joined to the existing username 

    return username #returns the new username variable

def export_to_file(username, password, file_number): # new function that will export file to desktop and number it accordingly
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop") #gets home path of user with ~ being home directory
    file_name = "upass{}.txt".format(file_number) #inserts file_number into file name w/respective number
    file_path = os.path.join(desktop_path, file_name) #joins path and file name to make full path to file

    try: #start of error checking
        with open(file_path, "w") as file: #tries to open file path in writing mode - https://www.geeksforgeeks.org/python-open-function/
            file.write("Generated Username: {}\n".format(username)) #writes username to file - https://www.geeksforgeeks.org/writing-to-file-in-python/
            file.write("Generated Password: {}\n".format(password))#writes password to file - https://www.geeksforgeeks.org/writing-to-file-in-python/
    except IOError: #this is exception caught if try fails and prints following message - https://www.askpython.com/python/examples/handling-ioerrors

        print "Error writing to file. Please check file permissions."

    print "User and password information exported to: {}".format(file_path) #prints message showing specific file path

def find_next_file_number(): #creates function that includes a loop to check if the file number 1 exists in file name and if it does, adds a 1 to name the next file 2, 3 and so on but continues to check each time in the loop until that number is not found.
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop") #creates pathway to home directory
    file_number = 1 #sets variable file_number to 1
    while True: # start of while loop -  https://www.geeksforgeeks.org/python-while-loop/
        file_path = os.path.join(desktop_path, "upass{}.txt".format(file_number)) # creates full path to file on desktop based on file number
        if not os.path.isfile(file_path): #checks if file path (from file_path) exists
            return file_number #executes if file path does not exist
        file_number += 1 #executes if file path does exist

def get_yes_no_input(prompt): #creates function
    while True: #starts while loop
        response = raw_input(prompt).lower() #prompts user and stores in variable response - https://pythonguides.com/python-input-and-raw_input-function/
        if response in ['y', 'yes']: #checks if response is either option - https://www.geeksforgeeks.org/python3-if-if-else-nested-if-if-elif-statements/
            return True #returns if true
        elif response in ['n', 'no']: #checks if response is either option otherwise
            return False # returns if true
        else: # if neither option is true, responds with this
            print "Invalid input. Please enter 'yes' or 'no'."

def get_integer_input(prompt):#creates function
    while True: #starts while loop
        try: #start of error checking
            value = int(raw_input(prompt)) #converts users response into int and stores in value
            return value # returns value data if no error
        except ValueError: #executes if error found in try script and prints error message
            print "Invalid input. Please enter a valid integer."

def main(): #main function created
    print "Password and Username Generator" #prints title of function

    username_length = get_integer_input("Enter the desired username length: ") # function call has user enter desired length for username and assigned to new variable
    keyword = raw_input("Enter a keyword for the username: ") # prompts user for keyword and assigns to new variable

    exclude_username = raw_input("Enter characters to exclude from username (comma-separated, or press Enter for none): ") # asks user for any excluded characters and assigns to variable

    include_username_characters = get_yes_no_input("Include characters in username? (y/n): ") #asks user for yes or no answer and function checks input for validation
    include_username_numbers = get_yes_no_input("Include numbers in username? (y/n): ") #asks user for yes or no answer and function checks input for validation
    include_username_symbols = get_yes_no_input("Include symbols in username? (y/n): ") #asks user for yes or no answer and function checks input for validation

    while True: #start of while loop
        password_length = get_integer_input("Enter the password length: ") # function call has user enter desired length for username and assigned to new variable
        exclude_password = raw_input("Enter characters to exclude from password (comma-separated, or press Enter for none): ") # asks user for any excluded characters and assigns to variable

        include_password_characters = get_yes_no_input("Include characters in password? (y/n): ") #asks user for yes or no answer and function checks input for validation
        include_password_numbers = get_yes_no_input("Include numbers in password? (y/n): ") #asks user for yes or no answer and function checks input for validation
        include_password_symbols = get_yes_no_input("Include symbols in password? (y/n): ") #asks user for yes or no answer and function checks input for validation

        file_number = find_next_file_number() # calls function to dtermine file number and assigns it to variable

        username = generate_username( 
            keyword,
            username_length,
            include_characters=include_username_characters,
            include_numbers=include_username_numbers,
            include_symbols=include_username_symbols,
            exclude_characters=exclude_username
        ) #function called to create user name and store in username varialbe

        password = generate_password(
            password_length,
            include_characters=include_password_characters,
            include_numbers=include_password_numbers,
            include_symbols=include_password_symbols,
            exclude_characters=exclude_password
        ) #function called to create password and store in username varialbe

        if username and password: #if checks to see that username and password are both greater than 0 - https://www.geeksforgeeks.org/python3-if-if-else-nested-if-if-elif-statements/
            export_to_file(username, password, file_number) #if true, export to file function is called
            break #breaks while loop to end after exporting script

if __name__ == "__main__": #checks if script is run directly and not as module
    main() # if true, main function is called and executed

