from project.models.enums.unidade_federativa import Unidade_federativa


class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str, unidade_federativa: Unidade_federativa) -> None:
        
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = self._verificar_cep(cep)
        self.cidade = cidade
        self.unidade_federativa = unidade_federativa


    def __str__(self) -> str:
        return (
            f"\nLogradouro: {self.logradouro}"
            f"\nNúmero: {self.numero}"
            f"\nComplemento: {self.complemento}"
            f"\nCEP: {self.cep}"
            f"\nCidade: {self.cidade}"
            f"\nUnidade Federativa: {self.unidade_federativa.texto}"
        )
    
    def _verificar_cep(self,cep):
        
        self._verificar_cep_tamanho(cep)
        self.cep = cep
        return self.cep
    
    def _verificar_cep_tamanho(cep):

        if len(cep) > 8:
            raise ValueError("Cep deve ter no mínimo 8 dígitos.")