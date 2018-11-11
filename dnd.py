from random import randint
import sys
import os

hero = {
    "name": "Adventurer",
    "armor": 13,
    "stats": {
        "str": 2,
        "dex": 1,
        "int": 1,
        "hp": 20,
        "atk": [6, 13]
    }
}

goblin = {
    "name": "Goblin",
    "armor": 12,
    "stats": {
        "str": 2,
        "dex": 3,
        "int": 1,
        "hp": 20,
        "atk": [5, 12]
    }
}


def dmg(target):
    dmg_roll = randint(1, 20)
    target["stats"]["hp"] = target["stats"]["hp"] - dmg_roll
    print("{} takes {} POINTS OF DAMAGE.".format(target["name"], dmg_roll))
    if target["stats"]["hp"] <= 0:
        print("{} was killed!".format(target["name"]))
        os.system("pause")
        sys.exit(0)


def crit_dmg(target):
    dmg_roll = randint(1, 20)
    target["stats"]["hp"] = target["stats"]["hp"] - 2*dmg_roll
    print("{} takes {} POINTS OF DAMAGE. (2 * {})".format(target["name"], 2*dmg_roll, dmg_roll))
    if target["stats"]["hp"] <= 0:
        print("{} was killed!".format(target["name"]))
        os.system("pause")
        sys.exit(0)


while hero["stats"]["hp"] > 0 or goblin["stats"]["hp"] > 0:
    answer = input("-----------------------------------------------"
                   "\nDo you wish to roll an attack at Goblin? (Y/N)\n"
                   "------------------------------------------------")
    if "y" in answer:
        hit_roll = randint(1, 20)
        if hit_roll >= goblin["armor"] and hit_roll != 20:
            print("[Hit roll: {}] HIT! Roll for damage:".format(hit_roll))
            dmg(goblin)
        if hit_roll == 20:
            print("Critical damage (20)! Damage will be doubled:")
            crit_dmg(goblin)
        if hit_roll < goblin["armor"]:
            print("[Roll: {} (miss)] Goblin defended itself!".format(hit_roll))
            print("Goblin gets an attack of opportunity against you:")
            ret_roll_1 = randint(1, 20)
            if ret_roll_1 >= hero["armor"] and ret_roll_1 != 20:
                print("[Hit roll: {}]".format(ret_roll_1))
                dmg(hero)
            if ret_roll_1 == 20:
                print("Critical hit against you (20):")
                crit_dmg(hero)
            if ret_roll_1 < hero["armor"]:
                print("[Hit: {}] Goblin misses its attack of opportunity.".format(ret_roll_1))
    else:
        print("Goblin attacks you!")
        hit_roll_2 = randint(1, 20)
        if hit_roll_2 >= hero["armor"] and hit_roll_2 != 20:
            print("[Goblin roll: {}]".format(hit_roll_2))
            dmg(hero)
        if hit_roll_2 == 20:
            print("Critical damage (20)! Damage will be doubled against you:")
            crit_dmg(hero)
        if hit_roll_2 < hero["armor"]:
            print("[Goblin's Roll: {} (miss)] You managed to defend yourself "
                  "from the goblin's attack!)".format(hit_roll_2))
            re_choice = input("You get an attack of opportunity. Do you wish to roll for it? (Y/N)")
            if "y" in re_choice:
                ret_roll_2 = randint(1, 20)
                if ret_roll_2 >= goblin["armor"] and ret_roll_2 != 20:
                    print("[Hit roll: {}] Hit! Roll for damage:".format(ret_roll_2))
                    dmg(goblin)
                if ret_roll_2 == 20:
                    print("Critical damage! Roll for dmg:".format(ret_roll_2))
                    crit_dmg(goblin)
                if ret_roll_2 < goblin["armor"]:
                    print("[Hit: {}] You've missed your attack of opportunity.".format(ret_roll_2))
