from typing import List


from ....Types import Good, Category
from .BaseGame import BaseGame
from ....Types.AccountManage import AccountManager


class Fortnite(BaseGame):

    def __init__(self, wrapper) -> None:
        super().__init__(wrapper)
        self.categ_obj = Category.FORTNITE
        
        self.name = self.categ_obj.name
        self.categ_id = self.categ_obj.id

    async def search(self, page: int = 1, pmin: int | None = None, pmax: int | None = None, title: str | None = None, parse_sticky_items: bool | None = None, parse_same_items: bool | None = None, game: list[int] | None = None, **kwargs) -> List[AccountManager]:
        """smin (number) - Minimum number of skins

smax (number) - Maximum number of skins

vbmin (number) - Minimum number of V-Bucks

vbmax (number) - Maximum number of V-Bucks

skin (array) - Skins

pickaxe (array) - Pickaxes

dance (array) - Dances

glider (array) - Gliders

change_email (boolean) - Can change email

platform (array) - Platform

bp (boolean) - Has Battle Pass

lmin (number) - Minimum level

lmax (number) - Maximum level

bp_lmin (number) - Minimum level of Battle Pass

bp_lmax (number) - Maximum level of Battle Pass

rl_purchases (boolean) - Has Rocket League purchases

last_trans_date (number) - How old is last transaction

last_trans_date_period (string) - In what notation is time measured

no_trans (boolean) - Has no transactions

xbox_linkable (boolean) - Can be linked to Xbox

psn_linkable (boolean) - Can be linked to PSN

daybreak (number) - Number of days the account has been offline

temp_email (boolean) - Access to market temp mail"""
        return await super().search(page, pmin, pmax, title, parse_sticky_items, parse_same_items, game, **kwargs)