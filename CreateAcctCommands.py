def createAcctIsUnique(user):

    try:
        isUnique = True

        credentials_file = open('credentials.txt', 'r')

        # Declare Line Counting Variable
        lineCount = 0

        # Read every line in file
        for line_of_text in credentials_file:

            lineNoSpace = line_of_text.strip() # remove White Space
            
            if (lineCount % 2 == 0): # Checks if Line is a Username Line (Even)
                if (lineNoSpace == user): # Checks if Username is already on file
                    isUnique = False # Returns false is Username is already used

            lineCount += 1 # Keeps count of Lines

        credentials_file.close # Closes file
        
        return isUnique
        
    except IOError:
        print('No File exists.')

def createAcctIsValid(user, pswd):

    isValid = False

    # Declare Username Validators
    userHasWhiteSpace = False

    # Declare Password Validators
    pswdHasWhiteSpace = False
    pswdHasNineChars = False
    pswdHasDigit = False
    pswdHasUpper = False
    pswdHasLower = False

    # Tests if username has White Space
    for temp in user:
        if (temp.isspace()):
            userHasWhiteSpace = True

    # Count for Password Validation        
    pswdCount = 0

    # Tests if Password is Valid (9 chars, 1 Upper, 1 Lower, 1 Digit)
    for temp in pswd:

        pswdCount += 1
        
        if (temp.isdigit()): # checks for digit in password
            pswdHasDigit = True

        if (temp.isupper()): # checks for upper case letter in password
            pswdHasUpper = True

        if (temp.islower()): # checks for lower case letter in password
            pswdHasLower = True

        if (temp.isspace()): # checks for space in password
            pswdHasWhiteSpace = True

        if (pswdCount >= 9): # checks if password is 9 chars long
            pswdHasNineChars = True

    # If every Validation is Passed, IsValid is returned as True
    if (userHasWhiteSpace == False and pswdHasWhiteSpace == False and pswdHasNineChars == True and pswdHasDigit == True and pswdHasUpper == True and pswdHasLower == True):
        isValid = True
    else:
        isValid = False

    return isValid

def createAcctFile(user, pswd):
    
    try:
        credentials_file = open('credentials.txt', 'a')
        
        credentials_file.write(user)
        credentials_file.write("\n")
        credentials_file.write(pswd)
        credentials_file.write("\n")
        
        credentials_file.close
        
    except IOError:
        print('No File exists.')

#int = createAcctIsUnique("Username")
#print(int)
#int = createAcctIsValid("Userna888me", "Pas888sword")
#print(int)
#createAcctFile("Username", "Password")
