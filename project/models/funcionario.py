from abc import ABC
from project.models.endereco import Endereco
from project.models.enums.estado_civil import Estado_civil
from project.models.enums.genero import Genero
from project.models.pessoa_fisica import Pessoa_fisica
from project.models.enums.setor import Setor

class Funcionario(Pessoa_fisica,ABC):
    def __init__(self, rg: str, cpf: str, matricula: str, setor: Setor, salario: float, genero: Genero, estado_civil: Estado_civil, data_de_nascimento: str, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        super().__init__(genero, estado_civil, data_de_nascimento, nome, telefone, email, endereco)

        self.cpf = cpf
        self.rg = rg
        self.matricula = matricula
        self.setor = setor
        self.salario = salario