from abc import ABC, abstractmethod

class Exame:
    def __init__(self, tipo:str):
        self.tipo = tipo

class AprovaExame(ABC):
    @abstractmethod
    def aprovar_solicitacao_exame(self, exame):
        pass
    @abstractmethod
    def verifica_condicoes_exame(self, exame):
        pass
        
class AprovaExameRaioX(AprovaExame):
    def aprovar_solicitacao_exame(self, exame: Exame) -> None:
        if self.verifica_condicoes_exame(exame):
            print("Exame sanguíneo aprovado!")

    def verifica_condicoes_exame(self, exame: Exame) -> bool:
        pass

        
class AprovaExameSangue(AprovaExame):
    def aprovar_solicitacao_exame(self, exame: Exame) -> None:
        if self.verifica_condicoes_exame(exame):
            print("Raio-X aprovado!")

    def verifica_condicoes_exame(self, exame:Exame) -> bool:
        pass




exame_sangue = Exame('Sangue')
exame_raio_x = Exame('Raio-x')

aprovador_sangue = AprovaExameSangue()
aprovador_raio_x = AprovaExameRaioX()

aprovador_raio_x.aprovar_solicitacao_exame(exame_raio_x)
aprovador_sangue.aprovar_solicitacao_exame(exame_sangue)
