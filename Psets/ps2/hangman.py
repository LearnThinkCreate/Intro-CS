# Problem Set 2, hangman.py
# Name: Warren Hyson
# Collaborators: NA
# Time spent: 

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import os 

WORDLIST_FILENAME = str(os.getcwd()) + '/Psets/ps2/words.txt'

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):

    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # Initializing guessed variable
    # If a letter of secret word is not in letters_guessed the Function will break and Return False
    guessed = True
    for i in secret_word:
      if i not in letters_guessed:
        guessed = False
        break
    return guessed



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # Intiializing list 
    guesses = []
    # if a letter of the secret word is in i, then it's append to the list, otherwise a underscore is appended
    for i in secret_word:
      if i in letters_guessed:
        guesses.append(i)
      else:
        guesses.append("_")
      ## Returning string
    return(''.join(guesses))
  

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    import string
        ## creating variable that has all lowercase letters
    available_letters = list(string.ascii_lowercase)
        ## Removing the guessed letters from available letters
    for i in letters_guessed:
      available_letters.remove(i)
    return ''.join(available_letters)


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    import string
    ## Intitiliazing Variables and list 
    warnings = 0
    guesses = 0
    letters_guessed = []

    print("Welcome to the game Hangman!") ## Game opening Statements
    print("I am thinking of a word that is" , len(secret_word) , "letters long.")
    print("You have 3 warnings left.")
  
    while guesses < 6:
      ##showing number of guesses and available letters remaining
      print("- - - - - - - - - - -")
      print("You have" , 6-guesses , "guesses left.")
      print( "Available letters:", get_available_letters(letters_guessed))
      ## Player input
      guess = str(input("Please guess a letter: " ))
      ## verifying the guess is alpha 
      if str.isalpha(guess):
        ## converting the string to lowercase just in case
        guess = str.lower(guess) 

        ##punishing user if letter is in letters_guessed
        if guess in letters_guessed: 
          if warnings >= 3:
            print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word , letters_guessed))
            guesses += 1
          else: 
            warnings += 1
            print("Oops! You've already guessd that letter. You now have " , 3-warnings , "warnings:")
            print(get_guessed_word(secret_word , letters_guessed))
        else:
          ## appending to letters guessed after verifying it's a unique, lowercase letter
          letters_guessed.append(guess) 

          ## checking if the guess is in the secret word
          if guess in secret_word:
            print("good guess" , get_guessed_word( secret_word , letters_guessed))
          else:
            print("Oops that letter is not in my word:" ,  get_guessed_word(secret_word , letters_guessed))

            ## Punishing the user disprortionatly for choosing vowels 
            if guess in ['a' , 'e' ,'i' , 'o' , 'u']:
              guesses += 2
            else:
              guesses += 1
            ## Ending the game if the 
          if is_word_guessed(secret_word , letters_guessed):
            print("Congragulations,  you won!")
            total_score = (6 - guesses) * (26-len(get_available_letters(letters_guessed)))
            print("Your total score for this game is: " , total_score)
            break
      else:
        if warnings >= 3:
            print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word , letters_guessed))
            guesses += 1
        else: 
          warnings += 1
          print("Oops! You've already guessd that letter. You now have " , 3-warnings , "warnings:")
          print(get_guessed_word(secret_word , letters_guessed))    
     ## Ending the gam if the user runs out of guesses     
    if guesses == 6:
      print("- - - - - - - - - - -")
      print("Sorry, you ran out of guesses. The word is" , secret_word)


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
  
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''

    ## Creating range for loop to iterate over
    index = range(len(my_word)) 
      ## Intializing the same_word variable that will return boolean
    same_word = True
    ## Checking that the length of the two words are the same
    if len(my_word) == len(other_word):
      for i in index:
          ##Skipping letter if it is a underscore
        if my_word[i] == "_":
          pass
        elif my_word[i] != other_word[i]:
          ## breakign and returnging false if a letter doesn't match
          same_word = False
          break
    else:
      ## returning false if the words aren't the same length
      same_word = False
    return same_word


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    matches = []
    for i in wordlist:
      if match_with_gaps(my_word , i):
        matches.append(i)
    if len(matches) == 0:
      print("No matches found")
    print(' '.join(matches))

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    import string
    ## Intitiliazing Variables and list 
    warnings = 0
    guesses = 0
    letters_guessed = []

    print("Welcome to the game Hangman!") ## Game opening Statements
    print("I am thinking of a word that is" , len(secret_word) , "letters long.")
    print("You have 3 warnings left.")
  
    while guesses < 6:
      ##showing number of guesses and available letters remaining
      print("- - - - - - - -")
      print("You have" , 6-guesses , "guesses left.")
      print( "Available letters:", get_available_letters(letters_guessed))
      ## Player input
      guess = str(input("Please guess a letter: " ))

      if guess == "*":
        print("Possible word matches are:")
        my_word = get_guessed_word(secret_word, letters_guessed)
        show_possible_matches(my_word)
      ## verifying the guess is alpha 
      elif str.isalpha(guess):
        ## converting the string to lowercase just in case
        guess = str.lower(guess) 

        ##punishing user if letter is in letters_guessed
        if guess in letters_guessed: 
          if warnings >= 3:
            print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word , letters_guessed))
            guesses += 1
          else: 
            warnings += 1
            print("Oops! You've already guessd that letter. You now have " , 3-warnings , "warnings:")
            print(get_guessed_word(secret_word , letters_guessed))
        else:
          ## appending to letters guessed after verifying it's a unique, lowercase letter
          letters_guessed.append(guess) 

          ## checking if the guess is in the secret word
          if guess in secret_word:
            print("good guess:" , get_guessed_word( secret_word , letters_guessed))
          else:
            print("Oops that letter is not in my word:" ,  get_guessed_word(secret_word , letters_guessed))
            ## Punishing the user disprortionatly for choosing vowels 
            if guess in ['a' , 'e' ,'i' , 'o' , 'u']:
              guesses += 2
            else:
              guesses += 1
            ## Ending the game if the user has guessed the word
          if is_word_guessed(secret_word , letters_guessed):
            print("Congragulations,  you won!")
            total_score = (6 - guesses) * (26-len(get_available_letters(letters_guessed)))
            print("Your total score for this game is: " , total_score)
            break
      else:
        ## Punishing user if input is not a letter
        if warnings >= 3:
            print("Oops! Please enter a letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word , letters_guessed))
            guesses += 1
        else: 
          warnings += 1
          print("Oops! please enter a ltter. You now have " , 3-warnings , "warnings:")
          print(get_guessed_word(secret_word , letters_guessed))    
     ## Ending the gam if the user runs out of guesses   
    if guesses == 6:
      print("- - - - - - - - - - -")
      print("Sorry, you ran out of guesses. The word is" , secret_word)

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


# if __name__ == "__main__":
#     # pass

#     # To test part 2, comment out the pass line above and
#     # uncomment the following two lines.
    
#     secret_word = choose_word(wordlist)
#     #secret_word = 'test'
#     hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)
