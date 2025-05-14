# 1. Import the random module.
import random 

play_again = True
while play_again:
    print ("wlcome to the rock paper scissors!")
    print ()
    # 2. Generate a random number between 1 and 3 and set it equal to a variable called computer (hint: use the randint() function) 
    reptar= random.randint(1,3)

    # 3. Using input, get the user's choice where 1 is rock, 2, paper, and 3 is scissors. Store the user's input in a variable called user.
    choice = int(input ("Enter \n 1 for rock \n 2 for papaer \n 3 for scissors: "))

    # 4. Use if-statements to determine the winner of the game and print the result.
    # If the computer and the user choose the same option, print "It's a tie!". If the computer wins, print "Computer wins!". If the user wins, print "You win!". 

    # paper (2) beats rock (1)
    # rock (1) beats scissors (3)
    # scissors (3) beats paper (2)

    print ("reptar chose",reptar)
    if reptar == choice:
        print("It's a tie 😂 ")
    elif reptar == 2 and choice == 1:
        print("Bro its an AI do better")
    elif reptar == 1 and choice ==3:
         print("Bro you are two away how 🤣")
    elif reptar ==3 and choice ==2:
        print("you lost bro its an AI come on 😐")
    elif choice >3 or choice <1:
        print("You cant do that 😐")
    else:
        print("You beat an AI good job 👍")


    # Ask the user if they want to continue
        user_input = input("Do you want to play again? (yes/no): ").lower()

        if user_input == "no":
            # the game should stop!
            play_again = False

print()
print("Thanks come again")