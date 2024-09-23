from abc import ABC
from project.models.pessoa import Pessoa

class Pessoa_juridica(ABC):
    def __init__(self) -> None:
        super().__init__()