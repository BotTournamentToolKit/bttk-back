from pathlib import Path


class Executor(object):
    file_name: str
    timeout: float
    parent_path: str
    file_name: str

    def __init__(self, path: str, timeout: float = 5.0):
        self.file_name = path
        self.timeout = timeout
        pth = Path(self.file_name)
        self.parent_path = str(pth.parent)
        self.file_name = str(pth.name)

    async def turn(self, field: str) -> str:
        raise NotImplementedError()
