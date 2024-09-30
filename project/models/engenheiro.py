from project.models.endereco import Endereco
from project.models.enums.estado_civil import Estado_civil
from project.models.enums.genero import Genero
from project.models.enums.setor import Setor
from project.models.funcionario import Funcionario

class Engenheiro(Funcionario):
    def __init__(self,crea: str, rg: str, cpf: str, matricula: str, setor: Setor, salario: float, genero: Genero, estado_civil: Estado_civil, data_de_nascimento: str, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        super().__init__(rg, cpf, matricula, setor, salario, genero, estado_civil, data_de_nascimento, nome, telefone, email, endereco)

        self.crea = crea
    


    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nCREA: {self.crea}"
        )