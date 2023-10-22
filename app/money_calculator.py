'''
gas money - $0.655 / mile
boba - $5.84
Bottled water 16.9 oz - $1.29, so ~0.07633/fl. oz, so ~$0.611 per cup
Cooking at home - $7.00
'''
money_spent = 0

def get_base_value(base):
    if base == 'walk':
        return 0.655
    elif base == 'boba':
        return 5.84
    elif base == 'water':
        return 0.611
    elif base == 'cook':
        return 7

def add_money_spent(cost):
    global money_spent
    money_spent -= cost

def add_completed_task(task):
    pass

def gas_money(miles):
    return miles * 0.655

def boba(num):
    return num * 5.84

def bottled_water(cups):
    return cups * 0.611

def meals_cooked(num):
    return num * 7