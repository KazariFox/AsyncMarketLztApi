from typing import List


from ....Types import Good, Category
from .BaseGame import BaseGame
from ....Types.AccountManage import AccountManager


class Spotify(BaseGame):

    def __init__(self, wrapper) -> None:
        super().__init__(wrapper)
        self.categ_obj = Category.SPOTIFY
        self.name = self.categ_obj.name
        self.categ_id = self.categ_obj.id

    async def search(self, page: int = 1, pmin: int | None = None, pmax: int | None = None, title: str | None = None, parse_sticky_items: bool | None = None, parse_same_items: bool | None = None, game: list[int] | None = None, **kwargs) -> List[AccountManager]:
        """country[] (array) - List of allowed countries

not_country[] (array) - List of disallowed countries

family (boolean) - Has family subscription

family_manager (boolean) - Has family manager permissions

family_member_count_min (number) - Minimum count of members in family

family_member_count_max (number) - Maximum count of members in family

subscription_length (number) - Length of subscription

subscription_period (string) - In what notation is time measured

recurring (boolean) - Is auto renewal enabled

trial (boolean) - Trial subscription

plan_name[] (array) - List of allowed plans"""
        return await super().search(page, pmin, pmax, title, parse_sticky_items, parse_same_items, game, **kwargs)