import random
import tkinter as tk

def randomWord():

    try:
        word_file = open('wordlist.txt', 'r') #open file

        # Gets the amount of Words in File
        wordFileSize = lineCounter() - 1

        # Returns random number
        randomWordLine = random.randint (0, wordFileSize)

        # Line Count Variable
        lineCount = 0

        # Random Word Variable
        randomWord = ''

        # Read file
        for line_of_text in word_file:

            # Gets the word on the random number's line
            if (lineCount == randomWordLine):
                randomWord = line_of_text.strip()

            lineCount += 1


        word_file.close #close file
        
        return randomWord

    
    except IOError:
        print('No file exists.')

def lineCounter():

    try:
        word_file = open('wordlist.txt', 'r') #open file

        # Line Count Variable
        lineCount = 0

        # Counts the number of lines
        for line_of_text in word_file:
            lineCount += 1

        word_file.close #close file

        return lineCount


    except IOError:
        print('No file exists.')

class colorLegendWindow():
    def __init__ (self):

        # Standard window configuration
        self.color_win = tk.Tk()
        self.color_win.title("Color Legend")
        self.color_win.minsize(width=850, height=400)
        self.color_win.resizable(height = False, width = False)

        # Create rows and Columns
        for r in range(3):
            self.color_win.rowconfigure(r, minsize = 75)

        for c in range(14):
            self.color_win.columnconfigure(c, minsize = 15)

        # Displays the example word
        self.word_char = tk.Label(self.color_win, text = "R", bg = "red", padx=12, pady=6, font=("Helvetica Bold", 24))

        self.word_char.grid(row=1, column=5)

        self.word_char = tk.Label(self.color_win, text = "O", bg = "green", padx=12, pady=6, font=("Helvetica Bold", 24))

        self.word_char.grid(row=1, column=7)

        self.word_char = tk.Label(self.color_win, text = "U", bg = "green", padx=12, pady=6, font=("Helvetica Bold", 24))

        self.word_char.grid(row=1, column=9)

        self.word_char = tk.Label(self.color_win, text = "N", bg = "orange", padx=12, pady=6, font=("Helvetica Bold", 24))

        self.word_char.grid(row=1, column=11)

        self.word_char = tk.Label(self.color_win, text = "D", bg = "red", padx=12, pady=6, font=("Helvetica Bold", 24))

        self.word_char.grid(row=1, column=13)

        # Create the explanation label
        self.info = tk.Label(self.color_win, text = "Red means the letter is not in the word;\n\nOrange means the letter is in the word but not in the right position;\n\nGreen means the letter is in the word and in the correct position", padx=12, pady=6, font=("Helvetica Bold", 9))

        self.info.grid(row=2, column=14)


        tk.mainloop()