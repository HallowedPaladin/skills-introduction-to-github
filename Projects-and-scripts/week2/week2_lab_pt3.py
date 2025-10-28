name = 'Luke'
course = 'Software Engineering'
favMovie = 'Wall-E'
#example of String Concatenation
greeting = 'Hello, my name is ' + name
print(greeting)

#example of using format()
text1 = "My name is {name}, I'm doing {course}".format(name = 'Luke', course = 'Software Engineering')
print(text1)

#example of using f-strings
text2 = f'My name is {name}, and my favorite movie is {favMovie}'
print(text2)