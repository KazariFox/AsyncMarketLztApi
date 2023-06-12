from typing import List

from lztmarket.Types import Good
from ....Types import Good, Category
from .BaseGame import BaseGame
from ....Types.AccountManage import AccountManager


class GenshinImpact(BaseGame):

    def __init__(self, wrapper) -> None:
        super().__init__(wrapper)
        self.categ_obj = Category.GENSHIN_IMPACT
        self.name = self.categ_obj.name
        self.categ_id = self.categ_obj.id

    async def search(self, page: int = 1, pmin: int | None = None, pmax: int | None = None, title: str | None = None, parse_sticky_items: bool | None = None, parse_same_items: bool | None = None, game: list[int] | None = None, **kwargs) -> List[AccountManager]:
        """email (boolean) - Has linked email

tel (boolean) - Has linked mobile

character[] (string) - List of characters

weapon[] (string) - List of characters

region (string) - Region

ea (boolean) - Has linked external accounts

legendary_min (number) - Minimum number of legendary characters

legendary_max (number) - Maximum number of legendary characters

constellation_min (number) - Minimum number of constellations on legendary characters

constellation_max (number) - Maximum number of constellations on legendary characters

legendary_weapon_min (number) - Minimum number of legendary weapon characters

legendary_weapon_max (number) - Maximum number of legendary weapon characters

char_min (number) - Minimum number of characters

char_max (number) - Maximum number of characters

level_min (number) - Minimum level

level_max (number) - Maximum level"""
        return await super().search(page, pmin, pmax, title, parse_sticky_items, parse_same_items, game, **kwargs)