from dataclasses import dataclass

@dataclass
class Macarrao:
    tipo: str
    quantidade: int
    tempo_de_cozimento: int
    cozido: bool