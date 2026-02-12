marks1=int(input("enter marks of student"))
marks2=int(input("enter marks of student"))
marks3=int(input("enter marks of student"))

obtained=marks1+marks2+marks3
total=300
per=(obtained/total)*100
mark1_per=(marks1/100)*100
mark2_per=(marks2/100)*100
mark3_per=(marks3/100)*100

if(per>40 and mark1_per>33 and mark2_per>33 and mark3_per>33):
    print("student is pass")

else:
    print("student is fail")
print(marks1," is marks of sub_1")
print(marks2)
print(marks3)
