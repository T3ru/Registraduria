from Modelos.Partido import Partido
from Repositorios.RepositorioPartido import RepositorioPartido


class ControladorPartido():

    def __init__(self):
        self.repositorioPartido= RepositorioPartido()
        print("Creando ControladorPartido")

    def index(self):
        print("Listar todos los partidos")
        return self.repositorioPartido.findAll()

    def create(self, elPartido):
        print("Crear un partido")
        nuevoPartido = Partido(elPartido)
        return self.repositorioPartido.save(nuevoPartido)

    def show(self, id):
        elPartido = Partido(self.repositorioPartido.findById(id))
        return elPartido.__dict__

    def update(self, id, elPartido):
        partidoActual = elPartido(self.repositorioPartido.findById(id))
        partidoActual.url=elPartido["Nombre"]
        partidoActual.metodo=elPartido["Lema"]
        return self.repositorioPartido.save(partidoActual)

    def delete(self, id):
        return self.repositorioPartido.delete(id)
