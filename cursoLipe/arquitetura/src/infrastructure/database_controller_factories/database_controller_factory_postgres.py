from domain.services.database_controller import DatabaseController
from domain.services.database_controller_factory import DatabaseControllerFactory


class DatabaseControllerFactoryPostgres(DatabaseControllerFactory):
    def call(self) -> DatabaseController:
        pass