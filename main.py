import random

def get_choice():
    player_choice = input("Enter your choice (rock/paper/scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {'player':player_choice, 'computer': computer_choice}
    return choices

def check_win(player, computer):
    print ( f'you chose {player}, computer chose {computer}')
    if player == computer:
        return "Its a Draw"
    elif player == "rock":
        if computer == "paper":
            return "Computer Wins"
        else:
            return "Player Wins"
    elif player == "paper":
        if computer == "scissors":
            return "Computer Wins"
        else:
            return "Player Wins"
    elif player == "scissors":  
        if computer == "rock":
            return "Computer Wins"
        else:
            return "Player Wins"
        
choices = get_choice()
winner = check_win(choices['player'], choices['computer'])
print(winner)
       

