import random
import os
import time

print("welcomme to among us you are red")
locations = ["Admin", "Cafeteria", "Communications", "Electrical", "Engines", "MedBay", "Navigation", "Bedroom"]
tasks = ["swipe the card", "empty garbage", "upload data", "fix wires", "align engine output", "inspect a sample",
         "do a chart course", "sleep"]

c_list = ["Red",
          "Blue",
          "Green",
          "Pink",
          "Orange",
          "Yellow",
          "Purple",
          "Brown", ]
#random crewmates and imposter
imposter = "Red"
c_list.remove("Red")
#copypool:
copypool = c_list.copy()
crew1 = random.choice(copypool)
copypool.remove(crew1)
crew2 = random.choice(copypool)
copypool.remove(crew2)
crew3 = random.choice(copypool)
copypool.remove(crew3)
if imposter == "Red":
    print("you are the imposter")
    choice = "impost"

else:
    print("you are a crewmate")
    choice = "crew"

while choice == "crew":

    random_number = random.randint(0, len(locations) - 1)
    locationo = locations[random_number]
    taske = tasks[random_number]
    crew3 = random.choice(c_list)
    print(f"you are in (the) {locationo} you must {taske}   you see {crew3} and {crew2}")

    input("press enter to continue: ")

    os.system("clear")
    if locationo == "Cafeteria":
        operation = int(input("3+5 =: "))
        if operation == 8:
            print("you did the task")
            locations.remove("Cafeteria")
            tasks.remove("empty garbage")
            crew2 = random.choice(c_list)
            copypool.remove(crew3)
            crew3 = random.choice(c_list)
            copypool.remove(crew3)
            random_number = random.randint(0, len(locations) - 1)
        elif operation != 8:
            print(f"you did not do the task so {imposter} killed you")
            input("press enter to continue: ")
            os.system("clear")
            quit("you died")

    elif locationo == "Admin":
        capital_ = input("what is the capital of russia: ")
        if capital_ == "Moscow" or capital_ == "moscow":
            print("you did the task")
            crew3 = random.choice(c_list)
            copypool.remove(crew3)
            locations.remove("Admin")
            tasks.remove("swipe the card")
            crew2 = random.choice(c_list)
            copypool.remove(crew2)
            random_number = random.randint(0, len(locations) - 1)
        elif capital_ != "Moscow" or capital_ != "moscow":
            print(f"you did not do the task so {imposter} killed you")
            input("press enter to continue: ")
            os.system("clear")
            quit("you died")
    elif locationo == "Communications":
        python_ = input("what is the most used programming language in the world: ")
        if python_ == "Python" or python_ == "python":
            print("you did the task")
            locations.remove("Communications")
            tasks.remove("upload data")
            crew3 = random.choice(c_list)
            copypool.remove(crew3)
            crew2 = random.choice(c_list)
            copypool.remove(crew2)
            random_number = random.randint(0, len(locations) - 1)
        else:
            print(f"you did not do the task so {imposter} killed you")
            input("press enter to continue: ")
            os.system("clear")
            quit("you died")
    elif locationo == "Electrical":
        zzap_ = input("red+blue=: ")
        if zzap_ == "purple" or zzap_ == "Purple":
            print("you did the task")
            locations.remove("Electrical")
            tasks.remove("fix wires")
            crew3 = random.choice(c_list)
            crew2 = random.choice(c_list)
            random_number = random.randint(0, len(locations) - 1)
        else:
            print(f"you did not do the task so {imposter} killed you")
            quit("you died")
    elif locationo == "Engines":
        print("aligning engine output...")
        time.sleep(3)
        print("you did the task")
        locations.remove("Engines")
        tasks.remove("align engine output")
        crew3 = random.choice(c_list)
        crew2 = random.choice(c_list)
        random_number = random.randint(0, len(locations) - 1)
    elif locationo == "MedBay":
        is_insect = input("is a spider an insect y/n: ")
        if is_insect == "n" or is_insect == "N":
            print("you did the task")
            locations.remove("MedBay")
            tasks.remove("inspect a sample")

            crew3 = random.choice(c_list)
            crew2 = random.choice(c_list)
            random_number = random.randint(0, len(locations) - 1)
        else:
            print(f"you did not do the task so {imposter} killed you")
            quit("you died")
    elif locationo == "Navigation":
        question = input("give your review on this game: ")
        if question != "":
            print("you did the task")
            locations.remove("Navigation")
            tasks.remove("do a chart course")
            crew3 = random.choice(c_list)
            crew2 = random.choice(c_list)
            random_number = random.randint(0, len(locations) - 1)
        else:
            print(f"you did not do the task so {imposter} killed you")
            quit("you died")
    elif locationo == "Bedroom":
        print("nap time 3 secs")
        time.sleep(3)
        print("you did the task")
        locations.remove("Bedroom")
        tasks.remove("sleep")
        crew3 = random.choice(c_list)
        crew2 = random.choice(c_list)
        random_number = random.randint(0, len(locations) - 1)

    eject_ = input("do you want to eject someone y/n: ")
    if eject_ == "y" or eject_ == "Y":
        print(c_list)
        who_to_eject = input("Who do you want to eject: ")
        if who_to_eject in c_list:
            c_list.remove(who_to_eject)
            if who_to_eject == imposter:
                print(f"{who_to_eject} was the imposter")
                input("press enter to continue: ")
                os.system("clear")
                quit(f"you won")
        else:
            print(f"{who_to_eject} is not a player")
    if len(locations) == 1:
        choice = "win"
if choice == "win":
    input("press enter to continue: ")
    os.system("clear")
    quit(f"you won the imposter was {imposter}")
while choice == "impost":
    crew1 = random.choice(c_list)
    crew2 = random.choice(c_list)
    crew3 = random.choice(c_list)
    mogus = random.randint(0, 2)
    random_number = random.randint(0, len(locations) - 1)
    locationo = locations[random_number]
    if mogus == 0:
        crew1 = random.choice(c_list)
        print(f"you are in the {locationo} you see {crew1}")
        print("you killed him")
        random_number = random.randint(0, len(locations) - 1)
        c_list.remove(crew1)
        locationo = locations[random_number]
        mogus = random.randint(0, 2)
        input("press enter to continue: ")
        os.system("clear")
    elif mogus == 1:
        crew1 = random.choice(c_list)
        crew2 = random.choice(c_list)
        print(f"you are in the {locationo} you see {crew1} and {crew2} ")
        kill_input = input("do you want to kill one of them y/n: ")
        if kill_input == "y" or kill_input == "Y":
            print(f"you killed {crew1} but {crew2} ejected you")
            input("press enter to cotinue")
            os.system("clear")
            quit("you died")
        else:
            print("you switched rooms")
            locationo = locations[random_number]
            crew1 = random.choice(c_list)
            crew2 = random.choice(c_list)
            mogus = random.randint(0, 2)
            random_number = random.randint(0, len(locations) - 1)
            input("press enter to continue: ")
            os.system("clear")
    elif mogus == 2:
        crew1 = random.choice(c_list)
        crew2 = random.choice(c_list)
        crew3 = random.choice(c_list)
        mogus = random.randint(0, 2)
        locationo = locations[random_number]
        random_number = random.randint(0, len(locations) - 1)
        print(f"you are in the {locationo} you see {crew1}, {crew2} and {crew3} ")
        kill_input = input("do you want to kill one of them y/n: ")
        if kill_input == "y" or kill_input == "Y":
            print(f"you killed {crew1} but {crew2} and {crew3} ejected you")
            input("press enter to cotinue")
            os.system("clear")
            quit("you died")
        else:
            print("you switched rooms")
            locationo = locations[random_number]
            crew1 = random.choice(c_list)
            crew2 = random.choice(c_list)
            mogus = random.randint(0, 2)
            random_number = random.randint(0, len(locations) - 1)
            input("press enter to continue: ")
            os.system("clear")
    if len(c_list) == 1:
        choice == "win"
if choice == "win":
    input("press enter to continue:")
    os.system("clear")
    quit("you won you killed all the crewmates")
