from typing import List


from ....Types import Good, Category
from .BaseGame import BaseGame
from ....Types.AccountManage import AccountManager


class SocialClub(BaseGame):

    def __init__(self, wrapper) -> None:
        super().__init__(wrapper)
        self.categ_obj = Category.SOCIAL_CLUB
        self.name = self.categ_obj.name
        self.categ_id = self.categ_obj.id

    async def search(self, page: int = 1, pmin: int | None = None, pmax: int | None = None, title: str | None = None, parse_sticky_items: bool | None = None, parse_same_items: bool | None = None, game: list[int] | None = None, **kwargs) -> List[AccountManager]:
        """rdr2 (boolean) - Has Red Dead Redemption 2

gtav (boolean) - Has GTA 5

daybreak (number) - Number of days the account has been offline"""
        return await super().search(page, pmin, pmax, title, parse_sticky_items, parse_same_items, game, **kwargs)