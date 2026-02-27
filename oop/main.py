from Enemigo import*
from Zombie import*
from Ogro import*

Zombie = zombie(10, 1)
Ogro =Ogro(20, 3)
print(f"{Zombie.get_tipo_enemigo()}tiene {zombie.puntos_energia}de energia y puede hacer ataques de {zombie.ataque}")
print(f"{zombie.habla()}")
print(f"{Ogro.get_tipo_enemigo()}tiene {Ogro.puntos_energia}de energia y puede hacer ataques de {Ogro.ataque}")
print(f"{Ogro.habla()}")

