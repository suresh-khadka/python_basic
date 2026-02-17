with open("new.html") as f:
    line=f.readline()
    lineno=1

    while(line!=""):
        l=line
        if("python" in l):
            print(f"python is present in line number : {lineno}")
            break
        lineno+=1 

    else:
        print("python is not present")   

    