# This is: Guess the player

# In this game there are the names of six football players. The aim is to
# guess the correct name. Good luck!


from random import shuffle
players = ["Rio Ferdinand", "Sergio Ramos", "Andres Iniesta", "Steven Gerrard", "Cristiano Ronaldo", "Alan Shearer"]
Positions = ["Defender", "Midfielder", "Striker"]


player_position = {"Rio Ferdinand": "Defender", "Sergio Ramos": "Defender", "Andres Iniesta": "Midfielder",
                    "Steven Gerrard": "Midfielder", "Cristiano Ronaldo": "Forward", "Alan Shearer": "Forward"}


class Player():
    def __init__(self,name):
        self.name = name


# Introduction:
print("Welcome to Guess the Player!")
print("The possible answers are:")
print("Rio Ferdinand", "Sergio Ramos", "Andres Iniesta", "Steven Gerrard", "Cristiano Ronaldo", "Alan Shearer")


name = raw_input("Name of player: ")
user = Player(name)


# Gameplay:
def randomizing_footballer_names():
    """This function will randomise the list of players and select one player
    name"""
    print("Randomizing the players now")
    shuffle(players)
    print("Try and guess the correct player")
    return players[2]


randomizing_footballer_names()


user_guess = raw_input("What is your guess? ")


guess_state = False



while guess_state != True:
    print("Wrong player. Here is a clue. The player is a: " + player_position[players[2]])
    user_guess = raw_input ("Wrong player. Guess again: ")
    if user_guess == players[2]:
        print ("CORRECT GUESS!")
        guess_state = True
