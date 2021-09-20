def volume(l, w, h):
    return l * w * h


length = int(input("type length"))
width = int(input("type width"))
height = int(input("type height"))

print("The volume of the rectangular prism is " + str(volume(length, width, height)) + " cubic meters")
