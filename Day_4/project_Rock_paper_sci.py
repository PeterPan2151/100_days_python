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
moves = [rock, paper, scissors]
moves_names = ['Rock', 'Paper', 'Scissors']
print("Let's play rock, Paper, Scissors!")
computer_choice = random.randint(0, 2)
player_choice = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
print(f"Player Choice: {moves_names[player_choice]}")
print(moves[player_choice])
print("VS")
print(f"Computer Choice: {moves_names[computer_choice]}")
print(moves[computer_choice])

if player_choice == computer_choice:
    print("It's a Tie.")
elif player_choice == 0 and computer_choice == 2:
    print("You win")
elif player_choice == 2 and computer_choice == 0:
    print("You Loose")
elif player_choice > computer_choice:
    print("You Won.")
elif player_choice < computer_choice:
    print("You Loose.")
