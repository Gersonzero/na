class Coche:
    def __init__(self, marca, modelo, anio):
        # Constructor: inicializa los atributos del coche
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.velocidad = 0

    @property
    def descripcion(self):
        # Propiedad: devuelve una descripción del coche
        return f"{self.marca} {self.modelo} {self.anio}"

    def acelerar(self, incremento):
        # Método: aumenta la velocidad del coche
        self.velocidad += incremento
        print(f"El coche ahora va a {self.velocidad} km/h")

    def frenar(self, decremento):
        # Método: reduce la velocidad del coche
        self.velocidad -= decremento
        if self.velocidad < 0:
            self.velocidad = 0
        print(f"El coche ahora va a {self.velocidad} km/h")
