import random

# Game Introduction
print("\n--- WELCOME TO MINI LUDO GAME ---")
print("Rules: Each player rolls a dice in turns. First to reach 30 wins!\n")

# Get player names
player1 = input("Enter Player 1's Name: ")
player2 = input("Enter Player 2's Name: ")

# Initialize player positions
player1_pos = 0
player2_pos = 0

# Function to simulate dice roll
def roll_dice():
    return random.randint(1, 6)

# Function to save result to a file
def save_result(winner, loser, winner_pos, loser_pos):
    with open("ludo_results.txt", "a") as file:
        file.write(f"\nWinner: {winner} (Position: {winner_pos})\n")
        file.write(f"Loser : {loser} (Position: {loser_pos})\n")
        file.write("-" * 40)

# Main game logic
def ludo_game():
    global player1_pos, player2_pos

    while True:
        # Player 1's turn
        input(f"{player1}, press Enter to roll the dice...")
        dice1 = roll_dice()
        player1_pos += dice1
        print(f"{player1} rolled a {dice1} and is now at position {player1_pos}")

        if player1_pos >= 30:
            print(f"\n🎉 {player1} wins the game! 🎉")
            save_result(player1, player2, player1_pos, player2_pos)
            break

        # Player 2's turn
        input(f"{player2}, press Enter to roll the dice...")
        dice2 = roll_dice()
        player2_pos += dice2
        print(f"{player2} rolled a {dice2} and is now at position {player2_pos}")

        if player2_pos >= 30:
            print(f"\n🎉 {player2} wins the game! 🎉")
            save_result(player2, player1, player2_pos, player1_pos)
            break

# Start the game
ludo_game()
