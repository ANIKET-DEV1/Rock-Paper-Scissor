import random
user_win=0
comp_win=0
options=["rock","paper","scissor"]
while True:
    user_input=input("choose Rock/Paper/Scissor or Quit to exit: ").lower()
    if user_input=="quit":
        break
    if user_input not in options:
        print("🤡 Select among options! ")
        continue
    Random=random.randint(0,2)
    computer_pick=options[Random]
    print(" 💻 Computer picked " + computer_pick + " .")
    if user_input=="rock" and computer_pick=="scissor":
        print("You Won!")
        user_win+=1
    elif user_input=="paper" and computer_pick=="rock":
        print("You Won!")
        user_win+=1
    elif user_input=="scissor" and computer_pick=="paper":
        print("You Won!")
        user_win+=1
    elif user_input==computer_pick:
        print("Draw")
    else :
        print("You lost!")
        comp_win+=1
print(" 😎 You won ",user_win, " times")
print(" 💻 Computer won ", comp_win, " times")
print(".Bye.......")








