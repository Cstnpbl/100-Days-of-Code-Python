import random
rock='''
_______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper= '''
_______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors= '''
_______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

symbols=[rock,paper,scissors]

your_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors \n" ))
computer_choice=random.randint(0,2)

while your_choice>2 or your_choice<0:
    print("Invalid Number! Please enter a number between 0 and 2")
    your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors \n"))

print("You chose: " + symbols[your_choice])

print("Computer chose: \n " + symbols[computer_choice])


if your_choice == computer_choice:
    print("It's a tie")
elif (your_choice == 0 and computer_choice == 1) or (your_choice == 1 and computer_choice == 2) or (
            your_choice == 2 and computer_choice == 0):
    print("You lose")
else:
    print("You Win!")
