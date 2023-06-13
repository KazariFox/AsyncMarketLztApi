from typing import List


from ....Types import Good, Category
from .BaseGame import BaseGame
from ....Types.AccountManage import AccountManager


class Supercell(BaseGame):

    def __init__(self, wrapper) -> None:
        super().__init__(wrapper)
        self.categ_obj = Category.SUPERCELL
        self.name = self.categ_obj.name
        self.categ_id = self.categ_obj.id

    async def search(self, page: int = 1, pmin: int | None = None, pmax: int | None = None, title: str | None = None, parse_sticky_items: bool | None = None, parse_same_items: bool | None = None, game: list[int] | None = None, **kwargs) -> List[AccountManager]:
        """system (string) - Account service

lmin (number) - Minimum level

lmax (number) - Maximum level

cup_min (number) - Minimum number of cups

cup_max (number) - Maximum number of cups

brawlers_min (number) - Minimum number of brawlers

brawlers_max (number) - Maximum number of brawlers

brawler (array) - List of brawlers"""
        return await super().search(page, pmin, pmax, title, parse_sticky_items, parse_same_items, game, **kwargs)