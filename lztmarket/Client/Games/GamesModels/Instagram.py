from typing import List


from ....Types import Good, Category
from .BaseGame import BaseGame
from ....Types.AccountManage import AccountManager


class Instagram(BaseGame):

    def __init__(self, wrapper) -> None:
        super().__init__(wrapper)
        self.categ_obj = Category.INSTAGRAM
        self.name = self.categ_obj.name
        self.categ_id = self.categ_obj.id

    async def search(self, page: int = 1, pmin: int | None = None, pmax: int | None = None, title: str | None = None, parse_sticky_items: bool | None = None, parse_same_items: bool | None = None, game: list[int] | None = None, **kwargs) -> List[AccountManager]:
        """tel (boolean) - Has linked mobile

country[] (array) - List of allowed countries

not_country[] (array) - List of disallowed countries

cookies (boolean) - Login by cookies

login_without_cookies (boolean) - Login without cookies

fmin (number) - Minimum number of followers

fmax (number) - Maximum number of followers

post_min (number) - Minimum number of posts

post_max (number) - Maximum number of posts

reg (number) - How old is the account

reg_period (string) - In what notation is time measured"""
        return await super().search(page, pmin, pmax, title, parse_sticky_items, parse_same_items, game, **kwargs)