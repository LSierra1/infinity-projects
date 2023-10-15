# ===================================================================================================
# import random


# while True:
    # computerChoice = random.choice(("Rock", "Paper", "Scissors"))
    # userChoice = input(
    #     'Type "End" to end the game\n'
    #     "Rock, paper or scissorz?\n")

    # match computerChoice:
    #     case "Rock":
    #         if userChoice.upper()[0] == "R":
    #             print(f"Computer has choosen {computerChoice}. Draw")
    #         elif userChoice.upper()[0] == "S":
    #             print(f"Computer has choosen {computerChoice}. You lose.")
    #         elif userChoice.upper()[0] == "P":
    #             print(f"Computer has choosen {computerChoice}. You won.")
    #     case "Paper":
    #         if userChoice.upper()[0] == "R":
    #             print(f"Computer has choosen {computerChoice}. You lose.")
    #         elif userChoice.upper()[0] == "P":
    #             print(f"Computer has choosen {computerChoice}. Draw.")
    #         elif userChoice.upper()[0] == "S":
    #             print(f"Computer has choosen {computerChoice}. You won.")
    #     case "Scissors":
    #         if userChoice.upper()[0] == "R":
    #             print(f"Compute has choosen {computerChoice}. You won.")
    #         elif userChoice.upper()[0] == "S":
    #             print(f"Computer has choosen {computerChoice}. Draw.")
    #         elif userChoice.upper()[0] == "P":
    #             print(f"Computer has choosen {computerChoice}. You lose.")
    # if userChoice.upper()[0] == "E":
    #     break
    
# ===================================================================================================

# pedra ganha de tesoura e perde de papel
# papel ganha de pedra e perde de tesoura
# tesoura ganha de papel e perde de pedra
import random

computerChoice = random.choice(("R", "P", "S"))

def game(computerChoice):
    if userChoice.upper()[0] == computerChoice:
        print(f"Computer has choosen {userChoice.capitalize()}. Draw.")
    elif ((userChoice.upper()[0] == "P" and computerChoice == "S") or (userChoice.upper()[0] == "S" and computerChoice == "R") or (userChoice.upper()[0] == "R" and computerChoice == "P")):
        print(f"Computer has choosen {computerChoice}. You lose.")
    else:
        print(f"Computer has choosen {computerChoice}. You won.")

userChoice = input(
        'Type "End" to end the game\n'
        "Rock, paper or scissors?\n"
        )
    
game(computerChoice)