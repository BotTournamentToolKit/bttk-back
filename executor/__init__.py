class Executor(object):
    file_path: str

    def __init__(self, path: str):
        self.file_path = path

    async def turn(self, field: str) -> str:
        raise NotImplementedError()
