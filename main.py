import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_image = [rock, paper, scissors]
type = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    ))
print(game_image[type])

computer_guess = print("Computer chose: \n")

computer_guess = random.randint(0, 2)
print(game_image[computer_guess])

if type >= 3 or type < 0:
    print("You typed an invalid number, you lose!")
elif type == 0 and computer_guess == 2:
    print("You win!")
elif type == 0 and computer_guess == 2:
    print("You lose!")
elif type == computer_guess:
    print("It's a draw!")
elif type > computer_guess:
    print("You win!")
elif computer_guess > type:
    print("You lose!")
