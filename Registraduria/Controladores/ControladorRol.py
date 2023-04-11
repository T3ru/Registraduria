from Modelos.Rol import Rol
from Repositorios.RepositorioRol import RepositorioRol



class ControladorRol():
    """
    constructor que permite llevar a cabo la creacion de instancias del controlador.
    """
    def __init__(self):
        self.repositorioRol = RepositorioRol()
        print("Creando ControladorRol")

    def index(self):
        print("Listar todos los roles")
        return self.repositorioRol.findAll()

    def create(self, elRol):
        print("Crear un rol")
        nuevoRol = Rol(elRol)
        return self.repositorioRol.save(nuevoRol)

    def show(self, id):
        elRol = Rol(self.repositorioRol.findById(id))
        return elRol.__dict__

    def update(self, id, elRol):
        rolActual = Rol(self.repositorioRol.findById(id))
        rolActual.nombre = elRol["nombre"]
        return self.repositorioRol.save(rolActual)

    def delete(self, id):
        print("Elimiando rol con id ", id)
        return self.repositorioRol.delete(id)