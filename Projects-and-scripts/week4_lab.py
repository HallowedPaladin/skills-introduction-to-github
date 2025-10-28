
def celsius_to_fahrenheit(celsius_temp):
    fahrenheit = (celsius_temp * 9/5)+32
    return fahrenheit
    #This block of code defines a funciton that takes in a celsius tempture value and then converts it to fahrenheit by running it through a formula then returning the value.

c_temp = 25
f_temp = celsius_to_fahrenheit(c_temp)
print(f"{c_temp}C is equal to {f_temp}F") 


my_variable = 'I am global'

def test_scope():
    my_variable = 'I, am local'
    print(my_variable)

test_scope()
print(my_variable)
"""The reason these 2 variables produce different results when printed even though they have the same variable name is because there is a global and local variable, where the global variable can be called anywhere
whilst the variable inside the test_scope function can only be called when inside the function, meaning you can have a variable with the same name as long as both are not global."""