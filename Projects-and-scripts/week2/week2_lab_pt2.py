name = 'Luke'
age = 19
randomNumber = 2.7
isBored = True

print('My name is ',name, ' and this message contains my name which is in the form of a string data type')
print('I am ',age,' years old, and this message contained my age which is in the form of a int data type')
print(randomNumber,' is a random number i thought up of, and its in the form of a float data type, different to a int due to the value being a decimal')
if isBored == True:
    print(isBored)
    print('If i am bored, then this message will be printed alongside a "True", by checking the isBored variable, a varaible in the form of the boolean data type')
elif isBored == False:
    print(isBored)
    print('If i am not bored, then this message will be printed alongside a "False", by checking the isBored variable, a variable in the form of the boolean data type')
print(str(isBored),' <- This is the isBored boolean, which has now been converted to a string')
#python allows us to change variables data type mid way through a program due to the language being dynamic, allowing for more flexible and concise code