from typing import List

from lztmarket.Types import Good
from ....Types import Good, Category
from .BaseGame import BaseGame
from ....Types.AccountManage import AccountManager


class TikTok(BaseGame):

    def __init__(self, wrapper) -> None:
        super().__init__(wrapper)
        self.categ_obj = Category.TIKTOK
        self.name = self.categ_obj.name
        self.categ_id = self.categ_obj.id

    async def search(self, page: int = 1, pmin: int | None = None, pmax: int | None = None, title: str | None = None, parse_sticky_items: bool | None = None, parse_same_items: bool | None = None, game: list[int] | None = None, **kwargs) -> List[AccountManager]:
        """tel (boolean) - Has linked mobile

fmin (number) - Minimum number of followers

fmax (number) - Maximum number of followers

post_min (number) - Minimum number of posts

post_max (number) - Maximum number of posts

like_min (number) - Minimum number of likes

like_max (number) - Maximum number of likes

coins_min (number) - Minimum number of coins

coins_max (number) - Maximum number of coins

tt_country[] (array) - List of allowed countries

tt_not_country[] (array) - List of disallowed countries

cookie_login (boolean) - Login by cookies

verified (boolean) - Has a verified badge

hasLivePermission (boolean) - Can start a live stream"""
        return await super().search(page, pmin, pmax, title, parse_sticky_items, parse_same_items, game, **kwargs)