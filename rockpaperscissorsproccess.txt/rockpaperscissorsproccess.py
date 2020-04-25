'''
Created on Apr 25, 2020

@author: ITAUser
'''
Objective:

This program will allow the user to play rock, paper, scissors against the computer

To-Do:

We will create code that checks who won each round

We will create code that takes input(choices) from the user

We will create code that takes ‘input’(choices) from the computer 

We will create code that checks if the user wants to quit, or if the user doesn’t enter one of the options(rock, paper, or scissors)

We will loop each round of the game

We will add statements at the end and the beginning that welcome and thank the user playing

We will loop the whole game, so that the user can keep playing until they choose to quit



PSEUDOCODE

#set variable keepPlaying to true

#while keepPlaying is true:



    #print statement welcoming players to the game

    #print statement stating the rules (best 2 out of 3 Press 'q' to quit)

    

    #make a key that assigns a number to each choice for the computer 

    #(rock is 1, scissors is 2, paper is 3)

    

    #import the random function 

    

    #set computers score to 0

    #set players score to 0

    

    #while players score is less than 2 and the computers score is less than 2:

    

    

    #computers choice = random number between 1 and 3

    #players choice = input (ask player to select rock, paper, or scissors)

    

    #if player inputs 'q' or 'Q':

    #   set keepPlaying to False

    #   stop the loop 

    

    #else if (player chooses rock and computer chooses rock) or

    #(player chooses paper and computer chooses paper) or

    #(player chooses scissors and computer chooses scissors):

    #   print out DRAW

    #   print out players score and computers score

    

    

    #else if (player inputs rock and computer inputs scissors) or

    #(player inputs scissors and computer inputs paper) or

    #(player inputs paper and computer inputs rock):

    #   add one to players score

    #   print out players score and computers score

    

    

    #else if (player inputs rock and computer inputs paper) or

    #(player inputs scissors and computer inputs rock) or

    #(player inputs paper and computer inputs scissors):

    #   add one to computers score

    #   print out players score and computers score

    

    #else:

    #   tell the user their input was not valid

    

    

#print statement thanking players for playing

#if players score is 2:

#   print statement letting the player know they won

#if computers score is 2:

#   print statement letting the player know the computer won

#print out players score and computers score