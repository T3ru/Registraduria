from Modelos.Candidato import Candidato
from Modelos.Mesa import Mesa
from Modelos.Resultado import Resultado
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioResultado import RepositorioResultado


class ControladorResultado():
    def _init_(self):
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioMesa = RepositorioMesa()
        self.repositorioResultado = RepositorioResultado()

    def index(self):
        return self.repositorioResultado.findAll()


    def create(self, infoResultado, id_mesa, id_candidato):
        nuevoResultado = Resultado(infoResultado)
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        nuevoResultado.mesa= laMesa
        nuevoResultado.candidato = elCandidato
        return self.repositorioResultado.save(nuevoResultado)

    def show(self, id):
        elResultado = Resultado(self.repositorioResultado.findById(id))
        return elResultado._dict_


    def update(self, id, infoResultado, id_mesa, id_candidato):
        elResultado = Resultado(self.repositorioResultado.findById(id))
        elResultado.numero = infoResultado["Número de mesa"]
        elResultado.candidato = infoResultado["Candidato"]
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        elResultado.mesa = laMesa
        elResultado.candidato = elCandidato
        return self.repositorioInscripcion.save(elResultado)

    def delete(self, id):
        return self.repositorioResultado.delete(id)