from Repositorios.RepositorioPermiso import RepositorioPermiso
from Modelos.Permiso import Permiso
class ControladorPermiso():
    def __init__(self):
        self.repositorioPermiso= RepositorioPermiso()
        print("Creando ControladorPermiso")
    def index(self):
        print("Listar todos los permisos")
        return self.repositorioPermiso.findAll()

    def create(self, elpermiso):
        print("Crear un estudiante")
        nuevoPermiso = Permiso(elpermiso)
        return self.repositorioPermiso.save(nuevoPermiso)

    def show(self, id):
        elpermiso = Permiso(self.repositorioPermiso.findById(id))
        return elpermiso.__dict__

    def update(self, id, elpermiso):
        permisoActual = Permiso(self.repositorioPermiso.findById(id))
        permisoActual.url=elpermiso["url"]
        permisoActual.metodo=elpermiso["metodo"]


    def delete(self, id):
        return self.repositorioPermiso.delete(id)
