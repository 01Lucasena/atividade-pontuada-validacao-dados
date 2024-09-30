from project.models.endereco import Endereco
from project.models.enums.estado_civil import Estado_civil
from project.models.enums.genero import Genero
from project.models.pessoa_fisica import Pessoa_fisica

class Cliente(Pessoa_fisica):
    def __init__(self,protocolo_atendimento: int, genero: Genero, estado_civil: Estado_civil, data_de_nascimento: str, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        super().__init__(genero, estado_civil, data_de_nascimento, nome, telefone, email, endereco)
        
        self.protocolo_atendimento = protocolo_atendimento

    def __str__(self) -> str:
        return (
            (super().__str__()) +
            f"\nProtocolo do atendimento: {self.protocolo_atendimento}"
        )