from typing import List

from lztmarket.Types import Good
from ....Types import Good, Category
from .BaseGame import BaseGame
from ....Types.AccountManage import AccountManager


class WarThunder(BaseGame):

    def __init__(self, wrapper) -> None:
        super().__init__(wrapper)
        self.categ_obj = Category.WAR_THUNDER
        self.name = self.categ_obj.name
        self.categ_id = self.categ_obj.id

    async def search(self, page: int = 1, pmin: int | None = None, pmax: int | None = None, title: str | None = None, parse_sticky_items: bool | None = None, parse_same_items: bool | None = None, game: list[int] | None = None, **kwargs) -> List[AccountManager]:
        """daybreak (number) - Number of days the account has been offline

gold_min (number) - Minimum number of gold

gold_max (number) - Maximum number of gold

silver_min (number) - Minimum number of silver

silver_max (number) - Maximum number of silver

rank_min (number) - Minimal rank

rank_max (number) - Maximum rank

eliteUnits_min (number) - Minimum number of elite units

eliteUnits_max (number) - Maximum number of elite units

played_min (number) - Minimum number of played games

played_max (number) - Maximum number of played games

wins_min (number) - Minimum number of wins

wins_max (number) - Maximum number of wins

phone_verified (boolean) - Has verified mobile

email_verified (boolean) - Has verified email

premium (boolean) - Has premium"""
        return await super().search(page, pmin, pmax, title, parse_sticky_items, parse_same_items, game, **kwargs)