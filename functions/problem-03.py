def greatest(a,b,c):
    if(a>b and a>c):
        print(f'{a} is greatest')
    if(b>a and b>c):
        print(f'{b} is greatest')
    else:
        print(f'{c} is greatest')

a=int(input('enter any number : '))
b=int(input('enter any number : '))
c=int(input('enter any number : '))
greatest(a,b,c)