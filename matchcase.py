import random

kill_list = ["stabbed", "stabbed", "stabbed", "fucked", "killed", "killed", "eaten", "eaten", "eaten", "eaten",

             "poisonned", "poisonned", "sent in hell", "was ejected from amogus", "was ejected from amogus", ]

kill_choice = random.choice(kill_list)

match kill_choice:
    case "stabbed":
        death_unprobabilyty = 40

    case "fucked":
        death_unprobabilyty = 30

    case "killed":
        death_unprobabilyty = 20

    case "eaten":
        death_unprobabilyty = 10
    case "poisonned":
        death_unprobabilyty = 7

    case _:
        death_unprobabilyty = 0
print(death_unprobabilyty)

