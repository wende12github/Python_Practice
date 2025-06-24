import random as ra

def introRules():
    print("\n\t___________________________________________________\n")
    print("\t\tEach Player choose one of the three options! ")
    print('\t\t  The Winner is determined by the choices! ')
    print("\t\t\tRock Crushes Scissors,\n\t\t\tScissors Cuts Paper and\n\t\t\tPaper Covers Rock.")
    print("\t___________________________________________________\n")
    


def user_choices():

    print("\t*                                       *")
    print("\t\tRock Paper and Scissors Game")
    print("\t*                                       *")
    print("**************************************************")
    print("\t1. Rock\n\t2. Paper\n\t3. Scissors \n\t4. Exit")
    print("**************************************************")
    while True:
        choice = input("\nPlease, enter Your Choice (rock, paper, scissors): ")

        if choice == "rock" or choice == "paper" or choice == "scissors":
           return choice
        else:
           print("Invalid Choice! Please, Choise from (rock, paper, scissors).")


def computer_choices():
    return ra.choice(['rock', 'paper', 'scissors'])


def determine_winner(user_choice, computer_choice):

    if user_choice == computer_choice:
        return 'Tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or\
        (user_choice == 'scissors' and computer_choice == 'paper') or (user_choice == 'paper' and computer_choice == 'rock'):
        return "User"
    else:
        return 'Çomputer'
    

def display_results(user_choice, computer_choice, winner):
    print(f"\n\tYour Choice: {user_choice}")
    print(f"\tComputer's Choice: {computer_choice}")
    if winner == 'Tie':
        print(f"It's a Tie! {name}== Computer")
    else :
        print(f"Hello {name}, {winner} You Win!")

introRules()
name = input("If You agree with this Rule Please, enter your Name and Start the Game: ").upper()

with open("gameData.txt", 'w') as file:
    while True:
    
        user_choice = user_choices() #assign to user_choice the function
        computer_choice = computer_choices()

        winner = determine_winner(user_choice, computer_choice)

        display_results(user_choice, computer_choice, winner)

        play_again = input("Do you want to Play Again? if Yes please, press yes else no: ").lower()

        if play_again != 'yes':
            print("Thank You Truly For playing. Goodbye! ")
            break