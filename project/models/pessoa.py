from abc import ABC
from project.models.endereco import Endereco

class Pessoa(ABC):
    def __init__(self,id: int, nome: str, telefone: str , email: str, endereco: Endereco) -> None:

        self.id = self._verificar_id(id)
        self.nome = self._verificar_nome(nome)
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def __str__(self) -> str:
        return (
            f"\nNome: {self.nome}"
            f"\nTelefone: {self.telefone}"
            f"\nEmail: {self.email}"
            f"\nEndereco: {self.endereco}"
        )
    
    def _verificar_nome(self,nome):
        self._verificar_nome_invalido(nome)
        self._verificar_nome_vazio(nome)
        self.nome = nome
        
        return self.nome

    def _verificar_id(self, id):
        self._verificar_id_invalido(id)
        self.id = id

        return self.id

    def _verificar_nome_invalido(nome):
        if not isinstance(nome, str):
            raise ValueError("Nome deve conter apenas letras.")

    def _verificar_nome_vazio(nome):

        if not nome.strip():
            raise ValueError("Nome não deve ficar vazio.")
        
    def _verificar_id_invalido(id):
        if not isinstance(id, int):
            raise ValueError("ID inválido.")