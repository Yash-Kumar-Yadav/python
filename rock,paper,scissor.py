import random
l=["rock","paper","scissor"]
while True:
    ucount=0
    ccount=0
    user_count=int(input('''
    GAME START
    PRESS:-
    1. TO PLAY
    2. TO EXIT
    
    '''))
    if user_count==1:
        for a in range(1,6):
            UserInput=int(input('''
            1 ROCK
            2 PAPER
            3 SCISSOR
            '''))
            if UserInput==1:
                user_choice="rock"
            elif UserInput==2:
                user_choice = "paper"
            elif UserInput==3:
                user_choice = "scissor"
            computer_choice=random.choice(l)
            if computer_choice==user_choice:
                print("COMPUTER VALUE",computer_choice)
                print("USER VALUE",user_choice)
                print("GAME DRAW")
                ucount=ucount+1
                ccount=ccount+1
            elif (user_choice=="rock" and computer_choice=="scissor") or (user_choice=="paper" and computer_choice=="rock") or ( user_choice=="scissor" and computer_choice=="paper"):
                print("COMPUTER VALUE", computer_choice)
                print("USER VALUE", user_choice)
                print("YOU WIN")
                ucount = ucount + 1
            else:
                print("COMPUTER VALUE", computer_choice)
                print("USER VALUE", user_choice)
                print("COMPUTER WIN")
                ccount = ccount + 1

        if ucount==ccount:
            print("--------****--------")
            print("\nFINAL GAME GAME IS DRAW")
            print("USER COUNT",ucount)
            print("COMPUTER COUNT",ccount)
        elif ucount>ccount:
            print("--------****--------")
            print("\nFINAL GAME USER WIN")
            print("USER COUNT", ucount)
            print("COMPUTER COUNT", ccount)
        else:
            print("--------****--------")
            print("\nFINAL GAME COMPUTER WIN")
            print("USER COUNT", ucount)
            print("COMPUTER COUNT", ccount)

    else:
        break