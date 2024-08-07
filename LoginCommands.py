def loginIsValid(user, pswd):

    try:
        isValid = False

        credentials_file = open('credentials.txt', 'r') # Open file

        # Declare line counting variable
        lineCount = 0
        usernameFound = False

        for line_of_text in credentials_file:

            lineNoSpace = line_of_text.strip() #Removes white space

            if (lineCount % 2 == 0): #checks if line is a username line (odd #)
                if (lineNoSpace == user): # checks if line is equal to entered username
                    usernameFound = True
                    passwordLine = lineCount + 1 # writes the password line as the line after found username

            if (usernameFound == True and lineCount == passwordLine): # Checks if password matches username
                if (lineNoSpace == pswd):
                    isValid = True

            lineCount += 1 # Update line count

        credentials_file.close # Close file

        return isValid


    except IOError:
        print('No file exists.')

#loginValid = loginIsValid("Username", "Password")
#print(loginValid)
