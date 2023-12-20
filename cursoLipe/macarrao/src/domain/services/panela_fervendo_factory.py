from domain.models import Fogo, PanelaComAgua
from domain.services import MacarraoFactory


class PanelaFervendoFactory:
    def call(self, fogo: Fogo, panela_com_agua: PanelaComAgua) -> MacarraoFactory:
        raise NotImplementedError()