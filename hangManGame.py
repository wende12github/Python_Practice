import random as RA

# Predefined list of words
word_list = ["apple", "beautiful", "cherry", "date", "elderberry", "fig", "grape", "selfishness"]

# Track score across games
score = {'wins': 0, 'losses': 0}

fullName = None # Global variable to store user input

def introRules():
    print("\t_________________________________________________________________")
    print("\t|           WELCOME TO HANG MAN WORD GUESSING GAME!              |")
    print("\t|                                                                |")
    print("\t|  ** TRY TO GUESS THE WORD BY SUGGESTING LETTERS.               |")
    print("\t|                                                                |")
    print("\t|  ** YOU HAVE A LIMITED NUMBER OF ATTEMPTS.                     |")
    print("\t|                                                                |")
    print("\t|  ** EACH INCORRECT GUESS WILL REDUCE YOUR REMAINING ATTEMPTS.  |")
    print("\t|                                                                |")
    print("\t|  ** IF YOU STACK, DO NOT WORRY, WE WILL GIVE YOU A HINT        |")
    print("\t_________________________________________________________________\n")

    global fullName
    fullName = input("\nEnter Your Name To start the Game: ").upper()  # Get the player's name and store it

def choose_word():
    return RA.choice(word_list)


def initialize_game():
    word = choose_word()
    guessed_letters = []
    tries_left = 6  # Number of tries/guesses allowed
    return word, guessed_letters, tries_left


# Display the word with correctly guessed letters and underscores for unguessed letters
def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()

# Get a valid letter input from the player
def get_player_input(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Please enter only a single letter.")
        elif not guess.isalpha():
            print("Please enter a letter.")
        elif guess in guessed_letters:
            print("You've already guessed that letter.")
        else:
            return guess

# Choose a random letter from the word that hasn't been guessed yet and return it as a hint
def provide_hint(word, guessed_letters):

    available_letters = [letter for letter in word if letter not in guessed_letters]
    hint = RA.choice(available_letters)
    return hint


# Display the current state of the game
def display_game_status(word, guessed_letters, tries_left):
    print("\nWord:", display_word(word, guessed_letters))
    print("Tries left:", tries_left)
    print("Guessed letters:", guessed_letters)


# Main Function
def play_game():
    
    while True:
        word, guessed_letters, tries_left = initialize_game()
        
        while True:
            display_game_status(word, guessed_letters, tries_left)
            
            global fullName
            if "_" not in display_word(word, guessed_letters):
                print(f"\nCongratulations! {fullName} You guessed the word:", word.upper())
                score['wins'] += 1
                break
            elif tries_left == 0:
                print(f"\nSorry! {fullName} you ran out of tries. The word was:", word.upper())
                score['losses'] += 1
                break

            print("\nChoice from the given option and Enter the Choice as a Word.")
            print("______________________________________________________________\n")
            print("   1. Enter 'GUESS' to guess a letter")
            print("   2. Enter 'HINT' to get a hint")
            print("   3. Enter 'QUIT' to end the game:")

            action = input("\t: ").lower()
            
            if action == 'guess':
                guess = get_player_input(guessed_letters)
                guessed_letters.append(guess)
                if guess not in word:
                    tries_left -= 1
            elif action == 'hint':
                hint = provide_hint(word, guessed_letters)
                print(f"Hint: Try '{hint}'!")
            elif action == 'quit':
                break
            else:
                print("Invalid action. Please enter 'guess', 'hint', or 'quit'.")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThank you for playing Hangman!")
            print(f"Total wins: {score['wins']}, Total losses: {score['losses']}")
            break


# Call Functions here!
introRules()
play_game()

