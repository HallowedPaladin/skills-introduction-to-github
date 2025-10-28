"""
A small python program that convers a temperature from celsius to farenheight
"""
celsius=0
fahrenheit=0
result=0
tempType='c'


print('Are converting from Celsius(c) or Fahrenheit(f)')
tempType = input()
if tempType == 'c':
    print('What is your value?')
    celsius = input()
    #takles input for value to be converted
    result= (int(celsius)* 9/5) + 32
    #converts celsius value into fahrenheit value via a formula
    print(celsius,' is ',result,' in fahrenheit')
    #prints out original value and converted result

elif tempType == 'f':
    print('What is your value?')
    fahrenheit = input()
    result=(int(fahrenheit) -32) * 5/9
    #converts fahrenheit value into celsius by reversing original formula
    print(fahrenheit, ' is ',result,' in celsius')

else:
    print('please enter a valid temperature type')