##python number guessing game

"""import random built in function for for random number"""

import random

"""below print statement for welcome into the game"""

print('welcome to number guessing game ')

""" Below line create a function for number guessing game"""

def number_guessing_game():

    """ below two lines create argument or variable  of number and chances """
    
    number = random.randint(1,100)  #return the random no between givan range
    chances = 0

    """ below line print the statement """
    
    print('guess any number in between 1 and 100')

    """ Below line create a condition for chances at max 7 no chances are there for player"""
    
    while chances < 7:

        """below line create a variable guess and asking a dynamically input from user or player"""
        
        guess = int(input())

        """below line create a condition , if that condtion is true then it will print statement
           break statement will come outside of the loop"""

        if guess == number:
            print('Bravo , you won!')
            break
##
##          #""" the below line if condition will be false the elif condtion will be run
##            #if the guess is less than number it will print given no is low"""

        elif (guess < number) :
            print('the number you have given is low i.e', guess)

##            """ the below if condition will be false the elif condtion will be run
##           if the guess is greater than number it will print given no is high"""
        

        elif (guess < number):
             print('the number you have given is high i.e', guess)


            #"""the below line incremented the value of chances + 1 everytime when you run the code"""
            
        chances +=1
        print(chances)

        #""" below line  says no of chanses will be less than 7 or equal to 7 """
    if not chances > 7:

        #""" below line prints when the no chances will be finished"""
        
        print('Sorry you dont have any chance remaning', number)

#""" below line call the function """

number_guessing_game()

#""" Below line ask for user intrest to play or quit"""

interest=input("\n Do you want to play again: Y/N \n")

#"""Below line is condition , if user puts y then the function will run and game will start"""
while interest =='y' or interest=='Y':
    number_guessing_game()

    #""""below line asking a user input in dynamically if yes then function will run,
         #if NO then it will print last line"""
    
    interest = input("Do you want to play again: Y/N \n")

    #""""below line print statment"""

print("THANKS FOR PLAYING!")






