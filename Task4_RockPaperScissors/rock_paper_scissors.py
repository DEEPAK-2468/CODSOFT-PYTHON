import random as r

menu=["Rock","Paper","Scissors"]
user_score,bot_score=0,0

choice="y"
while (choice=="y"):
    try:
        print("\nMenu:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")

        user_choice=int(input("Enter your choice: "))
        if (user_choice not in [1,2,3]):
            print("Invalid Choice.")
            continue

        bot_choice=r.randint(0,2)
        user_choice-=1
        print(f"You: {menu[user_choice]} | Computer: {menu[bot_choice]}")
        if (bot_choice==user_choice):
            print("It's a Tie.")
        elif ((bot_choice==0 and user_choice==1) or
              (bot_choice==1 and user_choice==2) or
              (bot_choice==2 and user_choice==0)):
            user_score+=1
            print("You Win.")
        else:
            bot_score+=1
            print("Computer Wins.")

        choice=input("\nPlay Again (y/n): ").lower()

    except ValueError:
        print("Enter a Valid Number.")

print(f"\nYour Score: {user_score}")
print(f"Computer Score: {bot_score}")
print("Game Over.")