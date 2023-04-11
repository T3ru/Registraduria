from Modelos.Usuario import Usuario
from Repositorios.RepositorioUsuario import RepositorioUsuario


class ControladorUsuario():
    """
    constructor que permite llevar a cabo la creacion de instancias del controlador.
    """
    def __init__(self):
        self.repositorioUsuario = RepositorioUsuario()
        print("Creando ControladorUsuario")

    def index(self):
        print("Listar todos los Usuarios")
        return self.repositorioUsuario.findAll()

    def create(self, elUsuario):
        print("Crear un usuario")
        nuevoUsuario = Usuario(elUsuario)
        return self.repositorioUsuario.save(nuevoUsuario)

    def show(self, id):
        elUsuario = Usuario(self.repositorioUsuario.findById(id))
        return elUsuario.__dict__

    def update(self, id, elUsuario):
        usuarioActual = Usuario(self.repositorioUsuario.findById(id))
        usuarioActual.seudonimo = elUsuario["seudonimo"]
        usuarioActual.correo = elUsuario["correo"]
        usuarioActual.contrseña = elUsuario["contraseña"]
        return self.repositorioUsuario.save(usuarioActual)

    def delete(self, id):
        print("Elimiando usuario con id ", id)
        return self.repositorioUsuario.delete(id)
