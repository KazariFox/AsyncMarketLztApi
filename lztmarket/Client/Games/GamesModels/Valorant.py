from typing import List

from lztmarket.Types import Good
from ....Types import Good, Category
from .BaseGame import BaseGame
from ....Types.AccountManage import AccountManager


class Valorant(BaseGame):

    def __init__(self, wrapper) -> None:
        super().__init__(wrapper)
        self.categ_obj = Category.VALORANT
        self.name = self.categ_obj.name
        self.categ_id = self.categ_obj.id

    async def search(self, page: int = 1, pmin: int | None = None, pmax: int | None = None, title: str | None = None, parse_sticky_items: bool | None = None, parse_same_items: bool | None = None, game: list[int] | None = None, **kwargs) -> List[AccountManager]:
        """weaponSkin[] (array) - List of weapon skis

buddy[] (array) - List of buddies

agent[] (array) - List of agents

country[] (array) - List of allowed countries

not_country[] (array) - List of disallowed countries

daybreak (number) - Number of days the account has been offline

level_min (number) - Minimum level

level_max (number) - Maximum level

vp_min (number) - Minimum number of Valorant points

vp_max (number) - Maximum number of Valorant points

smin (number) - Minimum number of skins

smax (number) - Maximum number of skins

rmin (number) - Minimum rank (from 3 to 27)

rmax (number) - Maximum rank

last_rmin (number) - Last Minimum rank (from 3 to 27)

last_rmax (number) - Last Maximum rank

rank_type (string) - Rank type

amin (number) - Minimum amount of agents

amax (number) - Maximum amount of agents

region[] (array) - List of allowed regions

not_region[] (array) - List of disallowed regions

email (boolean) - Has linked email

tel (boolean) - Has linked mobile

changeable_email (boolean) - Can change email"""
        return await super().search(page, pmin, pmax, title, parse_sticky_items, parse_same_items, game, **kwargs)