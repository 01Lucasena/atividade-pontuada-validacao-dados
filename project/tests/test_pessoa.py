import pytest
from project.models.pessoa import Pessoa
from project.models.endereco import Endereco
from project.models.enums.unidade_federativa import Unidade_federativa


@pytest.fixture
def pessoa_valida():
    pessoa1 = Pessoa(101,"Lucas","0000000000","lucas@email.com",
                     Endereco("Rua A","01","Apt 02","0000","Salvador", Unidade_federativa.BAHIA))
    return pessoa1

def test_pessoa_id_valido(pessoa_valida):
    assert pessoa_valida.id == 101

def test_pessoa_id_tipo_invalido_retorna_mensagem(pessoa_valida):
    with pytest.raises(TypeError,match="ID deve ser um número inteiro."):
        Pessoa("abc","Lucas","0000000000","lucas@email.com",
                     Endereco("Rua A","01","Apt 02","0000","Salvador", Unidade_federativa.BAHIA))

def test_pessoa_nome_valido(pessoa_valida):
    assert pessoa_valida.nome == "Lucas"

def test_pessoa_nome_vazio_retorna_mensagem(pessoa_valida):
    with pytest.raises(TypeError,match="Nome não deve ficar vazio."):
        Pessoa(101,"","0000000000","lucas@email.com",
                     Endereco("Rua A","01","Apt 02","0000","Salvador", Unidade_federativa.BAHIA))
        
def test_pessoa_nome_caracter_invalido_retorna_mensagem(pessoa_valida):
    with pytest.raises(TypeError,match="Caracteres inválidos foram inseridos."):
        Pessoa(101,"111","0000000000","lucas@email.com",
                     Endereco("Rua A","01","Apt 02","0000","Salvador", Unidade_federativa.BAHIA))