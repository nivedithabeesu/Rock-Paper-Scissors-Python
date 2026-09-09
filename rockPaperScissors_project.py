import random
Rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images=[Rock,Paper,Scissors]
user_choice=int(input("Enter your Choice: Type 0 for Rock,1 for Paper,2 for Scissor"))
if user_choice>=3 or user_choice<0:
    print("you entered invalid number,you lose")
else:
    print(game_images[user_choice])
    computer_choice=random.randint(0,2)
    print("computer chose:")
    print(game_images[computer_choice])
    if computer_choice==user_choice:
        print("it's draw")
    elif computer_choice==0 and user_choice==2:
        print("you lose")
    elif user_choice==0 and computer_choice==2:
        print("you win")
    elif computer_choice>user_choice:
        print("you lose")
    elif user_choice>computer_choice:
        print("you win")