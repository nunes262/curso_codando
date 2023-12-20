from domain.models import Panela, PanelaComAgua

class ColocarAguaNaPanelaFactory:
    def call(self, panela: Panela) -> PanelaComAgua:
        raise NotImplementedError()

