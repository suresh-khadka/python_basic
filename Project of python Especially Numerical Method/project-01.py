def selection():
    print("press button")
    print("for snake -> 1")
    print("for water -> 2")
    print("for gun -> 3")
    print("")
    a=input("enter a choice : ")
    if(a=="1"):
        print("congrats,you select snake")
    elif(a=="2"):
        print("congrats,you select water")
    elif(a=="3"):
        print("congrats,you select gun")
    else:
        print("invalid choice, try again!!")
        print("")
        selection()

    return a
    
while(1):
    inpt=selection()
    import random
    choices = ["snake", "water", "gun"]
    computer_choice = random.choice(choices)
    print("")
    print("Computer selected:", computer_choice)
    print("")


    if(computer_choice=="snake"):
        if(inpt=="1"):
            print("game draw!!, try again")

        if(inpt=="2"):
            print("snake drink water........")
            print("you loose")

        if(inpt=="3"):
            print("The gun shoots and kills the snake........")
            print("congrulation!! you won.")


    if(computer_choice=="water"):
        if(inpt=="2"):
            print("game draw!!, try again")

        if(inpt=="1"):
            print("snake drink water........")
            print("congrulation!! you won.")

        if(inpt=="3"):
            print("The gun is doused by the water")
            print("you loose")


    if(computer_choice=="gun"):
        if(inpt=="3"):
            print("game draw!!, try again")

        if(inpt=="2"):
            print("The gun is doused by the water")
            print("congrulation!! you won.")

        if(inpt=="1"):
            print("The gun shoots and kills the snake........")
            print("you loose")

    print("")
    print("if you want to terminate a game press 00")
    x=input("if not press any other key : ")
    print("")
    if(x=="00"):
        print("Game over!!")
        break



