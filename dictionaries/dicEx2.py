music_groups = {"Queen": "Bohemian Rhapsody",
                "Bee Gees": "Stayin' Alive",
                "U2": "One",
                "Michael Jackson": "Billie Jean",
                "The Beatles": "Hey Jude",
                "Bob Dylan": "Like A Rolling Stone"
                }

print(len(music_groups))

for key in music_groups.keys():
    print(key)

for value in music_groups.values():
    print(value)

for key, value in music_groups.items():
    print(key, value)

print(music_groups.get("Promise of the Real", "music_groups does not contain Promise of the Real"))
