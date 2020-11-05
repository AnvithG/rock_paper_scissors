import random
from time import sleep

user_choice = ['Rock', 'Paper', 'Scissors']
computer_choice = random.choice(user_choice)

user = False

while user == False:
    print("Welcome to Anvith's Era of Games: Rock, Paper, Scissors!!")
    print('\nLoading.....Please be patient')
    sleep(2)
    user = input('''
    Which one do you want to choose?
    \nRock : Rock\n
     Paper : Paper\n
    Scissors: Scissors\n
    Stop the game: Stop
    ''')

    if user == computer_choice:
        print('\nLoading.....Please be patient....we are taking your information and giving it to the computer')
        sleep(3)
        print('The computer chose ' + computer_choice)
        print("That's a draw!!")

    elif user == 'Rock':
        if computer_choice == 'Papers':
            print('\nLoading.....Please be patient....we are taking your information and giving it to the computer')
            sleep(3)
            print('The computer chose ' + computer_choice)
            print("Oh no, you have lost in this round !!")
        else:
            print('\nLoading.....Please be patient....we are taking your information and giving it to the computer')
            sleep(3)
            print('The computer chose ' + computer_choice)
            print("Oh yeah, you have won this round !!")

    elif user == 'Scissors':
        if computer_choice == 'Rock':
            print('\nLoading.....Please be patient....we are taking your information and giving it to the computer')
            sleep(3)
            print('The computer chose ' + computer_choice)
            print('Oh no, you have lost this round !!')
        else:
            print('\nLoading.....Please be patient....we are taking your information and giving it to the computer')
            sleep(3)
            print('The computer chose ' + computer_choice)
            print("Oh yeah, you won this round !!")

    elif user == 'Paper':
        if computer_choice == 'Scissors':
            print('\nLoading.....Please be patient....we are taking your information and giving it to the computer')
            sleep(3)
            print('The computer chose ' + computer_choice)
            print('Oh no, you have won this round')
        else:
            print('\nLoading.....Please be patient....we are taking your information and giving it to the computer')
            sleep(3)
            print('The computer chose ' + computer_choice)
            print('Oh yeah, you have one this round ')

    elif user == 'Stop':
        print('\nLoading.....Please be patient....we are taking your information and giving it to the computer')
        sleep(3)
        print('The computer chose ' + computer_choice)
        print("Thanks for playing, Hope you enjoyed this game !!")
        break

    else:
        print("That's not a valid function")
        break

    user = False
