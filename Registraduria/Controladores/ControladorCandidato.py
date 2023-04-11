from Modelos.Candidato import Candidato
from Repositorios.RepositorioCandidato import RepositorioCandidato


class ControladorCandidato():
   """
   constructor que permite llevar a cabo la creacion de instancias del controlador.
   """
   def __init__(self) -> object:
       self.repositorioCandidato = RepositorioCandidato()
       print("Creando Controlador Candidato")


   def index(self):
       print("Listar Los Candidatos")
       return self.repositorioCandidato.findAll()

   def create(self, elCandidato):
       print("Crear Candidato")
       nuevoCandidato = Candidato(elCandidato)
       return self.repositorioEstudiante.save(nuevoCandidato)

   def show(self, id):
       print("Mostrando Candidato Con id ", id)
       elCandidato = Candidato(self.repositorioCandidato.findById(id))
       return elCandidato.__dict__

   def update(self, id, elCandidato):
       print("Actualizando Candidato con id ", id)
       CandidatoActual = Candidato(self.repositorioCandidato.findById(id))
       CandidatoActual.cedula = elCandidato["Cedula"]
       CandidatoActual.no_resolucion = elCandidato["No resolucion"]
       CandidatoActual.nombre = elCandidato["Nombre"]
       CandidatoActual.apellido = elCandidato["Apellido"]
       return self.repositorioCandidato.save(CandidatoActual)

   def delete(self, id):
       print("Eliminando Candidato Con id ", id)
       return self.repositorioCandidato.delete(id)
