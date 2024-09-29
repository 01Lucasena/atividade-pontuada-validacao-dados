from project.models.endereco import Endereco
from project.models.pessoa_juridica import Pessoa_juridica

class prestacao_servico(Pessoa_juridica):
    def __init__(self,contrato_inicio: str, contrato_fim: str, cnpj: str, inscricao_estadual: str, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        super().__init__(cnpj, inscricao_estadual, nome, telefone, email, endereco)

        self.contrato_inicio = contrato_inicio
        self.contrato_fim = contrato_fim

    def _verificar_id(self, id):
        return super()._verificar_id(id)
    
    def _verificar_nome(self, nome):
        return super()._verificar_nome(nome)
    
    def _verificar_cep(self, cep):
        return super()._verificar_cep(cep)
    
    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\ninício do contrato: {self.contrato_inicio}"
            f"\nFim do contrato: {self.contrato_fim}"
        )
