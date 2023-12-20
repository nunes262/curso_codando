from domain.models import Macarrao


class MacarraoFactory:
    def call(self, macarrao_cru: Macarrao) -> Macarrao:
        raise NotImplementedError()