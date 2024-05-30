#ejercicio listas

class Fabrica:
    def __init__(self, N):
        if N <= 0:
            raise ValueError("El número de tipos de embalajes debe ser un valor positivo.")
        self.N = N
        self.embalajes = []

    def agregar_planilla(self, tipo, maquina, cantidad):
        if not (1 <= tipo <= self.N):
            raise ValueError(f"El tipo de embalaje debe estar entre 1 y {self.N}.")
        if not (1 <= maquina <= 5):
            raise ValueError("La máquina debe estar entre 1 y 5.")
        if cantidad < 0:
            return False  # Indica que se ha ingresado una cantidad negativa para terminar el ingreso
        self.embalajes.append((tipo, maquina, cantidad))
        return True

    def cantidad_total_embalajes(self):
        return sum(cantidad for _, _, cantidad in self.embalajes)

    def cantidad_por_maquina(self):
        cantidades = [0] * 5
        for _, maquina, cantidad in self.embalajes:
            cantidades[maquina - 1] += cantidad
        return cantidades

    def cantidad_por_tipo(self):
        cantidades = [0] * self.N
        for tipo, _, cantidad in self.embalajes:
            cantidades[tipo - 1] += cantidad
        return cantidades

    def tipo_mayor_cantidad(self):
        cantidades = self.cantidad_por_tipo()
        max_cantidad = max(cantidades)
        return [i + 1 for i, cantidad in enumerate(cantidades) if cantidad == max_cantidad]

    def tipos_no_producidos(self):
        cantidades = self.cantidad_por_tipo()
        return [i + 1 for i, cantidad in enumerate(cantidades) if cantidad == 0]


# Ejemplo de uso
def main():
    fabrica = Fabrica(4)

    # Agregar planillas (tipo, maquina, cantidad)
    datos = [
        (1, 1, 100),
        (2, 2, 200),
        (3, 3, 300),
        (4, 4, 400),
        (1, 5, 500),
        (2, 1, 600),
        (3, 2, 700),
        (4, 3, 800),
        (1, 4, 900),
        (2, 5, 1000),
        (3, 1, 1100),
        (4, 2, 1200),
        (1, 3, 1300),
        (2, 4, 1400),
        (3, 5, 1500),
        (4, 1, 1600),
        (1, 2, 1700),
        (2, 3, 1800),
        (3, 4, 1900),
        (4, 5, 2000),
        (1, 1, -1)  # Indica el fin del ingreso
    ]

    for tipo, maquina, cantidad in datos:
        if not fabrica.agregar_planilla(tipo, maquina, cantidad):
            break

    print("Cantidad total de embalajes fabricados:", fabrica.cantidad_total_embalajes())
    print("Cantidad total de embalajes fabricados por máquina:", fabrica.cantidad_por_maquina())
    print("Cantidad total de embalajes fabricados por tipo:", fabrica.cantidad_por_tipo())
    print("Tipo de embalaje del cual se ha fabricado la mayor cantidad:", fabrica.tipo_mayor_cantidad())
    print("Tipo de embalajes no producidos:", fabrica.tipos_no_producidos())


if __name__ == "__main__":
    main()