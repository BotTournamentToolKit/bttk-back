import pytest

from executor.python import PythonFileExecutor
from games.matches.bot.MatchesBot import MatchesBot
from games.matches.game.MatchesGame import MatchesGame
from game import UNINIT


def mbot_from_py(filename: str):
    executor = PythonFileExecutor(filename)
    return MatchesBot(executor)


def test_create():
    bot = mbot_from_py("foo")
    game = MatchesGame([bot, bot])
    assert game.state == UNINIT
    assert game.current_bot == 0
    assert game.bots == [bot, bot]


@pytest.mark.asyncio
async def test_game_true_bot():
    bot = mbot_from_py("bots_for_testing/matches/testing_bot.py")
    game = MatchesGame([bot, bot])
    for i in range(1, 16):
        with pytest.raises(Exception):
            await game.play(i)


@pytest.mark.asyncio
async def test_game_crash_bot():
    bot = mbot_from_py("bots_for_testing/matches/testing_crash.py")
    game = MatchesGame([bot, bot])
    with pytest.raises(Exception):
        await game.play(15)


@pytest.mark.asyncio
async def test_game_not_true_bot():
    bot = mbot_from_py("bots_for_testing/matches/testing_incorrect_turn.py")
    game = MatchesGame([bot, bot])
    for i in range(1, 16):
        with pytest.raises(Exception):
            await game.play(i)


@pytest.mark.asyncio
async def test_game_not_true_bot_2():
    bot = mbot_from_py("bots_for_testing/matches/testing_incorrect_turn_2.py")
    game = MatchesGame([bot, bot])
    for i in range(1, 16):
        with pytest.raises(Exception):
            await game.play(i)


@pytest.mark.asyncio
async def test_game_recur_bot():
    bot = mbot_from_py("bots_for_testing/matches/testing_bot_time_limit.py")
    game = MatchesGame([bot, bot])
    with pytest.raises(Exception):
        await game.play(15)
