class player: #Player Object that acts as a parent
    movement = 100
    maxHealth = 250
    currentHealth = maxHealth
    atkDamage = 50
    atkSpeed = 1.0

    def ability(self):#ability that does double damage
        bigAttack = self.atkDamage * 2
        return bigAttack

class ranger(player):#Adds range and projectile speed to the player
    atkRange = 500
    projectileSpeed = 150

    def ability(self):#Polymorph to an attack that does more damage
        biggerAttack = self.atkDamage * 3
        return biggerAttack

class paladin(player):#Adds armor and a heal ability to the player
    maxHealth = 500
    spells = "Heal"
    armor = 30

    def ability(self):#Polymorph the ability into a heal
        heal = self.maxHealth * .2
        return heal
        
