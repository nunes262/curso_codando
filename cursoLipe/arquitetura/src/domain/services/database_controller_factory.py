
from domain.services.database_controller import DatabaseController

class DatabaseControllerFactory:
    def call(self) -> DatabaseController:
        raise NotImplementedError()