class Executor(object):
    file_path: str
    timeout: float

    def __init__(self, path: str, timeout: float = 5.0):
        self.file_path = path
        self.timeout = timeout

    async def turn(self, field: str) -> str:
        raise NotImplementedError()
