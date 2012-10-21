# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random

    # fill in your code below
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!

def number_to_name(number):
    if number == 0:
        number="rock"
        return number
    elif number == 1:
        number="Spock"
        return number
    elif number == 2:
        number="paper"
        return number
    elif number == 3:
        number="lizard"
        return number
    else:
        number="scissor"
        return number
    
    
    
    # fill in your code below

    # convert name to number using if/elif/else
    # don't forget to return the result!

    
def name_to_number(name):
    if name=="rock":
        name=0
        return name
    elif name=="Spock":
        name=1
        return name
    elif name=="paper":
        name=2
        return name
    elif name=="lizard":
        name=3
        return name
    else :
        name=4
        return name

    




def rpsls(name): 
    # convert name to player_number using name_to_number
    player_number = name_to_number(name)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    

    # compute difference of player_number and comp_number modulo five
    num=(comp_number - player_number)% 5
    
    	# use if/elif/else to determine winner
    if num == 1 or num == 2:
        num = comp_number
    elif num == 3 or num == 4:
        num = player_number
    else:
        num=name
        
        
   
    

    # convert comp_number to name using number_to_name
    computer_guess = number_to_name(comp_number)
    player_guess = number_to_name(player_number)
    
    name = number_to_name(num)
    

    if name==player_guess:
        name = "Player Wins!"
        
    elif name==computer_guess:
        name = "Computer Wins!"
    else:
        name="Player and computer tie!"
    # print results

    print("")
    print("Player chooses " + player_guess)
    print("Computer chooses " + computer_guess)
    print(name)


    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


