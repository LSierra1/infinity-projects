import random

gameChoice = ["Rock", "Paper", "Scissors"]

while True:
    computerChoice = random.choice(gameChoice)
    userChoice = input(
        'Type "End" to end the game\n'
        "Rock, paper or scissorz?\n")

    match computerChoice:
        case "Rock":
            if userChoice.upper()[0] == "R":
                print(f"Computer has choosen {computerChoice}. Draw")
            elif userChoice.upper()[0] == "S":
                print(f"Computer has choosen {computerChoice}. You lose.")
            elif userChoice.upper()[0] == "P":
                print(f"Computer has choosen {computerChoice}. You won.")
        case "Paper":
            if userChoice.upper()[0] == "R":
                print(f"Computer has choosen {computerChoice}. You lose.")
            elif userChoice.upper()[0] == "P":
                print(f"Computer has choosen {computerChoice}. Draw.")
            elif userChoice.upper()[0] == "S":
                print(f"Computer has choosen {computerChoice}. You won.")
        case "Scissors":
            if userChoice.upper()[0] == "R":
                print(f"Compute has choosen {computerChoice}. You won.")
            elif userChoice.upper()[0] == "S":
                print(f"Computer has choosen {computerChoice}. Draw.")
            elif userChoice.upper()[0] == "P":
                print(f"Computer has choosen {computerChoice}. You lose.")
    if userChoice.upper()[0] == "E":
        break