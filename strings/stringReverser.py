my_string = input("Please insert a string: ")
s_range = range(len(my_string), 0, -1)
reversed_string = ""

for s in s_range:
    reversed_string = "".join([reversed_string, my_string[s-1]])

print(reversed_string)