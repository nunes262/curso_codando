from domain.models.database_settings import DatabaseSettings
from domain.services.connect_database_factory import ConnectDatabaseFactory
from domain.services.database_controller import DatabaseController

class GetDatabaseController:
    def __init__(self, connect_database_factory: ConnectDatabaseFactory):
        self.connect_database_factory = connect_database_factory

    def call(self, database_settings: DatabaseSettings) -> DatabaseController:
       database_controller_factory = self.connect_database_factory.call(database_settings)
       database_controller = database_controller_factory.call()
       return database_controller