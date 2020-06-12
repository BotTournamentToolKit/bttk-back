from typing import List

from game import Game, DISQUALIFIED, BOT_WON
from games.matches.bot.MatchesBot import MatchesBot


class MatchesGame(Game):
    matches_count: int

    def __init__(self, bots: List[MatchesBot]):
        super().__init__(bots)
        # check for count of bots  -----------???--------

    async def turn(self):
        # make turn
        try:
            turn = await self.bots[self.current_bot].turn(self.matches_count)
        except:
            self.state = DISQUALIFIED
            return

        turn = int(turn)

        # check for validity of turn
        if turn >= 1 & turn <= 3 & self.matches_count >= turn:
            # turn is correct
            self.matches_count -= turn
        else:
            # turn is incorrect
            self.state = DISQUALIFIED
            return

        # check for end of the game
        if self.matches_count == 0:
            self.state = BOT_WON
            return

        # else change player
        self.current_bot = (self.current_bot + 1) % 2
        return

    @property
    def field_json(self):
        return str(self.matches_count)

    @property
    def logs_json(self):
        return ""

    @property
    def game_name_json(self):
        return ""