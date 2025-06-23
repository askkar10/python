import random
ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'

def get_computer_rps():
    random_int = random.randint(1,3)
    if random_int == 1:
        return ROCK
    elif random_int == 2:
        return PAPER
    else:
        return SCISSORS

def get_user_rps():
    selection = ''
    while selection != ROCK and selection != PAPER and selection != SCISSORS:
        selection = input('Enter rock, paper, or scissors: ')
    return selection

def result_check(user,computer):
    if user == computer:
        print('TIE')
    elif (user == PAPER and computer == ROCK)    or \
         (user == ROCK and computer == SCISSORS) or \
         (user == SCISSORS and computer == PAPER):
        print('USER WON')
    else:
        print('COMPUTER WON')
    print('Computer choice: ' + computer)

def main():
    user_choice = get_user_rps()
    computer_choice = get_computer_rps()
    result_check(user_choice,computer_choice)

main()
