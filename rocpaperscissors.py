'''
Created on Apr 25, 2020

@author: ITAUser
'''

import random



#set variable keepPlaying to true

keepPlaying = True 

#while keepPlaying is true:

while(keepPlaying == True):

    #print statement welcoming players to the game

    print("Welcome Players")

    #print statement stating the rules (best 2 out of 3 Press 'q' to quit)

    print("Best 2 Out of 3")

    print("Press 'q' to quit")

    #make a key that assigns a number to each choice for the computer 

    #(rock is 1, scissors is 2, paper is 3)

    

    #import the random function 

    

    #set computers score to 0

    #set players score to 0

    player = 0

    computer = 0

    

    #while players score is less than 2 and the computers score is less than 2:

    while (player < 2 and computer < 2):

    

    #computers choice = random number between 1 and 3

        computerChoice = random.randint (1,3)

    #players choice = input (ask player to select rock, paper, or scissors)

    playerChoice = input ("Please choose (Rock, Paper, or Scissors):")

    playerChoice = playerChoice.lower()

    #if player inputs 'q' or 'Q':

    if(playerChoice == "q"):

    #   set keepPlaying to False

        keepPlaying = False

    #   stop the loop 

        break

    #else if (player chooses rock and computer chooses rock) or

    elif ((playerChoice == "rock" and computerChoice == "rock") or (playerChoice == "paper" and computerChoice == "paper")

           or (playerChoice == "scissors" and computerChoice == "scissors")):

    

        print("DRAW")

        print("Player Score = " + player.__str__() + "Computer Score = " + computer.__str__())

    

    #else if (player inputs rock and computer inputs scissors) or

    elif((playerChoice == "rock" and computerChoice == "scissors") or (playerChoice == "scissors" and computerChoice == "paper") or 

         (playerChoice == "paper" and computerChoice == "rock")):

    #   add one to players score

        player = player + 1

        print("Round Win")

        print("Player Score = " + player.__str__() + "Computer Score = " + computer.__str__())

    

    #else if (player inputs rock and computer inputs paper) or

    elif((playerChoice == "rock" and computerChoice == "paper") or (playerChoice == "scissors" and computerChoice == "rock") or

          (playerChoice == "paper" and computerChoice == "scissors")):

    #   add one to computers score

        computer = computer + 1

        

        print("Player Score = " + player.__str__() + "Computer Score = " + computer.__str__())

else:

    print("Your input is not valid")

    print("Thank you for playing")

    if(player == 2):

        print("You won!")

    if(computer == 2):

        print("The computer won")

        print("Player Score = " + player.__str__() + "Computer Score = " + computer.__str__())