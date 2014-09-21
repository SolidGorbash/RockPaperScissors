#Import random
import random
import getpass

#Defining dictionaries for game elements RPS & RPSLS
paper = { 'wins': 'rock, spock', 'loses': 'scissors, lizard', 'draws': 'paper', }
scissors = { 'wins': 'paper, lizard', 'loses': 'rock, spock', 'draws': 'scissors' }
rock = {'wins': 'scissors, lizard', 'loses': 'paper, spock', 'draws': 'rock'}

#Defining dictionaries for game elements RPSLS
lizard = {'wins':'spock, paper', 'loses': 'scissors, rock', 'draws': 'lizard' }
spock = {'wins':'scissors, rock', 'loses': 'paper, lizard', 'draws': 'spock' }

# List that contains all the game elements RPS
game_element = [paper,scissors,rock]
rpsls_game_element = [paper,scissors,rock,lizard,spock]

# Prompt User with initial instructions
def initial_instruction():
  print("*************************************************************\n" +
        "     - Welcome to SolidGorbash RockPaperScissors Game -      \n" +
        "[-Instructions:                                             ]\n" +
        "[-1 Type RPS to begin a normal match                        ]\n" +
        "[-2 Type RPSLS to begin a RockPaperScissorsLizardSpock Game ]\n" +
        "[-3 Type CUS to build and play your own version of the game ]\n" +
        "*************************************************************"
       )
  #Store user's game choice in a variable
  user_game_choice = input("What type of RockPaperScissors do you want to play? ")
  
  
  while user_game_choice not in "RPS,RPSLS,CUS":
    print("Please only insert RPS or RPSLS or CUS")
    user_game_choice = input("What type of RockPaperScissors do you want to play? ")
    
  return user_game_choice  
    


def players():
  print ("*************************************************************\n" +
         "[-> Type FRIEND to play against your friend                 ]\n" +
         "[-> Type COMPUTER to challenge the machine!                 ]\n" +
         "*************************************************************"
        )
  players = input("-> ").upper()
  
  #Check if input is correct
  while players not in "FRIEND, COMPUTER":
    #If input is not correct prompt the user
    print("Wrong! Type FRIEND or COMPUTER")
    players = input("-> ").upper()
  #Return input if correct value  
  return players  



#Define function to handle the user input choice
def user_choice():
  user_choice = input("Choose one: rock paper or scissors? ").lower()
  while user_choice not in ("rock,paper,scissors"):
    print("Please type in rock, paper or scissors")
    user_choice = input("Choose one: rock paper or scissors? ").lower()
  return user_choice

#Define modified user choice to handle the user input with rpsls game

def rpsls_user_choice():
  user_choice = input("Choose one: rock paper scissors lizard spock? ").lower()
  while user_choice not in ("rock,paper,scissors,lizard,spock"):
    print("Please type in rock, paper, scissors, lizard or spock")
    user_choice = input("Choose one: rock paper scissors lizard spock? ").lower()
  return user_choice

#Define function to handle the friend input choice
def friend_choice(game_element):
  friend_choice = getpass.getpass("Hello my friend stay a while and Play! Choose one: rock paper or scissors? ")
  #Check if input is correct
  while friend_choice not in ("rock,paper,scissors"):
    print("Please type in rock, paper or scissors")
    friend_choice = input("Hello my friend stay a while and Play! Choose one: rock paper or scissors? ")
  if friend_choice == "paper":
    return game_element[0]
  elif friend_choice == "scissors":
    return  game_element[1]
  else:
    return game_element[2]

#Define modified function to handle friend input choice
def rpsls_friend_choice(game_element):
  friend_choice = getpass.getpass("Hello my friend stay a while and Play! Choose one: rock paper scissors lizard or spock? ")
  while friend_choice not in ("rock,paper,scissors,lizard,spock"):
    print("Please type in rock, paper, scissors, lizard or spock")
    friend_choice = input("Hello my friend stay a while and Play! Choose one: rock paper scissors lizard or spock? ")
  if friend_choice == "paper":
    return game_element[0]
  elif friend_choice == "scissors":
    return game_element[1]
  elif friend_choice == "rock":
    return game_element[2]
  elif friend_choice == "lizard":
    return game_element[3]
  else:
    return game_element[4]
  
#Define function randomly choose the computer choice
def computer_choice(game_element):
  computer_choice = random.choice(game_element)
  return computer_choice 
    

def who_wins(user_choice, computer_choice):
  if user_choice in computer_choice['loses']:
    print("\nYou chose {}. Your opponent chose {}".format(user_choice, computer_choice['draws']))
    print("You crush your enemy. You Win!\n")
  elif user_choice in computer_choice['draws']:
    print("\nYou chose {}. Your opponent chose {}".format(user_choice, computer_choice['draws']))
    print("The strength of your oppent matches yours. It's a draw!\n")
  else:
    print("\nYou chose {}. Your opponent chose {}".format(user_choice, computer_choice['draws']))
    print("Your oppenent is awesome. You Lose!\n")  
  
  print("*************************************************************\n" +
        "[-> Type NEW to begin a new match                           ]\n" +
        "[-> Type EXIT...well to exit.                               ]\n" +
        "*************************************************************"
       )
  what_next = input("Make haste! -> ").upper()
  
  #Check if user input is correct
  while what_next not in "NEW,EXIT":
    print("Please type in NEW or EXIT")
    what_next = input("Make haste! -> ").upper()
  
  if what_next == "NEW":
    main()
  else:
    print("\nByeBye! Don't let the door hit you on the way out!")
  
def rps_computer():
  user = user_choice()
  computer = computer_choice(game_element)
  who_wins(user, computer)

def rpsls_computer():
  user = rpsls_user_choice()
  computer = computer_choice(rpsls_game_element)
  who_wins(user, computer)  
  
def rps_friend():
  friend = friend_choice(game_element)
  user = user_choice()
  who_wins(user, friend)  
  
def rpsls_friend():
  friend = rpsls_friend_choice(rpsls_game_element)
  user = rpsls_user_choice()
  who_wins(user,friend)
  
def custom_game():
  
  #Empty dictionaries for the three custom game tokens
  game_token_1 = {'wins': '', 'loses': '', 'draws': ''}
  game_token_2 = {'wins': '', 'loses': '', 'draws': ''}
  game_token_3 = {'wins': '', 'loses': '', 'draws': ''} 
  
  #List of all game tokens
  #Custom Game can only be played against the computer
  custom_game_element = [game_token_1, game_token_2, game_token_3]
  
  #List of token positions 
  position = ["first", "second", "third"]
  count = 0
  
  #Print little bit of instructions to the console
  print( "*************************************************************\n" +
          "[  Think About three game elements. They can be anything!   ]\n" +
          "[     You'll have to decide the win/lose combination        ]\n" +
          "*************************************************************"
        )
  
  #
  for token in custom_game_element:
    token['draws'] = input("What's the name of your {} game-token? ".format(position[count])).lower()
    token['wins'] = input("{} wins against? ".format(token['draws'].title())).lower()
    token['loses'] = input("{} loses with? ".format(token['draws'].title())).lower()
    count = count + 1
  
  user = input("Choose one: {}, {}, {} ? ".format(game_token_1['draws'], game_token_2['draws'], game_token_3['draws'])).lower()
  computer = computer_choice(custom_game_element)
  
  who_wins(user, computer)
  
   
#Define main game loop.  
#This will: 
  #Prompt the user with the initial instructions
  #Ask the user if he wants to play against the computer or a friend
  #Begin the game

def main():
  #Store in a variable the game to play
  game_chosen = initial_instruction().upper()
  #Check if the game_chosen variable is CUS for Custom Game
  #Ignore the player check. You can only play against the computer in a custom game
  if game_chosen == "CUS":
    custom_game()
  #Store in a variable the players
  else:
    players_chosen = players()
    if game_chosen == "RPS" and players_chosen == "COMPUTER":
      rps_computer()
    elif game_chosen == "RPS" and players_chosen == "FRIEND":
      rps_friend()
    elif game_chosen == "RPSLS" and players_chosen == "COMPUTER":
      rpsls_computer()
    elif game_chosen == "RPSLS" and players_chosen == "FRIEND":
      rpsls_friend()
    
    
#Start main game loop    
main()   


