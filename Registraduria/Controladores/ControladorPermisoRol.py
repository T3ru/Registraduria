from Modelos.Permiso import Permiso
from Modelos.PermisoRol import PermisoRol
from Modelos.Rol import Rol
from Repositorios.RepositorioPermiso import RepositorioPermiso
from Repositorios.RepositorioPermisoRol import RepositorioPermisoRol
from Repositorios.RepositorioRol import RepositorioRol


class ControladorPermisoRol():
    def __init__(self):
        self.repositorioPermiso = RepositorioPermiso()
        self.repositorioRol = RepositorioRol()
        self.repositorioPermisoRol = RepositorioPermisoRol()
        print("Creando ControlPermisoRol")

    def index(self):
        print("Listar todos los permisos de los roles")
        return self.repositorioPermisoRol.findAll()


    """
    Asignacion Rol y Permiso a PermisoRol
    """

    def create(self, infoPermisoRol, id_permiso,id_rol):
        print("Crear un Permiso de rol")
        nuevaPermisoRol = PermisoRol(infoPermisoRol)
        elRol = Rol(self.repositorioRol.findById(id_rol))
        elPermiso = Permiso(self.repositorioPermiso.findById(id_permiso))
        nuevaPermisoRol.rol= elRol
        nuevaPermisoRol.permiso= elPermiso
        return self.repositorioPermisoRol.save(nuevaPermisoRol)

    def show(self, id):
        elPermisoRol =PermisoRol(self.repositorioPermisoRol.findById(id))

        return elPermisoRol.__dict__

    """
    Modificación de inscripción (estudiante y materia)
    """

    def update(self, id,id_permiso,id_rol):
        elPermisoRol = PermisoRol(self.repositorioPermisoRol.findById(id))
        elRol = Rol(self.repositorioRol.findById(id_rol))
        elPermiso = Permiso(self.repositorioPermiso.findById(id_permiso))
        elPermisoRol.rol= elRol
        elPermisoRol.permiso = elPermiso
        return self.repositorioPermisoRol.save(elPermisoRol)

    def delete(self, id):
        print("Elimiando un permiso de rol con id ", id)
        return self.repositorioPermisoRol.delete(id)
