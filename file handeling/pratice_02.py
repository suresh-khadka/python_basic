import random

def game():
    score=random.randint(1,50)
    print("your score is:",score)

    with open("highscore.txt") as f:
        high_score=f.read()
        if(high_score!=""):
            high_score=int(high_score)

        else:
            high_score=0

    print(f"your high score is : {high_score}")

    
    if(score>high_score):
        with open("highscore.txt","w") as f:
            f.write(str(score))
        

game()