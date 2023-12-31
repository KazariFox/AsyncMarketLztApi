from typing import List


from ....Types import Good, Category
from .BaseGame import BaseGame
from ....Types.AccountManage import AccountManager


class Telegram(BaseGame):

    def __init__(self, wrapper) -> None:
        super().__init__(wrapper)
        self.categ_obj = Category.TELEGRAM
        self.name = self.categ_obj.name
        self.categ_id = self.categ_obj.id

    async def search(self, page: int = 1, pmin: int | None = None, pmax: int | None = None, title: str | None = None, parse_sticky_items: bool | None = None, parse_same_items: bool | None = None, game: list[int] | None = None, **kwargs) -> List[AccountManager]:
        """scam (boolean) - Has a scam badge

spam (boolean) - Has a spam ban

password (boolean) - Has a cloud password

premium (boolean) - Has a premium subscription

country[] (array) - List of allowed countries

not_country[] (array) - List of disallowed countries

daybreak (number) - Number of days the account has been offline"""
        return await super().search(page, pmin, pmax, title, parse_sticky_items, parse_same_items, game, **kwargs)