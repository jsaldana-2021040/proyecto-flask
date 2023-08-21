class Paginacion():
    def __init__(self, totalElementos: int, elementos: list, paginaActual: int=1, elementosPorPagina: int=10):
        self.totalElementos = totalElementos
        self.elementos = elementos
        self.paginaActual = paginaActual
        self.elementosPorPagina = elementosPorPagina
        self.totalPaginas: int = float(totalElementos / elementosPorPagina).__ceil__()