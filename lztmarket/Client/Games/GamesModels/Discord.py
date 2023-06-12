from typing import List

from lztmarket.Types import Good
from ....Types import Good, Category
from .BaseGame import BaseGame
from ....Types.AccountManage import AccountManager


class Discord(BaseGame):

    def __init__(self, wrapper) -> None:
        super().__init__(wrapper)
        self.categ_obj = Category.DISCORD
        self.name = self.categ_obj.name
        self.categ_id = self.categ_obj.id

    async def search(self, page: int = 1, pmin: int | None = None, pmax: int | None = None, title: str | None = None, parse_sticky_items: bool | None = None, parse_same_items: bool | None = None, game: list[int] | None = None, **kwargs) -> List[AccountManager]:
        """tel (boolean) - Has linked mobile

nitro (boolean) - Has Nitro

billing (boolean) - Has billing

gifts (boolean) - Has gifts

quarantined (boolean) - Кодер еблан, почему вообще заблокированные акки можно заливать?

condition[] (array) - List of account conditions

chat_min (number) - Minimum number of chats

chat_max (number) - Maximum number of chats

reg (number) - How old is the account

reg_period (string) - In what notation is time measured

locale[] (array) - List of regions

not_locale[] (array) - List of regions that won't be included

badge[] (array) - List of badges"""
        return await super().search(page, pmin, pmax, title, parse_sticky_items, parse_same_items, game, **kwargs)