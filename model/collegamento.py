from dataclasses import dataclass


@dataclass
class Collegamento:
    id_filiale_1: int
    id_filiale_2: int
    importo_medio: float