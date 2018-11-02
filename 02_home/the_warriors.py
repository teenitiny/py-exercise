"""
You need to create the class Warrior, the instances of which will have 2 parameters - health (equal to 50 points) and attack (equal to 5 points), and 1 property - is_alive, which can be True (if warrior's health is > 0) or False (in the other case). In addition you have to create the second unit type - Knight, which should be the subclass of the Warrior but have the increased attack - 7. Also you have to create a function fight(), which will initiate the duel between 2 warriors and define the strongest of them. The duel occurs according to the following principle:
every turn one of the warriors will hit another one and the last will lose his health in the same value as the attack of the first warrior. After that, the second warrior will do the same to the first one.
If in the end of the turn the first warrior has > 0 health and the other one doesn’t, the function should return True, in the other case it should return False.
Example:
	chuck = Warrior()
	bruce = Warrior()
	carl = Knight()
	dave = Warrior()

	fight(chuck, bruce) == True
	fight(dave, carl) == False
	chuck.is_alive == True
	bruce.is_alive == False
	carl.is_alive == True
	dave.is_alive == False
"""

class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
    @property
    def is_alive(self):
        return self.health > 0
    
    def decrease_health(self, attack):
        self.health -= attack
    
    def get_attack(self):
        return self.attack
    
    def get_health(self):
        return self.health

class Knight(Warrior):
    def __init__(self):
        Warrior.__init__(self)
        self.attack = 7


def fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        unit_2.decrease_health(unit_1.get_attack())
        if unit_2.is_alive: unit_1.decrease_health(unit_2.get_attack())
    return unit_1.is_alive

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")
