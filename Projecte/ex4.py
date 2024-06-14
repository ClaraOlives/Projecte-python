class Coche:
    def __init__(self, marca, llantas, color, precio):
        #característiques que demanen
        self.marca = marca
        self.llantas = llantas
        self.color = color
        self.precio = precio

        #com s'escriuran
    def marca_coche(self):
        print(f"Coche: {self.marca}.")

    def tipo_llantas(self):
        print(f"\nEl coche tiene las llantas de {self.llantas}.")

    def color_coche(self):
        print(f"\nEl coche es de color {self.color}.")

    def precio_coche(self):
        print(f"\nEl coche cuesta {self.precio}.\n\n")

#cream els objectes amb classes
class Renault(Coche):
    def __init__(self, marca, llantas, color, precio):
        super().__init__(marca, llantas, color, precio)

class BMW(Coche):
    def __init__(self, marca, llantas, color, precio):
        super().__init__(marca, llantas, color, precio)

class Toyota(Coche):
    def __init__(self, marca, llantas, color, precio):
        super().__init__(marca, llantas, color, precio)

class Opel(Coche):
    def __init__(self, marca, llantas, color, precio):
        super().__init__(marca, llantas, color, precio)

def pex4():
    #li pasem les dades de cada objecte a la llista
    l =[Renault("Renault Clio", "18 pulgadas", "verde metalizado", "25.000€"), BMW("BMW M2", "20 pulgadas", "azul mate", "50000€"), Toyota("Toyota Supra", "18 pulgadas", "rojo", "35000€"), Opel("Opel Corsa", "14 pulgadas", "negro", "20000€")]
    for e in l:
        #li aplica les seguents funcions als elements de la llista
        e.marca_coche()
        e.tipo_llantas()
        e.color_coche()
        e.precio_coche()
