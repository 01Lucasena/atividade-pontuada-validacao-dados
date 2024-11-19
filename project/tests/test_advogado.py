import pytest
from project.models.advogado import Advogado
from project.models.endereco import Endereco
from project.models.enums.unidade_federativa import Unidade_federativa
from project.models.enums.setor import Setor
from project.models.enums.genero import Genero
from project.models.enums.estado_civil import Estado_civil

@pytest.fixture
def criar_endereco():
    return Endereco(
        "rua a",  
        "01",     
        "casa branca",  
        "1234567",
        "Salvador",
        Unidade_federativa.BAHIA  
    )

@pytest.fixture
def criar_advogado(criar_endereco):
    return Advogado(
        "123456789",
        "12345678900",
        "123456789012",
        "1234567890",
        Setor.JURIDICO,
        10000.00,
        Genero.MASCULINO,
        Estado_civil.CASADO,
        "10.10.90",
        "João",
        "999999999",
        "joao@email.com",
        criar_endereco
    )

def test_advogado_oab(criar_advogado):
    assert criar_advogado.oab == "123456789"
