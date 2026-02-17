with open("pomes.txt","r") as f:
    str=f.read()
    print(str)

    if("twinkle" in str):
        print("word \"twinkle\" is found ")