import random

# Function to get the computer's choice
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

# Main function to run the game
def main():
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        user_choice = input("Choose Rock, Paper, or Scissors (or type 'exit' to quit): ").lower()

        if user_choice == 'exit':
            print("Thanks for playing!")
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

if __name__ == "__main__":
    main()