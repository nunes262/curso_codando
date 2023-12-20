from dataclasses import dataclasses

@dataclasses
class DatabaseSettings:
    host: str
    port: int
    user: str
    password: str
    databse_name: str