import random  # to generate random number

random_number = random.randint(10, 30)
random_number = 16  # Uncomment this for testing

# Player 1:
def guess_number():
    return int(input('Guess any number from 10 to 30: '))

def guess_player():
    count = 0
    while(1):
        a = guess_number()
        count += 1
        if a < random_number:
            print("Your guess does not match. Please guess a higher number.")
        elif a > random_number:
            print("Your guess does not match. Please guess a lower number.")
        else:
            print("Congratulations!! Your guess matched.")
            break
    return count

print("Player 1, let's play............")
attempts = guess_player()
print(f"You successfully guessed in {attempts} attempt(s).")
