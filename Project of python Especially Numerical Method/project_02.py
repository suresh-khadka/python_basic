# this is a game which can play two player. both player guess number from 10 t0 30. one who can guess in lesser attempt win a game.

import random #to genarate randon number 
def generate_rand_number():
    random_number = random.randint(10, 30)
    return random_number

def Guess_Number():
    Guess_number=int(input('Guess any number from 10 t0 30 : '))
    return Guess_number

def guess_player(): #function that count number of guesses of player
    count=0
    while(1):
        a=Guess_Number()
        count+=1
        if(a<random_number):
            print("your guess doesnot match.please! guess higher number.")

        elif(a>random_number):
            print("your guess doesnot match.please! guess lesser number.")

        else:
            print("congrulation!! your guess matched.")
            break
    return count  


#for player 1
random_number=generate_rand_number()
name1=input("enter your name player 1 : ")             
print(name1+", lets play............")
a=guess_player()
print(name1 + f"  successfully guess in {a} attempt")



# for player 
random_number=generate_rand_number()
name2=input("enter your name player 2 : ")             
print(name2+", lets play............")
b=guess_player()
print(name2 + f"  successfully guess in {b} attempt")

# final decision
if(a>b):
    print("congrulation!! "+ name2 +"won the match")

else:
    print("congrulation!! "+ name1 +" won the match")

print("Game Over")

