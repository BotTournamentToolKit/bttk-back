from typing import List

from bot import Bot

UNINIT = -1
BOT_TURN = 0
BOT_WON = 1
DISQUALIFIED = 2


class Game(object):
    bots: List[Bot]
    current_bot: int
    state: int

    def __init__(self, bots: List[Bot]):
        self.bots = bots
        self.current_bot = 0
        self.state = UNINIT
        pass

    async def play(self):
        self.state = BOT_TURN
        while self.state == BOT_TURN:
            await self.turn()

    async def turn(self):
        raise NotImplementedError()

    async def repr_json(self):
        return {
            "game": self.game_name_json,
            "state": self.state,
            "field": self.field_json,
            "logs": self.logs_json,
        }

    @property
    def field_json(self):
        raise NotImplementedError()

    @property
    def logs_json(self):
        raise NotImplementedError()

    @property
    def game_name_json(self):
        raise NotImplementedError()
