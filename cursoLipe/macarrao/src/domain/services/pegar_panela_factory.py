from domain.models import Panela


class PegarPanelaFactory:
    def call(self) -> Panela:
        raise NotImplementedError()