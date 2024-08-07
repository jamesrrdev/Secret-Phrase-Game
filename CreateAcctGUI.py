# File for Create Account Window
import tkinter as tk
import tkinter.messagebox
import CreateAcctCommands
import SecretPhraseWindow


class createAcctGUI:
    def __init__ (self):

        self.main_win = tk.Tk() # create the main window
        self.main_win.title("Create Account") # title bar label
        self.main_win.minsize(width=500,height=375) # window size
        self.main_win.resizable(height = False, width = False) # locks window's width and height


        # Declare column and row sizes
        self.main_win.columnconfigure(0, minsize = 88)
        self.main_win.columnconfigure(1, minsize = 0)
        self.main_win.columnconfigure(2, minsize = 0)
        self.main_win.rowconfigure(0, minsize = 100)
        self.main_win.rowconfigure(1, minsize = 50)
        self.main_win.rowconfigure(2, minsize = 25)
        self.main_win.rowconfigure(3, minsize = 50)
        self.main_win.rowconfigure(4, minsize = 25)
        self.main_win.rowconfigure(5, minsize = 50)
        self.main_win.rowconfigure(6, minsize = 25)
        self.main_win.rowconfigure(7, minsize = 100)

        # Create Password Requirements Label (ROW 0)
        self.heading_label = tk.Label(text='Password Requires At Least:\n 9 characters\n1 digit, upper-case letter, and lower-case letter', # label
                                      font=("Helvetica Bold", 10), fg="black") # font, size, and color of label
        
        self.heading_label.grid(row=0, column=1) # label location

        # Create Username Label (ROW 1)
        self.heading_label = tk.Label(text='Create your username (no spaces):', # label
                                      font=("Helvetica Bold", 14), fg="black") # font, size, and color of label
        
        self.heading_label.grid(row=1, column=1) # label location


        # Create Username TextBox (ROW 2)
        self.username_input = tk.Entry(justify = 'right',
                                      width = 20)
        self.username_input.grid(row=2,column=1, padx=0, pady=0, ipadx=0) # declare grid

        # Create Password Label (ROW 3)
        self.heading_label = tk.Label(text='Create your password:', # label
                                      font=("Helvetica Bold", 14), fg="black") # font, size, and color of label
        
        self.heading_label.grid(row=3, column=1) # label location

        # Create Password TextBox (ROW 4)
        self.password_input = tk.Entry(justify = 'right', show="*",
                                      width = 20)
        self.password_input.grid(row=4,column=1, padx=0, pady=0, ipadx=0) # declare grid

        # Create Confirm Password Label (ROW 5)
        self.heading_label = tk.Label(text='Confirm password:', # label
                                      font=("Helvetica Bold", 14), fg="black") # font, size, and color of label
        
        self.heading_label.grid(row=5, column=1) # label location

        # Create Confirm Password TextBox (ROW 6)
        self.confirm_password_input = tk.Entry(justify = 'right', show="*",
                                      width = 20)
        self.confirm_password_input.grid(row=6,column=1, padx=0, pady=0, ipadx=0) # declare grid

        # Create CreateAcct Button
        self.login_button = tk.Button(text=' Create Account ', command = lambda:createAcctPress(self),\
                                          font=("Times", 12))
        self.login_button.grid(row=7,column=1, padx=20, pady=0, ipadx=15)

        # Create Account Button function
        def createAcctPress(self):

            # Writes credentials to string
            username = self.username_input.get()
            password = self.password_input.get()
            confirm_password = self.confirm_password_input.get()

            # Tests if Password matches confirm password
            if (password == confirm_password):

                isUnique = CreateAcctCommands.createAcctIsUnique(username) # Calls function to test if Username is unique
                isValid = CreateAcctCommands.createAcctIsValid(username, password) # Calls function to test if Username and Password are valid

                if (isUnique == True and isValid == True):
                    CreateAcctCommands.createAcctFile(username, password) # Calls function to Write Username and Password to File
                    
                    tk.messagebox.showinfo("Success!", 'Account was successfully created!') # Success dialogue box

                    self.main_win.destroy() # Destroys window

                    SecretPhraseWindow.secretPhraseWindow() # Creates Secret Phrase Game

                elif (isUnique == False):

                    # Deletes input from Text Boxes
                    self.username_input.delete(0, tk.END)
                    self.password_input.delete(0, tk.END)
                    self.confirm_password_input.delete(0, tk.END)
                    
                    tk.messagebox.showwarning("Invalid Credentials", 'Username is already in use') # Error dialogue box for Non Unique User

                elif (isValid == False):

                    # Deletes input from Text Boxes
                    self.username_input.delete(0, tk.END)
                    self.password_input.delete(0, tk.END)
                    self.confirm_password_input.delete(0, tk.END)
                    
                    tk.messagebox.showwarning("Invalid Credentials", 'Username or password is invalid') # Error dialogue box for Invalid Credentials
                
            else:

                # Deletes input from Text Boxes
                self.username_input.delete(0, tk.END)
                self.password_input.delete(0, tk.END)
                self.confirm_password_input.delete(0, tk.END)
                
                tk.messagebox.showwarning("Invalid Credentials", 'Password does not match Confirm Password') # Error dialogue box

        self.main_win.bind('<Return>', (lambda event:createAcctPress(self)))
        
        tk.mainloop() # the main loop

# test function
# gui = createAcctGUI()