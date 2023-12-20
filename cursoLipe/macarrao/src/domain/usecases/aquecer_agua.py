from domain.models import PanelaComAgua
from domain.services import FogoFactory, PanelaFervendoFactory


class AquecerAgua:
    def __init__(
        self,
        fogo_factory: FogoFactory,
        panela_fervendo_factory: PanelaFervendoFactory,
    ):
        self.fogo_factory = fogo_factory
        self.panela_fervendo_factory = panela_fervendo_factory

    def call(self, panela_com_agua: PanelaComAgua):
        fogo = self.fogo_factory.call()
        macarrao_factory = self.panela_fervendo_factory.call(
            fogo, panela_com_agua
        )
