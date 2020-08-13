from classes.game import Person, bcolors

magic = [{
    "name": "Fire",
    "cost": 10,
    "dmg": 100
},
    {
    "name": "Thunder",
    "cost": 10,
    "dmg": 124
},
    {
    "name": "Blizzard",
    "cost": 100,
    "dmg": 60
}]

player = Person(900, 65, 60, 34, magic)

enemy = Person(1200,65,45,25,magic)

running = True
i = 0

print( "An Enemy Attacks!")

while running: 
    print("=========================================")
    player.choose_action()

    choice = input("Choose an Action: ")

    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.self_damage(dmg)

        print("total enemy HP is:",enemy.get_hp())
        print("generated damage to enemy is:",dmg )
        
        enemy_choice = 1
        enemy_dmg = enemy.generate_damage()
        player.self_damage(enemy_dmg)
        print("=================================")
        print("enemy attacks for",enemy_dmg,"Your current HP is",player.get_hp())

        if enemy.get_hp() == 0:
            print("You win the battle")
        elif player.get_hp() == 0:
            print("you died")
            running = False

    elif index == 1:
        player.choose_magic()
        magic_choice = input("Choose magic")
        magic_choice = int(magic_choice) - 1
        magic_damage = player.generate_spell_damage(magic_choice)

        enemy.self_damage(magic_damage)
        print("total enemy HP is:",enemy.get_hp())
        print("generated magic damage to enemy is:",magic_damage )
        


        enemy_choice = 1
        enemy_dmg = enemy.generate_damage()
        player.self_damage(enemy_dmg)
        print("=================================")
        print("enemy attacks for",enemy_dmg,"Your current HP is",player.get_hp())

        if enemy.get_hp() == 0:
            print("You win the battle")
        elif player.get_hp() == 0:
            print("you died")
            running = False


    # running = False