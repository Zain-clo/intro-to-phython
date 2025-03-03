import random

# Function to start the game
def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # Set a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Initialize number of attempts
    attempts = 0
    
    # Loop until the player guesses correctly
    while True:
        # Ask the player to guess a number
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
        
        # Check the guess and provide feedback
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break

# Call the function to start the game
number_guessing_game()
