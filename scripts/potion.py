import random


def use_potion(ppv):
    """this function add a random pv number to the player but reduce the number by 1.  A error message display if he has no more potion."""
    potion = random.randint(15, 50)
    ppv += potion
    if ppv>50:
        ppv=50
    return ppv
  

