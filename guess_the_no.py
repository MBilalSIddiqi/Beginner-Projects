import random

def guess_the_number():
    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)
    print("\n🎯 Guess the number between 1 and 100!")

    attempts = 0

    while True:
        try:
            ask_number = int(input("Enter your guess: "))
            attempts += 1

            # Validate the input is within range
            if ask_number < 1 or ask_number > 100:
                print("⚠️ Please enter a number between 1 and 100.")
                continue

            difference = abs(random_number - ask_number)

            if ask_number == random_number:
                print(f"🎉 YOU GUESSED IT in {attempts} attempts!")
                break

            elif ask_number < random_number:
                if difference > 30:
                    print("📉 Too LOW!")
                elif difference > 20:
                    print("⬇️ Lower!")
                elif difference > 5:
                    print("🔽 Low!")
                else:
                    print("🔥 Very Close (Low)")

            else:  # ask_number > random_number
                if difference > 30:
                    print("📈 Too HIGH!")
                elif difference > 20:
                    print("⬆️ Higher!")
                elif difference > 5:
                    print("🔼 High!")
                else:
                    print("🔥 Very Close (High)")

        except ValueError:
            print("❌ Please enter a valid number.")

# Wrap the game in a loop to allow replay
def main():
    while True:
        guess_the_number()
        play_again = input("Play again? (y/n): ").lower()
        if play_again != 'y':
            print("👋 Thanks for playing!")
            break

# Start the game
main()
