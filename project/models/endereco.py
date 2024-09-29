from project.models.enums.unidade_federativa import Unidade_federativa

class CepError(Exception):
    pass

class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str, unidade_federativa: Unidade_federativa) -> None:
        
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.unidade_federativa = unidade_federativa

        def _verificar_cep(self, cep):
            if len(cep) > 10:
                raise CepError("CEP inválido.")
        return cep

    def __str__(self) -> str:
        return (
            f"\nLogradouro: {self.logradouro}"
            f"\nNúmero: {self.numero}"
            f"\nComplemento: {self.complemento}"
            f"\nCEP: {self.cep}"
            f"\nCidade: {self.cidade}"
            f"\nUnidade Federativa: {self.unidade_federativa.value}"
        )