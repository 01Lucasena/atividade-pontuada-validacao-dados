from abc import ABC
from project.models.endereco import Endereco

class Pessoa(ABC):
    def __init__(self,id: int, nome: str, telefone: str , email: str, endereco: Endereco) -> None:
        super().__init__()
        
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
    
    '''
    def _verificar_id(self, id):
        if not isinstance(id, int):
            raise TypeError("Dados inválidos foram inseridos.")
        if id < 0:
            raise ValueError("Dados inválidos foram inseridos.")
        return id
    
    def _verificar_nome(self, nome):
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("Nome não deve estar vazio.")
        return nome

    def _verificar_cep(self, cep):
        return super._verificar_cep(cep) 
    '''     

    def __str__(self) -> str:
        return (
            f"\nID: {self.id}"
            f"\nNome: {self.nome}"
            f"\nTelefone: {self.telefone}"
            f"\nEmail: {self.email}"
            f"\nEndereco: {self.endereco}"
        )