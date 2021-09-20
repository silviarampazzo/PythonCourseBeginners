import string

ex_8 = "orange"
print(ex_8[2])  # a --> python is 0 indexed
print("apple"[4])

# string slicing
ex_10 = "apricots"
print(ex_10[:3]) # apr
print(ex_10[2:5]) # ric
print(ex_10[4:]) # cots

# string concatenation
print("peacon" + " " + "pie")

# Exercises
my_str = "Just do it!"
print(my_str[10])
sliced = my_str[5:7]
print(sliced)
sliced1 = my_str[8:]
print(sliced1)
sliced2 = my_str[:4]
print(sliced2)
concat = "Don't " + sliced + " " + sliced1
print(concat)
print("Don't " + my_str[5:])

v = 2.45
print(type(v))
print((str(v) + " is a float"))
print("\"Hello, I'm Silvia, it's nice to meet you!\"")
print("*******\n ***** \n  ***  \n   *   ")

name = input("What is your name?")
quest = input("What is your quest?")
color = input("What is your favorite color?")
print("So your name is " + name + ", your quest is " + quest + " and your favorite color is " + color)

