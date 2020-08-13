import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self, hp, mp, atk, df, magic):
        self.maxHP = hp
        self.hp = hp
        self.maxMP = mp
        self.mp = mp
        self.atkL = atk -10
        self.atkH = atk +10
        self.df = df
        self.magic = magic
        self.actions = ["Attack","Magic"]


    def generate_damage(self):

        return random.randrange(self.atkL,self.atkH)

    def generate_spell_damage(self,i):
        mgl = self.magic[i]["dmg"]-5
        mgh = self.magic[i]["dmg"] + 5

        return random.randrange(mgl,mgh)


    def self_damage(self,dmg):
        self.hp = self.hp - dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp
    
    def get_hp(self):
        return self.hp

    def get_maxHP(self):
        return self.maxHP

    def get_Mp(self):
        return self.mp
        
    def get_maxMp(self):
        return self.maxMP

    def reduce_mp(self,cost):
        self.mp = self.mp - cost

    def get_spell_name(self, i):
        return self.magic[i]["name"]

    def get_spell_mp_cost(self,i):
        return self.magic[i]["cost"]

    def choose_action(self):
        i = 1
        print("Actions")
        for item in self.actions:
            print(str(i)+":",item)
            i+=1

    def choose_magic(self):
        i = 1
        print("Magic")
        for spell in self.magic:
            print(str(i)+":",spell["name"], "(cost:",str(spell["cost"])+")")
            i +=1


             

    



