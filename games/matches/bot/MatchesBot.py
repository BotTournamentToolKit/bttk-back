from bot import Bot
from executor.python import PythonFileExecutor


class MatchesBot(Bot):
    executor: PythonFileExecutor

    async def turn(self, field: int) -> int:
        try:
            res = await self.executor.turn(str(field))
        except:
            raise NotImplementedError()
        return int(res)
