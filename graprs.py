import random
import sys

player_points = 0
computer_points = 0

while(True):
        print("===========Prepare to battle!!!==============")
        user_hand = input("Choose paper, rock, scissors or exit to quit the program: ").lower()
        possibilities = ["paper", "rock", "scissors", "exit"]
        computer_hand = random.choice(possibilities)
        if user_hand not in possibilities:
                print("FOLLOW THE RULES STUPID!!! Paper, rock or scissors only!")

        

        if user_hand == computer_hand:
                print("That's draw! No points!")

        elif user_hand == "rock":
                if computer_hand == "scissors":
                        print("Computer choice:"+ computer_hand +". You win! Damn You!")
                        player_points += 1
                else:
                        print("Computer choose: " + computer_hand + "! You loose!!!")
                        computer_points += 1

        elif user_hand == "scissors":
                if  computer_hand == "paper":
                        print("Computer choose: " + computer_hand + ". You lucky Bastard!")
                        player_points += 1
                else:
                        print("Ha! You loose again! Computer choose: " + computer_hand + "!")
                        computer_points += 1
        elif user_hand == "paper":
                if computer_hand == "rock":
                        print("You win! Computer's choice:" + computer_hand + ".")
                        player_points += 1
                else:
                        print("Looser!!! Comp choose:" + computer_hand + "!")
                        computer_points += 1

        elif user_hand == "exit":
                print("Run Chicken, run!!!")
                sys.exit()

        print("Computer points: ",computer_points,"\n" "Player points: ", player_points,)
        if computer_points > player_points:
                print("This time Computer win!")
        elif computer_points < player_points:
                print("Player wins!!!")
        
        
