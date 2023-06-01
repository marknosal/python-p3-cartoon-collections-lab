def roll_call_dwarves(dwarves):
    [print(f"{index+1}. {dwarves[index]}") for index in range(len(dwarves))]

def summon_captain_planet(planeteer_calls):
    return [call.capitalize() + '!' for call in planeteer_calls]

def long_planeteer_calls(planeteer_calls):
    for call in planeteer_calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(snacks):
    cheese_types = ['cheddar', 'gouda', 'camembert']
    for snack in snacks:
        if snack in cheese_types:
            return snack
    return None