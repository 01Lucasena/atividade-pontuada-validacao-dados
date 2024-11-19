from abc import ABC
from project.models.endereco import Endereco
from project.models.enums.estado_civil import Estado_civil
from project.models.enums.genero import Genero
from project.models.pessoa_fisica import Pessoa_fisica
from project.models.enums.setor import Setor


class Funcionario(Pessoa_fisica,ABC):
    def __init__(self, rg: str, cpf: str, matricula: str, setor: Setor, salario: float, genero: Genero, estado_civil: Estado_civil, 
                 data_de_nascimento: str, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        super().__init__(genero, estado_civil, data_de_nascimento, nome, telefone, email, endereco)

        self.cpf = cpf
        self.rg = rg
        self.matricula = matricula
        self.setor = setor
        self.salario = self._verificar_salario(salario)

    def __str__(self) -> str:
        return (
            super().__str__() +
            f"\nCPF: {self.cpf}"
            f"\nRG: {self.rg}"
            f"\nMatrícula: {self.matricula}"
            f"\nSetor: {self.setor}"
            f"\nSalário: {self.salario}"
            )

    def _verificar_cpf(self, cpf):
        self._verificar_cpf_tamanho(cpf)
        self.cpf = cpf
        return self.cpf

    def _verificar_rg(self, rg):
        self._verificar_rg_tamanho(rg)
        self.rg = rg
        return self.rg
    
    def _verificar_cpf_tamanho(cpf):
        if len(cpf) > 11:
            raise ValueError("CPF deve ter pelo menos 11 dígitos")
    
    def _verificar_rg_tamanho(rg):
        if len(rg) > 10:
            raise ValueError("RG deve ter pelo menos 10 dígitos")
        
    def _verificar_id(self, id):
        return super()._verificar_id(id)
    
    def _verificar_nome(self, nome):
        return super()._verificar_nome(nome)