import random


class Enemy:
    hp = 200

    def __init__(self, atkL, atkH):
        self.atkL = atkL
        self.atkH = atkH

    def getAtk(self):
        print("Attack Damage is", self.atkL)

    def getHP(self):
        print("HP is", self.hp)


enemy1 = Enemy(40, 49)
enemy1.getAtk()
enemy1.getHP()
enemy2 = Enemy(75, 90)
enemy2.getAtk()
enemy2.getHP()

'''
playerHP = 260
enemyatkH = 80
enemyatkL = 60


while playerHP > 0:
    dmg = random.randrange(enemyatkL,enemyatkH)
    playerHP = playerHP - dmg

    if playerHP <= 30:
        playerHP = 30
        # print('You are Dead')
        print("enemy caused ",dmg,"points of damage. Current HP is: ",playerHP )

    if playerHP > 30:
        # pass
        continue


    print("enemy caused ",dmg,"points of damage. Current HP is: ",playerHP)
    print("You have been teleported to the nearest hospital")
    break
'''