#Malin Heineking Nemergut
#I certify this code is my work

from graphics import *
from random import *
from time import sleep

class Button:
    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, width, height, label, color):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit','yellow') """ 
        self.xmax, self.xmin = center.getX()+width/2.0, center.getX()-width/2.0
        self.ymax, self.ymin = center.getY()+height/2.0, center.getY()-height/2.0
        p1,p2 = Point(self.xmin, self.ymin), Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill(color)
        self.label = Text(center, label)
        self.win = win
        self.active = False

    def clicked(self, p):
        "Returns true if button active and p is inside"
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def activate(self):
        "Sets this button to 'active'and draws the button."
        if self.active == False:
            self.active = True
            self.rect.draw(self.win)
            self.label.draw(self.win)

    def deactivate(self):
        "Sets this button to 'inactive' and undraws the button."
        if self.active == True:
            self.active = False
            self.rect.undraw()
            self.label.undraw()
          
class Words:
    '''reads a file of words and creates a list of words'''
    def __init__(self,filename):
        infile = open(filename, 'r')
        file_str = infile.read()
        self.word_list = file_str.split()

    def get_word(self):
        '''returns a random word from the list'''
        rand = randint(0, len(self.word_list) -1)

        return self.word_list[rand]

class Guess:
    def __init__(self, word):
        self.word = word
        self.guessed_letters = []
        self.num_guesses = 0
        self.guessed_word = []
        
    def missed(self):
        '''returns the word string that could not be guessed'''
        return self.word
        
    def guess_letter(self, letter):
        '''uncovers letters that match the guess, counts the bad guesses
        and keeps track of the letters guessed. It returns a number, 0,
        if the letter has already been guessed, 1 if the letter is NOT
        in the word and 2 if the letter IS in the word'''
        if letter in self.word:
            self.guessed_letters.append(letter)
            return 2
        elif letter in self.guessed_letters:
            return 0
        else:
            self.num_guesses += 1
            self.guessed_letters.append(letter)
            return 1

    def gameover(self):
        '''returns Boolean, T if word is guessed or the number of guesses
        has exceeded the limit and F otherwise'''
        if self.num_guesses >= 7 or str(self).strip() == self.word:
            if str(self).strip() == self.word:
                print("You win.")
            elif str(self).strip() != self.word:
                print("You lost.")

            return True
            
        elif self.num_guesses < 7:
            return False

    def num_of_guesses(self):
        '''returns a STRING with the number of remaining guesses'''
        return str(8 - self.num_guesses)
        
    def letters_guessed(self):
        '''returns a string, in alphabetical order, of all the letters
        that have been guessed'''
        sorted_letters = sorted(self.guessed_letters)

        return ''.join(sorted_letters)
        
    def   __str__(self):
        '''returns a string with the letters in the word and for each
        unguessed letter separated by spaces'''
        display_word = ''
        for letter in self.word:
            if letter in self.guessed_letters:
                display_word += letter + ' '
            else:
                display_word += '_ '

        return display_word
        
class Noose:
    def __init__(self, win):
        '''creates a Noose object with 7 sections that can be drawn one at a
        time in the win canvas'''
        self.win = win

        base = (Line(Point(100, 450), Point(300, 450)))
        base.draw(win)

        pole = (Line(Point(185, 150), Point(185, 450)))
        pole.draw(win)

        hline = (Line(Point(185, 150), Point(300, 150)))
        hline.draw(win)

        vline = (Line(Point(300, 150), Point(300, 170)))
        vline.draw(win)
        
    def wrong(self, sect_num):
        '''draws another of the 7 sections to the noose platform and/or figure'''
        if sect_num == 7:
            head = Circle(Point(300, 200), 28)
            head.draw(self.win)
        if sect_num == 6:
            body = (Line(Point(300, 228), Point(300, 270)))
            body.draw(self.win)
        if sect_num == 5:
            body2 = (Line(Point(300, 270), Point(300, 295)))
            body2.draw(self.win)
        if sect_num == 4:
            leg1 = (Line(Point(300, 295), Point(270, 330)))
            leg1.draw(self.win)
        if sect_num == 3:
            leg2 = (Line(Point(300, 295), Point(330, 330)))
            leg2.draw(self.win)
        if sect_num == 2:
            arm1 = (Line(Point(300, 240), Point(330, 275)))
            arm1.draw(self.win)
        if sect_num == 1:
            arm2 = (Line(Point(300, 240), Point(270, 275)))
            arm2.draw(self.win)


def play_one_game():    
    win = GraphWin("Hangman Game", 500, 500)
    gallows = Noose(win)
    list_words = Words("wordlist.txt")
    random_word = list_words.get_word()
    buttonA = Button(win, Point(55, 150), 45, 25, "Click", "red")

    guess = Guess(random_word)
    while not guess.gameover():
        # Take in a user's letter
        buttonA.activate()
        # Get a click
        if(buttonA.clicked(Point(56, 151))):
            place = Point(60, 100)
            display = Text(place, str(guess))

            display.draw(win)
            #print(str(guess))
            buttonA.deactivate()
            # Prompt for an input in a popup
            guessed_letter = input("Please guess a letter.")
            # Add it to the guessed letters
            result = guess.guess_letter(guessed_letter)

            # If they already guessed that letter
            if(result == 0):
                print("You have already guessed that letter!")
            
            # If the letter is correct
            elif(result == 2):
                print("Correct")
                # Replace it
            
            # If the letter is wrong
            elif(result == 1):
                # Draw a picture on the noose
                gallows.wrong(int(guess.num_of_guesses()))
            display.undraw()

    # Game over win or lose
    win.close()

def main():
    play_one_game()

main()
