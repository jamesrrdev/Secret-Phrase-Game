import tkinter as tk
import tkinter.messagebox
import SecretPhraseFunctions

class secretPhraseWindow:
    def __init__ (self):

        # MAIN WINDOW
        self.main_win = tk.Tk() # create the main window
        self.main_win.title("Secret Phrase Program") # title bar label
        self.main_win.minsize(width=850,height=800) # window size
        self.main_win.resizable(height = False, width = False) # locks window's width and height

        # Finds the starting random word
        self.randomWord = SecretPhraseFunctions.randomWord()

        # Create points variable
        self.totalPoints = 0
        
        # Row Configuration
        for c in range(14):
            self.main_win.columnconfigure(c, minsize = 15)

        for r in range(7):
            self.main_win.rowconfigure(r, minsize = 75)

        self.main_win.rowconfigure(7, minsize = 100)
        self.main_win.rowconfigure(8, minsize = 100)
        self.main_win.rowconfigure(9, minsize = 5)

        # Create New Menu Bar
        self.menu_bar = tk.Menu()

        # Create New Menu
        newmenu = tk.Menu(self.menu_bar, tearoff=0)
        newmenu.add_command(label="New Word", command = lambda:newWord(self))
        newmenu.add_command(label="Check Points", command = lambda:checkPoints(self))
        self.menu_bar.add_cascade(label="New", menu=newmenu)

        # Create Help Menu
        helpmenu = tk.Menu(self.menu_bar, tearoff=0)
        helpmenu.add_command(label="Color Legend", command = lambda:colorLegend(self))
        helpmenu.add_command(label="Help", command = lambda:help(self))
        helpmenu.add_command(label="Points Help", command = lambda:pointsHelp(self))
        self.menu_bar.add_cascade(label="Help", menu=helpmenu)

        self.main_win.config(menu=self.menu_bar)

        # Create Entry Box
        entry_word = ""
        
        self.entry_box = tk.Entry(width=10, bg="cyan", justify="center", textvariable=entry_word)
        self.entry_box.grid(row=7, column=7, pady=20)
        
        # A Button
        self.a_button = tk.Button(text=' A ', bg = "cyan", command = lambda:insertLetter(self, 'A'),\
                                          font=("Times", 14))
        self.a_button.grid(row=8,column=1, pady=0, ipadx=12)

        # B Button
        self.b_button = tk.Button(text=' B ', bg = "cyan", command = lambda:insertLetter(self, 'B'),\
                                          font=("Times", 14))
        self.b_button.grid(row=8,column=2, pady=0, ipadx=12)

        # C Button
        self.c_button = tk.Button(text=' C ', bg = "cyan", command = lambda:insertLetter(self, 'C'),\
                                          font=("Times", 14))
        self.c_button.grid(row=8,column=3, pady=0, ipadx=12)

        # D Button
        self.d_button = tk.Button(text=' D ', bg = "cyan", command = lambda:insertLetter(self, 'D'),\
                                          font=("Times", 14))
        self.d_button.grid(row=8,column=4, pady=0, ipadx=12)

        # E Button
        self.e_button = tk.Button(text=' E ', bg = "cyan", command = lambda:insertLetter(self, 'E'),\
                                          font=("Times", 14))
        self.e_button.grid(row=8,column=5, pady=0, ipadx=12)

        # F Button
        self.f_button = tk.Button(text=' F ', bg = "cyan", command = lambda:insertLetter(self, 'F'),\
                                          font=("Times", 14))
        self.f_button.grid(row=8,column=6, pady=0, ipadx=12)

        # G Button
        self.g_button = tk.Button(text=' G ', bg = "cyan", command = lambda:insertLetter(self, 'G'),\
                                          font=("Times", 14))
        self.g_button.grid(row=8,column=7, pady=0, ipadx=12)

        # H Button
        self.h_button = tk.Button(text=' H ', bg = "cyan", command = lambda:insertLetter(self, 'H'),\
                                          font=("Times", 14))
        self.h_button.grid(row=8,column=8, pady=0, ipadx=12)

        # I Button
        self.i_button = tk.Button(text=' I ', bg = "cyan", command = lambda:insertLetter(self, 'I'),\
                                          font=("Times", 14))
        self.i_button.grid(row=8,column=9, pady=0, ipadx=15)

        # J Button
        self.j_button = tk.Button(text=' J ', bg = "cyan", command = lambda:insertLetter(self, 'J'),\
                                          font=("Times", 14))
        self.j_button.grid(row=8,column=10, pady=0, ipadx=17)

        # K Button
        self.k_button = tk.Button(text=' K ', bg = "cyan", command = lambda:insertLetter(self, 'K'),\
                                          font=("Times", 14))
        self.k_button.grid(row=8,column=11, pady=0, ipadx=12)

        # L Button
        self.l_button = tk.Button(text=' L ', bg = "cyan", command = lambda:insertLetter(self, 'L'),\
                                          font=("Times", 14))
        self.l_button.grid(row=8,column=12, pady=0, ipadx=12)

        # M Button
        self.m_button = tk.Button(text=' M ', bg = "cyan", command = lambda:insertLetter(self, 'M'),\
                                          font=("Times", 14))
        self.m_button.grid(row=8,column=13, pady=0, ipadx=12)

        # N Button
        self.n_button = tk.Button(text=' N ', bg = "cyan", command = lambda:insertLetter(self, 'N'),\
                                          font=("Times", 14))
        self.n_button.grid(row=9,column=1, pady=0, ipadx=12)

        # O Button
        self.o_button = tk.Button(text=' O ', bg = "cyan", command = lambda:insertLetter(self, 'O'),\
                                          font=("Times", 14))
        self.o_button.grid(row=9,column=2, pady=0, ipadx=12)

        # P Button
        self.p_button = tk.Button(text=' P ', bg = "cyan", command = lambda:insertLetter(self, 'P'),\
                                          font=("Times", 14))
        self.p_button.grid(row=9,column=3, pady=0, ipadx=12)

        # Q Button
        self.q_button = tk.Button(text=' Q ', bg = "cyan", command = lambda:insertLetter(self, 'Q'),\
                                          font=("Times", 14))
        self.q_button.grid(row=9,column=4, pady=0, ipadx=12)

        # R Button
        self.r_button = tk.Button(text=' R ', bg = "cyan", command = lambda:insertLetter(self, 'R'),\
                                          font=("Times", 14))
        self.r_button.grid(row=9,column=5, pady=0, ipadx=12)

        # S Button
        self.s_button = tk.Button(text=' S ', bg = "cyan", command = lambda:insertLetter(self, 'S'),\
                                          font=("Times", 14))
        self.s_button.grid(row=9,column=6, pady=0, ipadx=12)

        # T Button
        self.t_button = tk.Button(text=' T ', bg = "cyan", command = lambda:insertLetter(self, 'T'),\
                                          font=("Times", 14))
        self.t_button.grid(row=9,column=7, pady=0, ipadx=12)

        # U Button
        self.u_button = tk.Button(text=' U ', bg = "cyan", command = lambda:insertLetter(self, 'U'),\
                                          font=("Times", 14))
        self.u_button.grid(row=9,column=8, pady=0, ipadx=12)

        # V Button
        self.v_button = tk.Button(text=' V ', bg = "cyan", command = lambda:insertLetter(self, 'V'),\
                                          font=("Times", 14))
        self.v_button.grid(row=9,column=9, pady=0, ipadx=12)

        # W Button
        self.w_button = tk.Button(text=' W ', bg = "cyan", command = lambda:insertLetter(self, 'W'),\
                                          font=("Times", 14))
        self.w_button.grid(row=9,column=10, pady=0, ipadx=12)

        # X Button
        self.x_button = tk.Button(text=' X ', bg = "cyan", command = lambda:insertLetter(self, 'X'),\
                                          font=("Times", 14))
        self.x_button.grid(row=9,column=11, pady=0, ipadx=12)

        # Y Button
        self.y_button = tk.Button(text=' Y ', bg = "cyan", command = lambda:insertLetter(self, 'Y'),\
                                          font=("Times", 14))
        self.y_button.grid(row=9,column=12, pady=0, ipadx=12)

        # Z Button
        self.z_button = tk.Button(text=' Z ', bg = "cyan", command = lambda:insertLetter(self, 'Z'),\
                                          font=("Times", 14))
        self.z_button.grid(row=9,column=13, pady=0, ipadx=13)

        # POINTS WINDOW
        self.points_win = tk.Tk() # create the main window
        self.points_win.title("Points") # title bar label
        self.points_win.minsize(width=300,height=300) # window size
        self.points_win.resizable(height = False, width = False) # locks window's width and height

        # Create rows and Columns
        for r in range(6):
            self.points_win.rowconfigure(r, minsize = 50)

        for c in range(6):
            self.points_win.columnconfigure(c, minsize = 50)

        # Create label for the total points
        self.total_points_label = tk.Label(self.points_win, text = "Total Points:", padx=12, pady=6, font=("Helvetica", 24))

        # Attach to grid
        self.total_points_label.grid(row=1, column=1)

        # Convert total points to string
        self.strTotalPoints = str(self.totalPoints)

        # Create the display of the total points
        self.total_points = tk.Label(self.points_win, text = self.strTotalPoints, padx=12, pady=6, font=("Helvetica Bold", 24))

        # Attach to grid
        self.total_points.grid(row=3, column=2)

        # Function for button presses
        def insertLetter(self, letter):

            self.entry_box.insert(100, letter)

        # Function for when the user enters input
        def entryEnter(self):

            user_entry = self.entry_box.get() # grabs the user's input

            user_entry = user_entry.upper() # converts users guess to uppercase

            self.entry_box.delete(0, 100) # deletes the input in the entry box

            # If the user has guesses left
            if (self.row_num < 6):

                # If the entry is 5 chars
                if (len(user_entry) == 5):
                    checkWord(self, user_entry)

                else :
                    tk.messagebox.showwarning("Invalid Input", 'Please enter a 5 letter word') # Tells user their input is invalid

            else:
                tk.messagebox.showwarning("Game Over", 'You are out of guesses! Select "New Word" when you are ready to continue!') # Error dialogue box for Non Unique User

        # Bind the Enter Key to the Window
        self.main_win.bind('<Return>', (lambda event:entryEnter(self)))

        self.row_num = 1

        # Checks if Guess matches the Word and displays it on the Window
        def checkWord(self, entry):

            # Call Letter Count and Column Num Variables
            letter_count = 0
            column_num = 3

            # Checks each letter in the entry
            for letter in entry:

                # Call background color variable
                background = ""

                # Correct Letter : Green Background
                if (letter == self.randomWord[letter_count]):
                    background = "green"

                    # Changes the Button Background to Green
                    changeButton(self, letter, 'normal', background, 'false')

                # Letter is in word but not in right place : Orange Background
                elif (letter == self.randomWord[0] or letter == self.randomWord[1] or letter == self.randomWord[2] or letter == self.randomWord[3] or letter == self.randomWord[4]) :
                    background = "orange"

                    # Changes the Button Background to Orange
                    changeButton(self, letter, 'normal', background, 'false')

                # Letter is not in word : Red Background
                else :
                    background = "red"

                    changeButton(self, letter, 'disabled', background, 'false')

                # Creates the Label for the letter
                self.word_char = tk.Label(text = letter, bg = background, padx=12, pady=6, font=("Helvetica Bold", 24))

                self.word_char.grid(row=self.row_num, column=column_num)

                # Adds iteration to the Letter and Column num
                letter_count += 1
                column_num += 2

            if (self.randomWord == entry):

                # Points algorithm (Start out with 100 points and for each guess deduct 20
                guess_deduction = 20 * (self.row_num - 1)

                round_points = 100 - guess_deduction

                # Add the round points to total points
                self.totalPoints += round_points

                # Add the points to the points window
                strTotalPoints = str(self.totalPoints)
                self.total_points.config(text=strTotalPoints)

                # Convert round points to string for message box
                strRoundPoints = str(round_points)

                # Success message box
                tk.messagebox.showinfo("SUCCESS", 'Congratulations, you have successfully guessed the Secret Phrase and have earned ' + strRoundPoints + ' points!')

            elif (self.row_num > 4):
                tk.messagebox.showwarning("Game Over", 'You are out of guesses! Select "New Word" when you are ready to continue!') # Error dialogue box for Non Unique User  

            self.row_num += 1

        # For the New Word Menu
        def newWord(self):

            # Creates a new random word
            self.randomWord = SecretPhraseFunctions.randomWord()

            # Resets the row number for the Guess Labels
            self.row_num = 1

            # Delets all labels (guesses)
            for widget in self.main_win.winfo_children():
                if isinstance(widget, tk.Label):
                    widget.destroy()

            # Resets all buttons
            changeButton(self, 'A', 'normal', 'cyan', 'true')

        # For the New Word Menu, Check points
        def checkPoints(self):

            # Converts total points to string for message box
            strTotalPoints = str(self.totalPoints)

            tk.messagebox.showwarning("Check Points", 'Your Total Points: ' + strTotalPoints)


        # Changes the button color or disables/enables it
        def changeButton(self, letter, state, bg, reset):

            if (letter == "A" or reset == 'true'):
                self.a_button['state'] = state
                self.a_button['bg'] = bg
                
            if (letter == "B" or reset == 'true'):
                self.b_button['state'] = state
                self.b_button['bg'] = bg

            if (letter == "C" or reset == 'true'):
                self.c_button['state'] = state
                self.c_button['bg'] = bg

            if (letter == "D" or reset == 'true'):
                self.d_button['state'] = state
                self.d_button['bg'] = bg

            if (letter == "E" or reset == 'true'):
                self.e_button['state'] = state
                self.e_button['bg'] = bg

            if (letter == "F" or reset == 'true'):
                self.f_button['state'] = state
                self.f_button['bg'] = bg

            if (letter == "G" or reset == 'true'):
                self.g_button['state'] = state
                self.g_button['bg'] = bg

            if (letter == "H" or reset == 'true'):
                self.h_button['state'] = state
                self.h_button['bg'] = bg

            if (letter == "I" or reset == 'true'):
                self.i_button['state'] = state
                self.i_button['bg'] = bg

            if (letter == "J" or reset == 'true'):
                self.j_button['state'] = state
                self.j_button['bg'] = bg

            if (letter == "K" or reset == 'true'):
                self.k_button['state'] = state
                self.k_button['bg'] = bg

            if (letter == "L" or reset == 'true'):
                self.l_button['state'] = state
                self.l_button['bg'] = bg

            if (letter == "M" or reset == 'true'):
                self.m_button['state'] = state
                self.m_button['bg'] = bg

            if (letter == "N" or reset == 'true'):
                self.n_button['state'] = state
                self.n_button['bg'] = bg

            if (letter == "O" or reset == 'true'):
                self.o_button['state'] = state
                self.o_button['bg'] = bg

            if (letter == "P" or reset == 'true'):
                self.p_button['state'] = state
                self.p_button['bg'] = bg

            if (letter == "Q" or reset == 'true'):
                self.q_button['state'] = state
                self.q_button['bg'] = bg

            if (letter == "R" or reset == 'true'):
                self.r_button['state'] = state
                self.r_button['bg'] = bg

            if (letter == "S" or reset == 'true'):
                self.s_button['state'] = state
                self.s_button['bg'] = bg

            if (letter == "T" or reset == 'true'):
                self.t_button['state'] = state
                self.t_button['bg'] = bg

            if (letter == "U" or reset == 'true'):
                self.u_button['state'] = state
                self.u_button['bg'] = bg

            if (letter == "V" or reset == 'true'):
                self.v_button['state'] = state
                self.v_button['bg'] = bg

            if (letter == "W" or reset == 'true'):
                self.w_button['state'] = state
                self.w_button['bg'] = bg

            if (letter == "X" or reset == 'true'):
                self.x_button['state'] = state
                self.x_button['bg'] = bg

            if (letter == "Y" or reset == 'true'):
                self.y_button['state'] = state
                self.y_button['bg'] = bg

            if (letter == "Z" or reset == 'true'):
                self.z_button['state'] = state
                self.z_button['bg'] = bg

                
        # For the help selection
        def help(self):
            
            tk.messagebox.showwarning("Help", 'Welcome to the Secret Phrase Game, \n\nThe main goal of the game is to guess a 5 letter word in 5 guesses\n\nInput a guess by using the buttons or typing it and press ENTER\n\nEach guess will provide clues to what letters are in the word \n\nIf you need help on the clues, please refer to the color legend') # Error dialogue box for Non Unique User  

        # For the point help selection
        def pointsHelp(self):

            tk.messagebox.showwarning("Points Help", 'Points earned from:\n\n\t\tFirst Guess: 100 \n\t\tSecond Guess: 80 \n\t\tThird Guess: 60 \n\t\tFourth Guess: 40 \n\t\tFifth Guess: 20 \n\t\tGame Over: 0')
            
        # For the Color Legend Selection
        def colorLegend(self):

            SecretPhraseFunctions.colorLegendWindow()
            
        tk.mainloop()

#secretPhraseWindow()