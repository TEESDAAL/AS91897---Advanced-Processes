##
# test.py
# Create a test version of the program
# TODO start sprint 16/8, goal create class for enemy mock-up text based version.
from random import randint, shuffle
from time import sleep


# TODO Make player class
class Enemy:
    def __init__(self, name, base_hp, base_attack, base_defence, base_speed, variation = 10):
        def percent_variation():
            return round(1 - (randint(-variation, variation)/100), 2)

        self.name = name
        self.hp = round(base_hp * percent_variation())
        self.max_hp = self.hp
        self.attack = round(base_attack * percent_variation())
        self.defence = round(base_defence * percent_variation())
        self.speed = round(base_speed * percent_variation())

    def introduction(self):
        return f"A wild {self.name} appeared."
    def faint(self):
        return f"The wild {self.name} fainted.\n"
    def stats(self):
        return f"""
        Name: {self.name},
        HP: {self.max_hp},
        Attack: {self.attack},
        Defense: {self.defence},
        Speed: {self.speed}
        """



enemies = []
while "Run game":
    # List of default enemies.
    enemies = [
        #     Name | hp | atk | dfc | spd
        ("Sweet", 20, 10, 5, 12),
        ("Soft Drink", 25, 7, 7, 4),
        ("Pickled Goods", 40, 5, 12, 3),
        ("Citrus", 30, 6, 9, 15),
    ]
    shuffle(enemies)

    for enemy_template in enemies:
        enemy = Enemy(*enemy_template)
        print(enemy.introduction())
        while enemy.hp > 0:
            print(f"""{enemy.hp}/{enemy.max_hp}""")
            damage_dealt = int(input("How much damage do you want to do?\n"))
            enemy.hp -= damage_dealt
            if enemy.hp <= 0:
                print(enemy.faint())
    sleep(2)