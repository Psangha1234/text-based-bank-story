# text-based RPG: Bank Heist 

score = 0
name = input("Welcome to Bank Heist Survival! What is your name? ")
print(f"Hi {name}! We hope you will enjoy the game. Here we go...\n")
      
print("You are walking to the bank.")
print("Walk [i]nside.")
ans1 = input("Choice: ").lower().strip()
    #DECISION 1
if ans1 == "i":
    score += 5
    print("You walk through the glass doors.")
    print("There are people waiting in line.")
    print("You hear a BANG.")
    print("[D]uck behind a chair.")
    print("Stand up and [C]onfront the gunman.")
    ans2 = input("Choice: ").lower().strip()
        #DECISION 2
    if ans2 == "d":
        score += 10
        print("You duck behind a chair.")
        print("The gunman yells for everyone to stay down.")
        print("Stay [H]idden.")
        print("Try to [R]un for the exit.")
        ans3 = input("Choice: ").lower().strip()
            #DECISION 3
        if ans3 == "h":
            score += 10
            print("The gunman grabs the teller.")
            print("He shouts for the money.")
            print("Pretend to be [D]ead.")
            print("Try to [C]all the police.")
            print("Wait [Q]uietly.")
            ans4 = input("Choice: ").lower().strip()
                #DECISION 4
            if ans4 == "d":
                score += 20
                print("You lie still on the ground.")
                print("The gunman doesn't notice you.")
                print("The police arrive and arrest him.")
                print("You survive.")
                print("Do you want to [E]scape now or [S]tay until police clear the area?")
                ans5 = input("Choice: ").lower().strip()
                #DECISION 5
                if ans5 == "e":
                    score += 10
                    print("You sneak out quietly and escape safely. You win!")
                elif ans5 == "s":
                    score += 5
                    print("You wait patiently. Police secure the area. You're safe for now.")
                else:
                    score -= 10
                    print("Invalid choice. You hesitate and get caught in crossfire. You die.")
            elif ans4 == "c":
                score -= 20
                print("You pull out your phone.")
                print("The gunman sees you and shoots.")
                print("You die instantly.")
            elif ans4 == "q":
                score += 15
                print("You wait silently.")
                print("The police arrive and tackle the gunman.")
                print("You survive.")
            else:
                score -= 10
                print("Invalid choice. You freeze and get caught.")
        elif ans3 == "r":
            score -= 15
            print("You run to the exit.")
            print("The gunman sees you and shoots.")
            print("You collapse to the floor, dead.")
        else:
            score -= 10
            print("Invalid choice. You freeze and get caught.")
    elif ans2 == "c":
        score -= 20   
        print("You stand up and shout at the gunman.")
        print("He points his gun at you and fires.")
        print("You die instantly.")
        print("Do you want to [R]etry or [Q]uit?")
        ans6 = input("Choice: ").lower().strip()
        #DECISION 6
        if ans6 == "r":
            print("Restarting the game...\n")
        elif ans6 == "q":
            print("Game over. Stay safe next time!")
        else:
            print("Invalid choice. Exiting game.")
else:
    score += 5 
    print("You decide not to enter.")
    print("Moments later, you hear sirens.")
    print("You survived by accident.")

print(f"\n{name}, your final score is: {score}")
