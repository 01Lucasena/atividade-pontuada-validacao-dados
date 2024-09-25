import pytest
from project.models.endereco import Endereco
from project.models.enums.unidade_federativa import Unidade_federativa

@pytest.fixture
def endereco_valido():
    endereco1 = Endereco("Rua A","01","Apt 02","0000","Salvador", Unidade_federativa.BAHIA)
    return endereco1

def test_endereco_logradouro_valido(endereco_valido):
    assert endereco_valido.logradouro == "Rua A"

def test_endereco_logradouro_vazio_retorna_mensagem(endereco_valido):
    with pytest.raises(ValueError,match="Logradouro não deve ficar vazio."):
        Endereco("","01","Apt 02","0000","Salvador", Unidade_federativa.BAHIA)
    
def test_endereco_numero_valido(endereco_valido):
    assert endereco_valido.numero == "01"

def test_endereco_numero_vazio_retorna_mensagem(endereco_valido):
    with pytest.raises(ValueError,match="Número não deve ficar vazio."):
        Endereco("Rua A","","Apt 02","0000","Salvador", Unidade_federativa.BAHIA)

def test_endereco_caracteres_numero_retorna_mensagem(endereco_valido):
    with pytest.raises(ValueError,match="Apenas números são permitidos."):
        Endereco("Rua A","abc","Apt 02","0000","Salvador", Unidade_federativa.BAHIA)

def test_endereco_complemento_valido(endereco_valido):
    assert endereco_valido.complemento == "Apt 02"

def test_endereco_complemento_vazio_retorna_mensagem(endereco_valido):
    with pytest.raises(ValueError,match="Complemento não deve ficar vazio."):
        Endereco("Rua A","01","","0000","Salvador", Unidade_federativa.BAHIA)

def test_endereco_cep_valido(endereco_valido):
    assert endereco_valido.cep == "0000"

def test_endereco_caracteres_cep_retorna_menssagem(endereco_valido):
    with pytest.raises(ValueError,match="Apenas números são permitidos."):
        Endereco("Rua A","01","Apt 02","abc","Salvador", Unidade_federativa.BAHIA)

def test_endereco_cidade_valido(endereco_valido):
    assert endereco_valido.cidade == "Salvador"

def test_endereco_cidade_vazio_retorna_mensagem(endereco_valido):
    with pytest.raises(ValueError,match="Cidade não deve ficar vazio."):
        Endereco("Rua A","01","Apt 02","0000","", Unidade_federativa.BAHIA)

def test_endereco_cidade_caracteres_retorna_menssagem(endereco_valido):
    with pytest.raises(ValueError,match="Caracteres inválidos foram inseridos."):
        Endereco("Rua A","01","Apt 02","0000","123", Unidade_federativa.BAHIA)

