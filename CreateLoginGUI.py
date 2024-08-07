# File for Login Window
import tkinter as tk
import LoginCommands
import SecretPhraseWindow

class createLoginGUI:
    def __init__ (self):

        self.main_win = tk.Tk() # create the main window
        self.main_win.title("Login") # title bar label
        self.main_win.minsize(width=500,height=325) # window size
        self.main_win.resizable(height = False, width = False) # locks window's width and height

        # Declare column and row sizes
        self.main_win.columnconfigure(0, minsize = 110)
        self.main_win.columnconfigure(1, minsize = 0)
        self.main_win.columnconfigure(2, minsize = 0)
        self.main_win.rowconfigure(0, minsize = 75)
        self.main_win.rowconfigure(1, minsize = 50)
        self.main_win.rowconfigure(2, minsize = 25)
        self.main_win.rowconfigure(3, minsize = 50)
        self.main_win.rowconfigure(4, minsize = 25)
        self.main_win.rowconfigure(5, minsize = 150)

        # Create Enter Username/Password Label (ROW 0)
        self.heading_label = tk.Label(text='Please enter your username and password.', # label
                                      font=("Helvetica Bold", 10), fg="black") # font, size, and color of label
        
        self.heading_label.grid(row=0, column=1) # label location

        # Create Username Label (ROW 1)
        self.heading_label = tk.Label(text='Username:', anchor = 'center', # label
                                      font=("Helvetica Bold", 14), fg="black") # font, size, and color of label
        
        self.heading_label.grid(row=1, column=1) # label location

        # Create Username TextBox (ROW 2)
        self.username_input = tk.Entry(justify = 'right',
                                      width = 20)
        
        self.username_input.grid(row=2,column=1, padx=0, pady=0, ipadx=0) # declare grid

        # Create Password Label (ROW 3)
        self.heading_label = tk.Label(text='Password:', # label
                                      font=("Helvetica Bold", 14), fg="black") # font, size, and color of label
        
        self.heading_label.grid(row=3, column=1) # label location

        # Create Password TextBox (ROW 4)
        self.password_input = tk.Entry(justify = 'right', show="*",
                                      width = 20)

        #self.password_input.config(show='*')
        self.password_input.grid(row=4,column=1, padx=0, pady=0, ipadx=0) # declare grid

        # Create Login Button (ROW 5)
        self.login_button = tk.Button(text=' Login ', command = lambda:loginPress(self),\
                                          font=("Times", 12))
        self.login_button.grid(row=5,column=1, padx=0, pady=0, ipadx=15)

        # Create Login Button function
        def loginPress(self):

            username = self.username_input.get()
            password = self.password_input.get()

            validLogin = LoginCommands.loginIsValid(username, password)

            if (validLogin == True):
                
                tk.messagebox.showinfo("Success!", 'Successful Login! Proceeding to program...') # Success dialogue box

                self.main_win.destroy() # destroy Login Window

                SecretPhraseWindow.secretPhraseWindow() # Creates Secret Phrase Game

            else:
                # Deletes input from Text Boxes
                self.username_input.delete(0, tk.END)
                self.password_input.delete(0, tk.END)
                
                tk.messagebox.showwarning("Error", 'Invalid Login') # Error dialogue box for Non Unique User

        #self.main_win.bind('<Return>', self.loginPress(self))

        self.main_win.bind('<Return>', (lambda event:loginPress(self)))
        
        tk.mainloop() # the main loop

# test function
#gui = createLoginGUI()
