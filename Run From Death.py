name = input("Enter your name.")
print(f"Hello, {name}! You are about to wake up from one nightmare into another. ")
start = input("You awaken from a nightmare and see Death at the foot of your bed. Run From Death? (yes/no)")

if start == "yes":
    print("You leap from your bed and run through the kitchen towards the front door.")
    response = input("Grab the flashlight or run out of the door?")
    if response == "grab the flashlight":
        print("You grab the flashlight in a haste and make it out the front door.")
        pathway = input("You see two paths one is moonlit the other is a dark woods. Moonlit path or dark woods?")
        if pathway == "moonlit path":
            print("The moon shines a clear path. You run fast yet carelessly. You trip over your own feet. Death/'s cold hand is quickly upon you. Game Over! DEATH 2 of 6.")
            quit()
        elif pathway == "dark woods":
            print("You run into the dark woods guided by your flashlight. You see the trees bend opening a path and a crow that beckons you overhead.")
            woods = input("Follow the trees or trust the crow?")
            if woods == "trust the crow":
                print("The crow leads you down a long path. You take a moment to catch your breath. You look up and see the crow perched on Death/'s scythe. You hear one last caw. Game Over. DEATH 3 of 6")
                quit()
            elif woods == "follow the trees":
                print("The trees lead you to a thicket of thorns. A shadow approaches. There is no way out. Game Over. DEATH ")
                quit()
            else:
                print("Death hears you mumbling and takes you into the shadows! Game Over. DEATH 6 of 7")
                quit()
        else:
            print("Death hears you mumbling and takes you into the shadows! Game Over. DEATH 6 of 7")
            quit()
    elif response == "run out of the door":
        print("You run out of the door with only a moment to think.")
        pathway = input("You see an old tool shed beside the house and a moonlit path. Go to the tool shed or take the moonlit path?")
        if pathway == "take the moonlit path":
            print("You run down the moonlit path as fast as you can. You notice the same trees pass you. You look over your shoulder and there stands Death. Game over. Death 5 of 6.")
        elif pathway == "go to the tool shed":
            print("You enter the shed, close the door, and turn on your flashlight. You hear scratching on the door that grows louder. The moon peers through a small window and a rake is propped up in the corner.")
            choice = input("Grab the rake or exit through the window?")
            if choice == "grab the rake":
                print("You arm yourself with a rake and burst through the door ready to fight. Death swings and misses. You flee deeper into the woods with a shadow quickly appraching.")
                final = input("Do you drop the rake or stand and fight?")
                if final == "stand and fight":
                    print("Your rake is no match and you are vanquished swiftly. Game Over. DEATH")
                    quit()
                elif final == "drop the rake":
                    print(f"Death steps on the rake and it hits him in the face. Embarressed at this cartoonish mistake he lets you live another day. {name}, YOU WIN!")
                    quit()
                else:
                    print("Death hears you mumbling and takes you into the shadows! Game Over. DEATH 6 of 7")
                    quit()
            elif choice == "exit through the window":
                print("You exit through the broken window. Glass cuts your leg. Death hears your screams and harvests your soul. Game Over. DEATH 4 of 6. ")
                quit()
            else:
                print("Death hears you mumbling and takes you into the shadows! Game Over. DEATH 6 of 7")
                quit()
        else:
            print("Death hears you mumbling and takes you into the shadows! Game Over. DEATH 6 of 7")
            quit()
    else:
        print("Death hears you mumbling and takes you into the shadows! Game Over. DEATH 6 of 7")
        quit()
else:
    print("Death hears you mumbling and takes you into the shadows! Game Over. DEATH 6 of 7")
    quit()
