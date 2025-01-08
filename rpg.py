name = input("enter your character's name: ")
name_type = input(f"what will {name}'s category be (a)wizard, (b)barbarian,(c)knight or just choose a custom one: ")
if name_type == "a":
    print(f"{name} is now a wizard")
    name_type_stats = {"attack": 50, "defense": 50,"health":100,"ability 1": "Wand smash", "ability 2": "fire rain", "ability3":"supermagic",
                       "inventory": "magic wand","money": 1000000}
elif name_type == "b":
    print(f"{name} is now a barbarian")
    name_type_stats = {"attack": 30, "defense": 5,"health":30,"ability 1": "take this!!!", "ability 2": "SMASH!??!",
                       "ability3": "heal",
                       "inventory": "smashy-smashy","money":1000}
elif name_type == "c":
    print(f"{name} is now a knight")
    name_type_stats = {"attack": 35, "defense": 25, "health": 50, "ability 1": "excalibur", "ability 2": "king's order",
                       "ability3": "helmet protect",
                       "inventory": "the mighty excalibur","money":100000}
else:
    print(f"{name}'s category is {name_type}")
    name_type_stats ={f"{name}":f"{name_type}"}
print(name_type_stats)
