class Persona():
    
    def __init__(self, codigo: int, nombres: str, apellidos: str, tieneVisa: bool, activo:bool):
        self.codigo = codigo
        self.nombres = nombres
        self.apellidos = apellidos
        self.tieneVisa = tieneVisa
        self.activo = activo