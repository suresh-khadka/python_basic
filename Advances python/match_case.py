def select_choices(choice):
    match(choice):
        case 200:
            return "good morning"
        
        case 300:
            return  "love you"
        
        case _:
            return "invalid"
        

a=int(input("enter any number : "))
print(select_choices(a))    