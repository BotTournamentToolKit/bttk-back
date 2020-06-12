from executor import Executor
from typing import Any


class Bot(object):
    executor: Executor

    def __init__(self, executor):
        self.executor = executor

    async def turn(self, field: Any) -> Any:
        raise NotImplementedError()
