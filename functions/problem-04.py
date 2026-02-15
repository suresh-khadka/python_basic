def celsius_to_fahrenheit(c):
    f = (c * 9/5) + 32
    return f

a = int(input('Enter temperature in Celsius: '))
n = celsius_to_fahrenheit(a)
print('In Fahrenheit:' , n)  
# print('In Fahrenheit:' + n)     **we can ony concatinate string to string ont string to float
