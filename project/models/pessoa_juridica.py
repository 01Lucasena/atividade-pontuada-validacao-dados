from abc import ABC
from project.models.endereco import Endereco
from project.models.pessoa import Pessoa

class Pessoa_juridica(Pessoa,ABC):
    def __init__(self,cnpj: str, inscricao_estadual: str, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, endereco)
    
        self.cnpj = cnpj
        self.inscricao_estadual = inscricao_estadual