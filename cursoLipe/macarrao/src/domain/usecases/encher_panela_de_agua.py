from domain.models import PanelaComAgua
from domain.services import PegarPanelaFactory, ColocarAguaNaPanelaFactory


class EncherPanelaDeAgua:
    def __init__(
        self,
        pegar_panela_factory: PegarPanelaFactory,
        colocar_agua_na_panela_factory: ColocarAguaNaPanelaFactory
    ):
        self.pegar_panela_factory = pegar_panela_factory
        self.colocar_agua_na_panela_factory = colocar_agua_na_panela_factory

    def call(self) -> PanelaComAgua:
        panela = self.pegar_panela_factory.call()
        return self.colocar_agua_na_panela_factory.call(panela)
        
