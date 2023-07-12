import sys
total_deaths = 7
deaths_encountered = 0


def print_title():
    print("   _____                                    _____  ")
    print("  /     \                                  /     \\")
    print(" | () () |                                | () () |")
    print("  \  ^  /        RUN FROM THE REAPER       \  ^  / ")
    print("   |||||                                    |||||  ")
    print("   |||||                                    |||||  ")


def get_name():
    return input("\nEnter your name: ")


def start_game(name):

    while True:
        print(
            f"\nHello, {name}!\n \nYou are sound asleep in your bed when a shadow appears.\n")
        start = input(
            "You wake in a jolt to see the Reaper at the foot of your bed.\n\nRun from the Reaper? (yes/no)\n")

        if start == "yes":
            run_from_reaper(name)
            break
        else:
            print("\n***You have no choice.***\n")


def run_from_reaper(name):
    while True:
        print(
            "\nYou leap from your bed and run towards the front door, a flashlight hangs by the exit.\n")
        response = input("Grab the flashlight or run out of the door?")

        if response == "grab the flashlight":
            grab_flashlight()
        elif response == "run out of the door":
            run_out_of_door(name)
        else:
            print("\n---Quit mumbling---\n \n---Wake up---\n")


def grab_flashlight():
    global deaths_encountered
    print("\nYou grab the flashlight in haste and make it out the front door.\n")
    pathway = input(
        "\nYou see two paths, one is moonlit, the other enters a dark woods.\n Moonlit path or dark woods?\n")

    if pathway == "moonlit path":
        moonlit_path()
    elif pathway == "dark woods":
        dark_woods()
    else:
        print("\n---Quit mumbling---\n \n---Wake up---\n")


def run_out_of_door(name):
    global deaths_encountered
    print("\nYou run out of the door with only a moment to think.\n")
    pathway = input(
        "\nYou see an old tool shed beside the house and a moonlit path.\n Go to the tool shed or take the moonlit path?\n")

    if pathway == "take the moonlit path":
        moonlit_path()
    elif pathway == "go to the tool shed":
        go_to_tool_shed(name)
    else:
        print("\n---Quit mumbling---\n \n---Wake up---\n")


def moonlit_path():
    global deaths_encountered
    deaths_encountered += 1
    print("      ___")
    print("     /   \\")
    print("    |     |")
    print("    | RIP |")
    print("    |     |")
    print("     \\___/")
    print("\nThe moon shines a clear path.\n You run fast yet carelessly.\n You trip over your own feet.\n The Reaper's cold hand is quickly upon you.\n Game Over!\n \nDEATH\n",
          deaths_encountered, "of", total_deaths)


def dark_woods():
    global deaths_encountered
    print("\nYou run into the dark woods guided by your flashlight.\n \nYou see the trees bend, opening a path and a crow that beckons you overhead.\n")
    woods = input("Follow the trees or trust the crow?")

    if woods == "trust the crow":
        trust_the_crow()
    elif woods == "follow the trees":
        follow_the_trees()
    else:
        print("\n---Quit mumbling---\n \n---Make a decision.---\n")


def trust_the_crow():
    global deaths_encountered
    deaths_encountered + 1
    print("      ___")
    print("     /   \\")
    print("    |     |")
    print("    | RIP |")
    print("    |     |")
    print("     \\___/")
    print("\nThe crow leads you down a long path.\n You take a moment to catch your breath.\n You look up and see the crow perched on the Reaper's scythe.\n You hear one last caw.\n Game Over.\n \nDEATH\n",
          deaths_encountered, "of", total_deaths)


def follow_the_trees():
    global deaths_encountered
    deaths_encountered += 1
    print("      ___")
    print("     /   \\")
    print("    |     |")
    print("    | RIP |")
    print("    |     |")
    print("     \\___/")
    print("\nThe trees lead you to a thicket of thorns.\n A shadow approaches.\n There is no way out.\n Game Over.\n \nDEATH\n",
          deaths_encountered, "of", total_deaths)


def go_to_tool_shed(name):
    global deaths_encountered
    print("\nYou enter the shed, close the door, and turn on your flashlight.\n \nYou hear scratching on the door that grows louder.\n The moon peers through a small window and a rake is propped up in the corner.\n")
    choice = input("Grab the rake or crawl through the window?")

    if choice == "grab the rake":
        grab_the_rake(name)
    elif choice == "crawl through the window":
        crawl_through_the_window()
    else:
        print("\n---Quit mumbling---\n \n---Wake up---\n")


def crawl_through_the_window():
    global deaths_encountered
    deaths_encountered += 1
    print("      ___")
    print("     /   \\")
    print("    |     |")
    print("    | RIP |")
    print("    |     |")
    print("     \\___/")
    print("\nYou crawl out the window getting snagged on some glass.\n The Reaper hears your screams and moves swiftly toward you.\n \nDEATH\n",
          deaths_encountered, "of", total_deaths)


def grab_the_rake(name):
    global deaths_encountered
    print("\nYou grab the rake and rush out the door with the Reaper close behind.\n")
    final = input(
        "\nThe chase quickens, the reaper draws near.\n Do you drop the rake or stand and fight?\n")

    if final == "stand and fight":
        deaths_encountered += 1
        print("      ___")
        print("     /   \\")
        print("    |     |")
        print("    | RIP |")
        print("    |     |")
        print("     \\___/")
        print("\nYou swing the rake but are no match for the scythe.\n \nDEATH\n",
              deaths_encountered, "of", total_deaths)

    elif final == "drop the rake":
        print(
            f"\nYou drop the rake behind you.\nThe Reaper steps on the sharp tines, smacking himself with the handle.\nYou flee into the darkness safely.\nCongratulations, {name}! You WIN!!!\n")
        print("               ...                            ")
        print("             ;::::;                           ")
        print("           ;::::; :;                          ")
        print("         ;:::::'   :;                         ")
        print("        ;:::::;     ;.                        ")
        print("       ,:::::'       ;           OOO\         ")
        print("       ::::::;       ;          OOOOO\        ")
        print("       ;:::::;       ;         OOOOOOOO       ")
        print("      ,;::::::;     ;'         / OOOOOOO      ")
        print("    ;:::::::::`. ,,,;.        /  / DOOOOOO    ")
        print("  .';:::::::::::::::::;,     /  /     DOOOO   ")
        print(" ,::::::;::::::;;;;::::;,   /  /        DOOO  ")
        print(";`::::::`'::::::;;;::::: ,#/  /          DOOO ")
        print(":`:::::::`;::::::;;::: ;::#  /            DOOO")
        print("::`:::::::`;:::::::: ;::::# /              DOO")
        print("`:`:::::::`;:::::: ;::::::#/               DOO")
        print(" :::`:::::::`;; ;:::::::::##                OO")
        print(" ::::`:::::::`;::::::::;:::#                OO")
        print(" `:::::`::::::::::::;'`:;::#                O ")
        print("  `:::::`::::::::;' /  / `:#                  ")
        print("   ::::::`:::::;'  /  /   `#                  ")
        sys.exit()
    else:
        print("\n---Quit mumbling---\n \n---Wake up---\n")


def main():
    print_title()
    name = get_name()
    start_game(name)
    run_from_reaper(name)


main()
