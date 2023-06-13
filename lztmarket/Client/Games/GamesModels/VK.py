from typing import List

from ....Types import Good, Category
from .BaseGame import BaseGame
from ....Types.AccountManage import AccountManager


class VK(BaseGame):

    def __init__(self, wrapper) -> None:
        super().__init__(wrapper)
        self.categ_obj = Category.VK
        self.name = self.categ_obj.name
        self.categ_id = self.categ_obj.id

    async def search(self, page: int = 1, pmin: int | None = None, pmax: int | None = None, title: str | None = None, parse_sticky_items: bool | None = None, parse_same_items: bool | None = None, game: list[int] | None = None, **kwargs) -> List[Good.VkAccount]:
        """vk_country[] (array) - List of allowed countries

vk_city[] (array) - List of allowed cities

vk_friend_min (number) - Minimum number of friends

vk_friend_max (number) - Maximum number of friends

vk_follower_min (number) - Minimum number of followers

vk_follower_max (number) - Maximum number of followers

vk_vote_min (number) - Minimum number of votes

vk_vote_max (number) - Maximum number of votes

sex (string) - Sex of account

tel (boolean) - Has linked mobile

email (boolean) - Has linked email

tfa (boolean) - Has enabled 2FA

relation[] (boolean) - Has linked mobile

group_follower_min (number) - Minimum number of group followers

group_follower_max (number) - Maximum number of group followers

groups_min (number) - Minimum number of groups

groups_max (number) - Maximum number of groups

admin_level (string) - Admin level

min_age (number) - Minimum age

max_age (number) - Maximum age

dig_min (number) - Minimum number of digits in ID

dig_max (number) - Maximum number of digits in ID

conversations_min (number) - Minimum number of conversations

conversations_max (number) - Maximum number of conversations

reg (number) - How old is the account

reg_period (string) - In what notation is time measured

mcountry[] (array) - List of allowed countries of phone number

not_mcountry[] (array) - List of excluded countries of phone number

opened_profile (boolean) - Opened account profile"""
        return await super().search(page, pmin, pmax, title, parse_sticky_items, parse_same_items, game, **kwargs)