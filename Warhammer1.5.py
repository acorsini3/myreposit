
import random
#Class definition
class Hero:
    name = ""
    strenght = 0
    weapon = ""
#Method
    def fight(self):
        print(self.name + " is fighting with a " + self.weapon + " and a strenght of " + str(self.strenght))

#Objects
warrior = Hero()
warrior.name = "Arbaal"
warrior.strenght = random.randint(1,10)
warrior.weapon = "Double Axe"

deamon = Hero()
deamon.name = "Azazel"
deamon.strenght = random.randint(1,10)
deamon.weapon = "Giant Sword"

warriorHealthPoint = 10
deamonHealthPoint = 10

print(warrior.name + "'s health points = " + str(warriorHealthPoint))
print(deamon.name + "'s health points = " + str(deamonHealthPoint))

warrior.fight()
deamon.fight()
#calcul des points restants
warriorHealthPoint = (warriorHealthPoint - deamon.strenght) 
deamonHealthPoint = (deamonHealthPoint - warrior.strenght)
#affichage des points restants
print(warrior.name + "'s health points = " + str(warriorHealthPoint))
print(deamon.name + "'s  health points = " + str(deamonHealthPoint))

try: 
    while warriorHealthPoint !=0 and deamonHealthPoint !=0 :
        warrior.fight()
        deamon.fight()
        #calcul des points restants
        warriorHealthPoint = (warriorHealthPoint - deamon.strenght) 
        deamonHealthPoint = (deamonHealthPoint - warrior.strenght)
        #affichage des points restants
        print(warrior.name + "'s health points = " + str(warriorHealthPoint))
        print(deamon.name + "'s  health points = " + str(deamonHealthPoint))
        break   
                
except:    
    print("Game is over")
    quit()   

if (warriorHealthPoint<1) and (deamonHealthPoint <1):
    print("nobody wins ! ")
elif (deamonHealthPoint <1):
    print(warrior.name + " wins ! ")
elif (warriorHealthPoint <1):
    print(deamon.name + " wins ! ")
