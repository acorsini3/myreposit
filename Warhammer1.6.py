
import random
#Class definition
class Hero:
 
#Method
    def __init__(self, name, strenght, weapon):
        self.name = name
        self.strenght = strenght
        self.weapon = weapon

    def fight(self):
        print(self.name + " is fighting with a " + self.weapon + " and a strenght of " + str(self.strenght))

#Objects
warrior = Hero("Arbaal", random.randint(1,10), "Double Axe")

deamon = Hero("Azazel", random.randint(1,10), "Giant Sword")

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
    while warriorHealthPoint >0 and deamonHealthPoint >0 :
        warrior.fight()
        deamon.fight()
        #calcul des points restants
        warriorHealthPoint = (warriorHealthPoint - deamon.strenght) 
        deamonHealthPoint = (deamonHealthPoint - warrior.strenght)
        #affichage des points restants
        print(warrior.name + "'s health points = " + str(warriorHealthPoint))
        print(deamon.name + "'s  health points = " + str(deamonHealthPoint))
          
                
except:    
    print("Game is over")
    quit()   

if (warriorHealthPoint<1) and (deamonHealthPoint <1):
    print("nobody wins ! ")
elif (deamonHealthPoint <1):
    print(warrior.name + " wins ! ")
elif (warriorHealthPoint <1):
    print(deamon.name + " wins ! ")
