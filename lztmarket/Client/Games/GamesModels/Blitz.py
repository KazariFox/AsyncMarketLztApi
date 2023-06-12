from typing import List

from lztmarket.Types import Good
from ....Types import Good, Category
from .BaseGame import BaseGame
from ....Types.AccountManage import AccountManager


class Blitz(BaseGame):

    def __init__(self, wrapper) -> None:
        super().__init__(wrapper)
        self.categ_obj = Category.WORLD_OF_TANKS_BLITZ
        self.name = self.categ_obj.name
        self.categ_id = self.categ_obj.id

    async def search(self, page: int = 1, pmin: int | None = None, pmax: int | None = None, title: str | None = None, parse_sticky_items: bool | None = None, parse_same_items: bool | None = None, game: list[int] | None = None, **kwargs) -> List[AccountManager]:
        """tel (boolean) - Has linked mobile

daybreak (number) - Number of days the account has been offline

battles_min (number) - Minimum number of battles

battles_max (number) - Maximum number of battles

gold_min (number) - Minimum number of gold

gold_max (number) - Maximum number of gold

silver_min (number) - Minimum number of silver

silver_max (number) - Maximum number of silver

top_min (number) - Minimum number of top tanks

top_max (number) - Maximum number of top tanks

prem_min (number) - Minimum number of premium tanks

prem_max (number) - Maximum number of premium tanks

top_prem_min (number) - Minimum number of top premium tanks

top_prem_max (number) - Maximum number of top premium tanks

win_pmin (number) - Minimum number of wins

win_pmax (number) - Maximum number of wins

tank (array) - List of tanks

region (array) - Region

not_region (array) - Exclude region"""
        return await super().search(page, pmin, pmax, title, parse_sticky_items, parse_same_items, game, **kwargs)