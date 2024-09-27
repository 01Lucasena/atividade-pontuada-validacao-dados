from project.models.enums.unidade_federativa import Unidade_federativa

class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str, unidade_federativa: Unidade_federativa) -> None:
        
        if not numero.strip():
            raise TypeError("Número não deve ficar vazio.")

        if not self._is_valid(numero):
            raise TypeError("Apenas números são permitidos.")
        
        if not logradouro.strip():
            raise TypeError("Logradouro não deve ficar vazio.")
        
        if not complemento.strip():
            raise TypeError("Complemento não deve ficar vazio.")
        
        if not self._is_valid(cep):
            raise TypeError("Apenas números são permitidos.")
        
        if not cidade.strip():
            raise TypeError("Cidade não deve ficar vazio.")
        
        if self._is_valid(cidade):
            raise TypeError("Caracteres inválidos foram inseridos.")
        
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.unidade_federativa = unidade_federativa
    
    def _is_valid(self,numero):
        return numero.isdigit()
    
    def _is_valid(self,cep):
        return cep.isdigit()
    
    def _is_valid(self,cidade):
        return cidade.isdigit()
       

    def __str__(self) -> str:
        return (
            f"\nLogradouro: {self.logradouro}"
            f"\nNúmero: {self.numero}"
            f"\nComplemento: {self.complemento}"
            f"\nCEP: {self.cep}"
            f"\nCidade: {self.cidade}"
            f"\nUnidade Federativa: {self.unidade_federativa.value}"
        )