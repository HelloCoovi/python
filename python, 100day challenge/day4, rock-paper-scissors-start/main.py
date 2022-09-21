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

import random

player = int(input("What do you choose? Type 0 for Rock,  for Paper or 2 for Scissors."))

computer = random.randint(0,2)

hand = [rock, paper ,scissors]

if player > 2 or player < 0:
    print("You type wrong number and You loss")
else:
    print(f"You:\n{hand[player]}")
    print(f"computer:\n{hand[computer]}")
    
    if player == computer:
        print("DRAW!")
    
    elif player == 0 and computer == 1:
        print("You loss")
    elif player == 0 and computer == 2:
        print("You win")
    elif player == 1 and computer == 0:
        print("You win")
    elif player == 1 and computer == 2:
        print("You loss")
    elif player == 2 and computer == 0:
        print("You loss")
    elif player == 2 and computer == 1:
        print("You win")
