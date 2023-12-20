from domain.models.database_settings import DatabaseSettings
from domain.services.connect_database_factory import ConnectDatabaseFactory
from domain.services.database_controller_factory import DatabaseControllerFactory


class ConnectDatabaseFactoryPostgres(ConnectDatabaseFactory):
    def call(self, database_settings: DatabaseSettings) -> DatabaseControllerFactory:
        pass