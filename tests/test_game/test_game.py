import pytest

from bot import Bot
from executor import Executor
from game import Game, UNINIT


def test_create():
    ex = Executor("foo")
    bot = Bot(ex)
    game = Game([bot])
    assert game.state == UNINIT
    assert game.current_bot == 0
    assert game.bots == [bot]


@pytest.mark.asyncio
async def test_interface():
    ex = Executor("foo")
    bot = Bot(ex)
    game = Game([bot])
    with pytest.raises(NotImplementedError):
        await game.play()
    with pytest.raises(NotImplementedError):
        await game.turn()
    with pytest.raises(NotImplementedError):
        game.repr_json()
    with pytest.raises(NotImplementedError):
        game.field_json()
    with pytest.raises(NotImplementedError):
        game.game_name_json()
    with pytest.raises(NotImplementedError):
        game.logs_json()
