#implicit type conversion
x=10
y=10.2
z="hello"
print(x+y, type(x+y))

#explicit type conversion
age=input("what is your age?")
print(age, type(int(age)))

name=input("what is your name?")
print(name,type(str(name)))