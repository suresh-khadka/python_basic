with open("student.txt") as f:
    str=f.read()
    print(str)

a=f.read()     #open and closed inside with statement so, we cant read again
print(a)