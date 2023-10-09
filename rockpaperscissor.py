import random

# Function to get user's choice
def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

# Function to get computer's choice
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Function to play a round
def play_round():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose {user_choice}")
    print(f"Computer chose {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)
    return result

# Function to display the final score
def display_score(user_score, computer_score):
    print(f"Final Score: You {user_score}, Computer {computer_score}")

# Main game loop
def main():
    user_score = 0
    computer_score = 0
    while True:
        print("\nRock-Paper-Scissors Game")
        result = play_round()
        if "You win" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1
        display_score(user_score, computer_score)
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
