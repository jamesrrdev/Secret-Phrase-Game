# Main for Secret Phrase Game Program

import CreateAcctGUI
import CreateLoginGUI
import tkinter as tk

# Main
def main():

    gui = rootGUI() # creates initial gui window

# CreateAcct Window Function
def createAcct():
    print ("Creating CreateAcct Window")

    createAccountGUI = CreateAcctGUI.createAcctGUI()

# Login Window Function
def login():
    print ("Creating Login Window")

    loginGUI = CreateLoginGUI.createLoginGUI()
    
# Initial GUI Class
class rootGUI:
    def __init__ (self):

        print('Creating RootGUI Window') # Announces creation of window

        self.main_win = tk.Tk() # create the main window
        self.main_win.title("Secret Phrase Game Program") # title bar label
        self.main_win.minsize(width=500,height=250) # window size
        self.main_win.resizable(height = False, width = False) # locks window's width and height

        # Declare column and row sizes
        self.main_win.columnconfigure(0, minsize = 0)
        self.main_win.columnconfigure(1, minsize = 0)
        self.main_win.columnconfigure(2, minsize = 0)
        self.main_win.rowconfigure(0, minsize = 75)
        self.main_win.rowconfigure(1, minsize = 200)
        self.main_win.rowconfigure(2, minsize = 75)

        # Create Label
        self.heading_label = tk.Label(text='Secret Phrase Game', # label
                                      font=("Helvetica Bold", 24), fg="blue") # font, size, and color of label
        
        self.heading_label.grid(row=0, column=1) # label location


        # Create Cancel Button
        self.cancel_button = tk.Button(text=' Cancel ', command = self.main_win.destroy,\
                                          font=("Times", 14)) # declare font
        self.cancel_button.grid(row=2,column=0, padx=20, pady=0, ipadx=15) # declare grid


        # Create CreateAcct Button
        self.createacct_button = tk.Button(text=' Create Account ', command = lambda:createAcctPress(self),\
                                          font=("Times", 14))
        self.createacct_button.grid(row=2,column=1, padx=20, pady=0, ipadx=15) # declare grid

        # Create Login Button
        self.login_button = tk.Button(text=' Login ', command = lambda:loginPress(self),\
                                          font=("Times", 14))
        self.login_button.grid(row=2,column=2, padx=20, pady=0, ipadx=15)

        # Executes when Create Account Button is pressed
        def createAcctPress(self):
            self.main_win.destroy()

            createAcct()

        # Executes when Login Button is pressed
        def loginPress(self):
            self.main_win.destroy()

            login()

       # photo = tk.PhotoImage(file = "thought_bubble.jpg")
       # self.labelGIF = tk.Label(image = photo)
       # self.labelGIF.image = photo
       # self.labelGIF.grid(row=1, column=1) # photo location
        
        tk.mainloop() # the main loop

main()
