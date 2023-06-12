from typing import List

from lztmarket.Types import Good
from ....Types import Good, Category
from .BaseGame import BaseGame
from ....Types.AccountManage import AccountManager


class Battlenet(BaseGame):

    def __init__(self, wrapper) -> None:
        super().__init__(wrapper)
        self.categ_obj = Category.BATTLENET
        self.name = self.categ_obj.name
        self.categ_id = self.categ_obj.id

    async def search(self, page: int = 1, pmin: int | None = None, pmax: int | None = None, title: str | None = None, parse_sticky_items: bool | None = None, parse_same_items: bool | None = None, game: list[int] | None = None, **kwargs) -> List[AccountManager]:
        """game (array) - List of games

daybreak (number) - Number of days the account has been offline

country[] (array) - List of allowed countries

not_country[] (array) - List of disallowed countries

edit_btag (boolean) - Can edit BattleTag

changeable_fn (boolean) - Can edit full name

real_id (boolean) - Read name

tel (boolean) - Has linked mobile

parent_control (boolean) - Has enabled parent control

cookies (boolean) - Login by cookies

lmin (number) - Minimum level in Overwatch

lmax (number) - Maximum level in Overwatch

balance_min (number) - Minimum balance

balance_max (number) - Maximum balance"""
        return await super().search(page, pmin, pmax, title, parse_sticky_items, parse_same_items, game, **kwargs)