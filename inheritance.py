class player: #Player Object that acts as a parent
    movement = 100
    maxHealth = 250
    currentHealth = 250
    atkDamage = 50


class ranger(player):#Adds range and projectile speed to the player
    atkRange = 500
    projectileSpeed = 150


class paladin(player):#Adds armor and a heal ability to the player
    ability = Heal()#non existent function meant as a representation of what could be done
    armor = 30
