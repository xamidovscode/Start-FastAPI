from fastapi import FastAPI


async def on_startup() -> None:
    print('SUCCESS')


class Server:
    app: FastAPI

    def __init__(self, app: FastAPI):
        self.app = app

    def get_app(self):
        return self.app