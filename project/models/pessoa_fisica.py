from abc import ABC
from project.models.endereco import Endereco
from project.models.enums.genero import Genero
from project.models.enums.estado_civil import Estado_civil
from project.models.pessoa import Pessoa

class Pessoa_fisica(ABC,Pessoa):
    def __init__(self, genero: Genero, estado_civil: Estado_civil, data_de_nascimento: str,nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, endereco)
        
        
        self.genero = genero
        self.estado_civil = estado_civil
        self.data_de_nascimento = data_de_nascimento

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nGênero: {self.genero.value}"
            f"\nEstado Cívil: {self.estado_civil.value}"
            f"\nData de Nascimento: {self.data_de_nascimento}"
        )
