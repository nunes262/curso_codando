from domain.models.database_settings import DatabaseSettings
from domain.services.database_controller_factory import DatabaseControllerFactory

class ConnectDatabaseFactory:
    def call(self, database_settings: DatabaseSettings) -> DatabaseControllerFactory:
        raise NotImplementedError()