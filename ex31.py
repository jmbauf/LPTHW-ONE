print "You enter a dark room with two doors.  Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant mumble rapper here obfuscating in autotune.  What do you do?"
    print "1. Offer him a refreshing Sprite."
    print "2. Tell him to gain vocabulary."

    mumblerapper = raw_input("> ")

    if mumblerapper == "1":
        print "The mumble rapper spikes your Sprite and mumbles more.  Good job!"
    elif mumblerapper == "2":
        print "The mumble rapper gets increasingly frustrated and yells at you whilst dabbing.  Good job!"
    else:
        print "Well doing %s is probably better.  Mumble rapper goes to sleep." % mumblerapper

elif door == "2":
    print "You stare at the limited edition Big Baller Brand shoes."
    print "1. You become Lonzo Ball."
    print "2. You become that which you are not: a Big Baller Brand marketer."
    print "3. You sign a deal with Timberland, as you are the Dread DORMAMMU, pureveyor of fly kicks."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello.  Good job!"
    else:
        print "The irony of this situation turns you into an expert Captain America player.  Thumbs up, soldier!"

else:
    print "You wake up with a strange creature on your head and a propensity to complain on Twitter. This creature is Firebrand. Sad!"
