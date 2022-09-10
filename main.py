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
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors? \n").lower())
if user_choice >= 3 or user_choice < 0:
    print("You entered an invalid number, You lose")
else:
  choices = ["rock", "paper", "scissors"]
  user_answer = choices[user_choice]
  computer_choice = random.choice(choices)


  
  if user_answer == "rock" and computer_choice == "scissors":
      print(f"{rock}\n Computer choose: \n {scissors} \n You Win")
  elif computer_choice == "rock" and user_answer == "scissors":
      print(f"{scissors}\n Computer choose: \n {rock} \n You Lose")
  elif user_answer == "scissors" and computer_choice == "paper":
      print(f"{scissors}\n Computer choose: \n {paper} \n You Win")
  elif computer_choice == "scissors" and user_answer == "paper":
      print(f"{paper}\n Computer choose: \n {scissors} \n You Lose")
  elif user_answer == "paper" and computer_choice == "rock":
      print(f"{paper}\n Computer choose: \n {rock} \n You Win")
  elif computer_choice == "paper" and user_answer == "rock":
      print(f"{rock}\n Computer choose: \n {paper} \n You Lose")
  elif user_answer == "scissors" and computer_choice == "scissors":
      print(f"{scissors}\n Computer choose: \n {scissors} \n Draw")
  elif user_answer == "paper" and computer_choice == "paper":
      print(f"{paper}\n Computer choose \n {paper} \n Draw")
  elif user_answer == "rock" and computer_choice == "rock":
      print(f"{rock}\n Computer choose: \n {rock} \n Draw")
