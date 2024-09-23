from abc import ABC, abstractmethod
from project.models.endereco import Endereco

class Pessoa(ABC):
    def __init__(self, nome: str, telefone: str , email: str, endereco: Endereco) -> None:
        super().__init__()
        self.nome = nome
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