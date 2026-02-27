class enemigo:
    tipo_enemigo: str
    puntos_energia: int = 10
    ataque = 1

    def _init_(self, tipo_enemigo, puntos_energia=10, ataque=1):
        self._tipo_enemigo = tipo_enemigo 
        self._puntos_energia = puntos_energia
        self.ataque = ataque


    def get_tipo_enemigo(self):
        return self._tipo_enemigo