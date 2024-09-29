import pytest

from project.models.advogado import Advogado
from project.models.endereco import Endereco
from project.models.enums.setor import Setor
from project.models.enums.genero import Genero
from project.models.enums.estado_civil import Estado_civil
from project.models.enums.unidade_federativa import Unidade_federativa


@pytest.fixture
def advogado_valido():
    return Advogado("00000000","00.000.000-0","000.000.000-00","000",Setor.JURIDICO,9000,Genero.MASCULINO,Estado_civil.DIVORCIADO,
                    "18/10/1999","Lucas Sena","0000-0000","lucas@email.com",
                    Endereco("Rua A","001","Apt 002","Salvador",Unidade_federativa.BAHIA)
                    )

def test_advogado_oab_valido(advogado_valido):
    assert advogado_valido.oab == "00000000"

def test_advogado_rg_valido(advogado_valido):
    assert advogado_valido.rg == "00.000.000-0"

def test_advogado_cpf_valido(advogado_valido):
    assert advogado_valido.cpf == "000.000.000-00"

def test_advogado_matricula_valido(advogado_valido):
    assert advogado_valido.matricula == "000"

def test_advogado_setor_valido(advogado_valido):
    assert advogado_valido.setor == Setor.JURIDICO

def test_advogado_salario_valido(advogado_valido):
    assert advogado_valido.salario == 9000

def test_advogado_genero_valido(advogado_valido):
    assert advogado_valido.genero == Genero.MASCULINO

def test_advogado_estado_civil_valido(advogado_valido):
    assert advogado_valido.estado_civil == Estado_civil.DIVORCIADO

def test_advogado_data_de_nascimento_valida(advogado_valido):
    assert advogado_valido.data_de_nascimento == "18/10/1999"

def test_advogado_nome_valido(advogado_valido):
    assert advogado_valido.nome == "Lucas Sena"

def test_advogado_telefone_valido(advogado_valido):
    assert advogado_valido.telefone == "0000-0000"

def test_advogado_email_valido(advogado_valido):
    assert advogado_valido.email == "lucas@email.com"

def test_advogado_endereco_logradouro_valido(advogado_valido):
    assert advogado_valido.endereco.logradouro == "Rua A"

def test_advogado_endereco_numero_valido(advogado_valido):
    assert advogado_valido.endereco.numero == "001"

def test_advogado_endereco_complemento_valido(advogado_valido):
    assert advogado_valido.endereco.complemento == "Apt 002"

def test_advogado_endereco_cidade_valido(advogado_valido):
    assert advogado_valido.endereco.cidade == "Salvador"

def test_advogado_endereco_unidade_federativa_valido(advogado_valido):
    assert advogado_valido.endereco.unidade_federativa == Unidade_federativa.BAHIA