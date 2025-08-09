import random

def choices():
    print("Choices:")
    print("1: Rock 🪨")
    print("2: Paper 📜")
    print("3: Scissors ✂️")
    print("4: Lizard 🦎")
    print("5: Spock 🖖")

def computerch():
    choices = ["Rock 🪨", "Paper 📜", "Scissors ✂️", "Lizard 🦎", "Spock 🖖"]
    return random.choice(choices)

def determine_winner(player, computer):
    outcomes = {
        ("Rock 🪨", "Scissors ✂️"): "Rock 🪨 crushes Scissors ✂️! You win!",
        ("Rock 🪨", "Lizard 🦎"): "Rock 🪨 crushes Lizard 🦎! You win!",
        ("Paper 📜", "Rock 🪨"): "Paper 📜 covers Rock 🪨! You win!",
        ("Paper 📜", "Spock 🖖"): "Paper 📜 disproves Spock 🖖! You win!",
        ("Scissors ✂️", "Paper 📜"): "Scissors ✂️ cut Paper 📜! You win!",
        ("Scissors ✂️", "Lizard 🦎"): "Scissors ✂️ decapitate Lizard 🦎! You win!",
        ("Lizard 🦎", "Paper 📜"): "Lizard 🦎 eats Paper 📜! You win!",
        ("Lizard 🦎", "Spock 🖖"): "Lizard 🦎 poisons Spock 🖖! You win!",
        ("Spock 🖖", "Rock 🪨"): "Spock 🖖 smashes Rock 🪨! You win!",
        ("Spock 🖖", "Scissors ✂️"): "Spock 🖖 smashes Scissors ✂️! You win!",
    }
    
    if player == computer:
        return "Tie."
    
    if (player, computer) in outcomes:
        return outcomes[(player, computer)]
    return f"Dayumm! {computer} beats {player}. Computer wins!"

def play():
    print("Welcome to Rock, Paper, Scissors, Lizard, Spock! ")
    
    choices()
    player = int(input("Enter your choice (1-5): "))
    
    if player == 1:
        player = "Rock 🪨"
    elif player == 2:
        player = "Paper 📜"
    elif player == 3:
        player = "Scissors ✂️"
    elif player == 4:
        player = "Lizard 🦎"
    elif player == 5:
        player = "Spock 🖖"
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
        return

    computer = computerch()
    print(f"\nYou chose: {player}")
    print(f"The computer chose: {computer}\n")
    
    result = determine_winner(player, computer)
    print(result)

while True:
    play()
    play_again = input("\nEnter any key to play again\nEnter 0 to quit: ").lower()
    if play_again == '0':
        print("Thanks for playing. Bye 👋")
        break
