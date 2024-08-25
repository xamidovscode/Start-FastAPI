from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

class Database:

    @classmethod
    def get_database(cls, app):
        register_tortoise(
            app=app,
            db_url="sqlite://to.db",
            add_exception_handlers=True,
            generate_schemas=True,
            modules={"modules": ["app.sections.common.models"]}
        )

database = Database()
