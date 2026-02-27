from Enemigo import *

class zombie(enemigo):
    def _init_(self, puntos_energia=10, ataque=1):
        super()._init_(tipo_enemigo='zombie', puntos_energia=puntos_energia, ataque=1)

        def habla(self):
            print("Hummmm......")

            def propagar_enfermedad(self):
                print("El zombie esta tratando de propagar la enfermedad!!")