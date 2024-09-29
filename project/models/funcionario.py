from abc import ABC
from project.models.endereco import Endereco
from project.models.enums.estado_civil import Estado_civil
from project.models.enums.genero import Genero
from project.models.pessoa_fisica import Pessoa_fisica
from project.models.enums.setor import Setor

class RgError(Exception):
    pass

class CpfError(Exception):
    pass

class Funcionario(Pessoa_fisica,ABC):
    def __init__(self, rg: str, cpf: str, matricula: str, setor: Setor, salario: float, genero: Genero, estado_civil: Estado_civil, data_de_nascimento: str, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        super().__init__(genero, estado_civil, data_de_nascimento, nome, telefone, email, endereco)

        self.cpf = self._verificar_cpf(cpf)
        self.rg = self._verificar_rg(rg)
        self.matricula = matricula
        self.setor = setor
        self.salario = self._verificar_salario(salario)

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nCPF: {self.cpf}"
            f"\nRG: {self.rg}"
            f"\nMatrícula: {self.matricula}"
            f"\nSetor: {self.setor.value}"
            f"\nSalário: {self.salario}"
            )
    
    def _verificar_salario(self, salario):
        
        if not isinstance (salario, float):
            raise TypeError("Dados inválidos foram inseridos.")
        
        if salario < 0:
            raise ValueError("Salário não pode ser negativo.")
        return salario
    
    def _verificar_cpf(self, cpf):
        if len(cpf) > 14:
            raise CpfError("CPF inválido.")
        return cpf
    
    def _verificar_rg(self, rg):
        if len(rg) > 12:
            raise RgError("RG inválido.")
        return rg

    def _verificar_id(self, id):
        return super()._verificar_id(id)
    
    def _verificar_nome(self, nome):
        return super()._verificar_nome(nome)

    def __str__(self) -> str:
        return (
            f"\nCPF: {self.cpf}"
            f"\nRG: {self.rg}"
            f"\nMatrícula: {self.matricula}"
            f"\nSetor: {self.setor.value}"
            f"\nSalário: {self.salario}"
        )