import pytest

from bot import Bot
from executor import Executor


def test_create():
    ex = Executor("foo")
    bot = Bot(ex)
    assert bot.executor == ex


@pytest.mark.asyncio
async def test_interface():
    ex = Executor("foo")
    bot = Bot(ex)
    with pytest.raises(NotImplementedError):
        await bot.turn(None)
