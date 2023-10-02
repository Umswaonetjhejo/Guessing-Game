# Import the random module to generate a secret number
import random

# Generate a random secret number between 0 and 10 (inclusive)
secret_number = random.randint(0, 10)

# Initialize variables to keep track of guesses and guess limits
guess_count = 0
guess_limit = 3

# Display instructions and game information to the user
print("THIS IS A GUESSING GAME")
print("Guess a number between 0 and 10.")
print("If your number matches the Game Secret Number, you WIN.")
print("If not, you LOSE")

# Start a loop to allow the user to make up to three guesses
while guess_count < guess_limit:
    # Prompt the user to enter a guess as an integer
    guess = int(input("Guess a Number: "))
    
    # Increment the guess count
    guess_count += 1
    
    # Check if the guess matches the secret number
    if guess == secret_number:
        print("Congratulations! You won!")
        break  # Exit the loop if the guess is correct

# If the loop completes without a correct guess, inform the user that they lost
else:
    print("Sorry, you lost! The secret number was:", secret_number)

