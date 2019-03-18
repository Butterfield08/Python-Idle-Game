#Author Keith Butterfield
#This is a test for AP in RPG
ATK1 = -40
ATK2 = -54
ATK3 = -76


def combat():
    
    e_ap = 30
    p_ap = 56

    player_health = int(input("Please enter the hero's health: "))
    enemy_health = 10
        
    while player_health and enemy_health >= 0:
        print("player AP", p_ap)
        print("enemy AP", e_ap)
        print("")
        p_ap = p_ap + 1
        e_ap = e_ap + 1
        if p_ap == 100:
             print("PLAYER ATTACK!")
             print("Player's Stats", "HP", player_health, "AP", p_ap)
             print("Enemy's Stats", "HP", enemy_health, "AP", e_ap)
             attack = input("1 - base attack, 2, hard attack, 3 super attack")
             if attack == '1':
                p_ap = p_ap + ATK1
                enemy_health = enemy_health - 2
                print("You did 2 damage!")
                print("Player's Stats", "HP", player_health, "AP", p_ap)
                print("Enemy's Stats", "HP", enemy_health, "AP", e_ap)
                resume = input("press enter to continue")#Debugging prupose
             elif attack == '2':
                p_ap = p_ap + ATK2
                enemy_health = enemy_health - 3
                print("You did 3 damage!")
                print("Player's Stats", "HP", player_health, "AP", p_ap)
                print("Enemy's Stats", "HP", enemy_health, "AP", e_ap)
                resume = input("press enter to continue")#Debugging prupose
             elif attack == '3':
                p_ap = p_ap + ATK3
                enemy_health = enemy_health - 4
                print("You did 4 damage!")
                print("Player's Stats", "HP", player_health, "AP", p_ap)
                print("Enemy's Stats", "HP", enemy_health, "AP", e_ap)
                resume = input("press enter to continue")#Debugging prupose
                
        elif e_ap == 100:
            print("ENEMY ATTACK! ")
            print("Player's Stats", "HP", player_health, "AP", p_ap)
            print("Enemy's Stats", "HP", enemy_health, "AP", e_ap)
            attack = input("1 - base attack, 2, hard attack, 3 super attack")
            if attack == '1':
                e_ap = e_ap + ATK1
                player_health = player_health - 2
                print("Enemy did 2 damage!")
                print("Player's Stats", "HP", player_health, "AP", p_ap)
                print("Enemy's Stats", "HP", enemy_health, "AP", e_ap)
                resume = input("press enter to continue")#Debugging prupose
            elif attack == '2':
                e_ap = e_ap + ATK2
                player_health = player_health - 3
                print("Enemy did 3 damage!")
                print("Player's Stats", "HP", player_health, "AP", p_ap)
                print("Enemy's Stats", "HP", enemy_health, "AP", e_ap)
                resume = input("press enter to continue")#Debugging prupose
            elif attack == '3':
                e_ap = e_ap + ATK3
                player_health = player_health - 4
                print("Enemy did 4 damage!")
                print("Player's Stats", "HP", player_health, "AP", p_ap)
                print("Enemy's Stats", "HP", enemy_health, "AP", e_ap)
                resume = input("press enter to continue")#Debugging prupose

    if player_health <= 0:
        print("you lost the battle!")
    else:
        print("you won the battle!")

combat()
    
