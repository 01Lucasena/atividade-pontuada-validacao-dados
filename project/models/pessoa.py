from abc import ABC
from project.models.endereco import Endereco

class Pessoa(ABC):
    def __init__(self, id: int, nome: str, telefone: str , email: str, endereco: Endereco) -> None:

        
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def __str__(self) -> str:
        return (
            f"\nID: {self.id}"
            f"\nNome: {self.nome}"
            f"\nTelefone: {self.telefone}"
            f"\nEmail: {self.email}"
            f"\nEndereco: {self.endereco}"
        )
    
    def _verificar_id(self, id):
        self._verificar_id_invalido(id)
        self._verificar_id_negativo(id)
        
        self.id = id
        return self.id
    
    def _verificar_nome(self,nome):
        self._verificar_nome_invalido(nome)
        self._verificar_nome_vazio(nome)

        self.nome = nome
        return self.nome
    
    def _verificar_id_invalido(id):

        if not isinstance(id, int):
            raise TypeError("ID deve ser um número inteiro.")

    def _verificar_id_negativo(id):

        if id < 0:
            raise ValueError("ID não deve ser negativo.")

    def _verificar_nome_invalido(nome):

        if not isinstance(nome, str):
            raise ValueError("Nome deve conter apenas letras.")

    def _verificar_nome_vazio(nome):

        if not nome.strip():
            raise ValueError("Nome não deve ficar vazio.")