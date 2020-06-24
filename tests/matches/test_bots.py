import pytest

from executor.python import PythonFileExecutor
from games.matches.bot.MatchesBot import MatchesBot


def mbot_from_py(filename: str):
    executor = PythonFileExecutor(filename)
    return MatchesBot(executor)


@pytest.mark.asyncio
async def test_crash():
    bot = mbot_from_py("bots_for_testing/matches/testing_crash.py")
    with pytest.raises(Exception):
        await bot.turn(10)


@pytest.mark.asyncio
async def test_inc_turn():
    bot = mbot_from_py("bots_for_testing/matches/testing_incorrect_turn.py")
    assert await bot.turn(10) == -1


@pytest.mark.asyncio
async def test_inc_turn_2():
    bot = mbot_from_py("bots_for_testing/matches/testing_incorrect_turn_2.py")
    for i in range(1, 16):
        assert await bot.turn(10) == 11


@pytest.mark.asyncio
async def test_bot():
    bot = mbot_from_py("bots_for_testing/matches/testing_bot.py")
    for i in range(1, 16):
        if i % 4 != 0:
            assert await bot.turn(i) == i % 4
