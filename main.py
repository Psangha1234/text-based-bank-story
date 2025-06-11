# text-based RPG: Bank Heist

name = input("Welcome to Bank Heist Survival! What is your name? ")
print(f"hi {name}! we hope you will enjoy the game. Here we go...\n")

print("you are walking to the bank.")
print("walk [i]nside.")
ans1 = input("choice: ").lower().strip()

if ans1 == "i":
    print("you walk through the glass doors.")
    print("there are people waiting in line.")
    print("you hear a BANG.")
    print("[d]uck behind a chair.")
    print("stand up and [c]onfront the gunman.")
    ans2 = input("choice: ").lower().strip()

    if ans2 == "d":
        print("you duck behind a chair.")
        print("the gunman yells for everyone to stay down.")
        print("stay [h]idden.")
        print("try to [r]un for the exit.")
        ans3 = input("choice: ").lower().strip()

        if ans3 == "h":
            print("the gunman grabs the teller.")
            print("he shouts for the money.")
            print("pretend to be [d]ead.")
            print("try to [c]all the police.")
            print("wait [q]uietly.")
            ans4 = input("choice: ").lower().strip()

            if ans4 == "d":
                print("you lie still on the ground.")
                print("the gunman doesn't notice you.")
                print("the police arrive and arrest him.")
                print("you survive.")
                print("Do you want to [e]scape now or [s]tay until police clear the area?")
                ans5 = input("choice: ").lower().strip()
                if ans5 == "e":
                    print("You sneak out quietly and escape safely. You win!")
                elif ans5 == "s":
                    print("You wait patiently. Police secure the area. You're safe for now.")
                else:
                    print("Invalid choice. You hesitate and get caught in crossfire. You die.")
            elif ans4 == "c":
                print("you pull out your phone.")
                print("the gunman sees you and shoots.")
                print("you die instantly.")
            elif ans4 == "q":
                print("you wait silently.")
                print("the police arrive and tackle the gunman.")
                print("you survive.")
            else:
                print("Invalid choice. You freeze and get caught.")
        elif ans3 == "r":
            print("you run to the exit.")
            print("the gunman sees you and shoots.")
            print("you collapse to the floor, dead.")
        else:
            print("Invalid choice. You freeze and get caught.")
    elif ans2 == "c":
        print("you stand up and shout at the gunman.")
        print("he points his gun at you and fires.")
        print("you die instantly.")
        print("Do you want to [r]etry or [q]uit?")
        ans6 = input("choice: ").lower().strip()
        if ans6 == "r":
            print("Restarting the game...\n")
        elif ans6 == "q":
            print("Game over. Stay safe next time!")
        else:
            print("Invalid choice. Exiting game.")
else:
    print("you decide not to enter.")
    print("moments later, you hear sirens.")
    print("you survived by accident.")

