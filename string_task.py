print("""Mad libs where libs get Mad
 Start Below:
""")

time= input("Number: ")
items= (input("Noun(plural): "))
name= input("Name: ")
screem= input("Any sentence: ")
action= input("Verb: ")

print("""\n    It was {} o'clock when I heard a knock at the door.
    I opened the door and there was a box full of {} with a note saying "From Mr. {}".
    Just as I closed the door I heard a scream "{}".
    I froze in place and all I could do was {}.""".format(time,items,name.title(),screem.upper(),action))


