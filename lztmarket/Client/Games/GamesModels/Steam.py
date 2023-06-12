from typing import List
from ....Types import Good, Category
from .BaseGame import BaseGame
from ....Types.AccountManage import AccountManager


class Steam(BaseGame):

    def __init__(self, wrapper) -> None:
        super().__init__(wrapper)
        self.categ_obj = Category.STEAM
        self.name = self.categ_obj.name
        self.categ_id = self.categ_obj.id

    async def search(self, page: int = 1, pmin: int | None = None, pmax: int | None = None, title: str | None = None, parse_sticky_items: bool | None = None, parse_same_items: bool | None = None, game: list[int] | None = None, **kwargs) -> List[AccountManager]:
            """game[] (array) - List of games

            hours_played (array) - List of minimum hours played by game

            hours_played_max (array) - List of maximum hours played by game

            vac (number) - List of VAC bans by game

            rt (boolean) - Has red sign

            prime (boolean) - Has Prime in CS:GO

            daybreak (number) - Number of days the account has been offline

            limit (boolean) - Has 5$ limit

            mafile (boolean) - Has .mafile

            reg (number) - How old is the account

            reg_period (string) - In what notation is time measured

            lmin (number) - Minimum level

            lmax (number) - Maximum level

            rmin (number) - Minimum rank in CS:GO Matchmaking

            rmax (number) - Maximum rank in CS:GO Matchmaking

            wingman_rmin (number) - Minimum rank in CS:GO Wingman

            wingman_rmax (number) - Maximum rank in CS:GO Wingman

            no_vac (boolean) - Has no VAC ban

            mm_ban (boolean) - Has CS:GO Matchmaking ban

            balance_min (number) - Minimum balance

            balance_max (number) - Maximum balance

            inv_game (number) - Game ID to check inventory price

            inv_min (number) - Minimum inventory price for game

            inv_max (number) - Maximum inventory price for game

            friend_min (number) - Minimum number of friends

            friend_max (number) - Maximum number of friends

            gmin (number) - Minimum number of games

            gmax (number) - Maximum number of games

            win_count_min (number) - Minimum number of wins

            win_count_max (number) - Maximum number of wins

            medal[] (array) - List of medal names

            medal_id[] (array) - List of medal IDs

            medal_min (number) - Minimum number of medals

            medal_max (number) - Maximum number of medals

            gift[] (array) - List of gifts

            gift_min (number) - Minimum number of gifts

            gift_max (number) - Maximum number of gifts

            recently_hours_min (number) - Minimum number of recently played hours

            recently_hours_max (number) - Maximum number of recently played hours

            country[] (array) - List of allowed countries

            not_country[] (array) - List of disallowed countries

            csgo_profile_rank (string) - CS:GO rank (>=)

            csgo_profile_rank_min (number) - Minimum CS:GO rank

            csgo_profile_rank_max (number) - Maximum CS:GO rank

            solommr_min (number) - Minimum number of Dota 2 MMR

            solommr_max (number) - Maximum number of Dota 2 MMR

            d2_game_count_min (number) - Minimum number of Dota 2 games

            d2_game_count_max (number) - Maximum number of Dota 2 games

            d2_win_count_min (number) - Minimum number of Dota 2 wins

            d2_win_count_max (number) - Maximum number of Dota 2 wins

            d2_behavior_min (number) - Minimum number of Dota 2 behavior

            d2_behavior_max (number) - Maximum number of Dota 2 behavior

            faceit_lvl_min (number) - Minimum FACEIT level

            faceit_lvl_max (number) - Maximum FACEIT level

            points_min (number) - Minimum number of Steam points

            points_max (number) - Maximum number of Steam points

            relevant_gmin (number) - Minimum number of relevant games

            relevant_gmax (number) - Maximum number of relevant games

            last_trans_date (number) - How old is last transaction

            last_trans_date_period (string) - In what notation is time measured

            last_trans_date_later (number) - How new is last transaction

            last_trans_date_period_later (string) - In what notation is time measured

            no_trans (boolean) - Has no transactions

            trans (boolean) - Has transactions"""
            return await super().search(page, pmin, pmax, title, parse_sticky_items, parse_same_items, game, **kwargs)
