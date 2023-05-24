import os

counter = 0

while counter < 3:
    counter += 1

    var = os.system('open /System/Applications/Music.app')
    var1 = os.system('open /System/Applications/Contacts.app')
    var2 = os.system('open /System/Applications/FaceTime.app')

    print(var)
    print(var1)
    print(var2)