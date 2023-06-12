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
        """P.s. на момент разработки параметры не были указаны в документации к API. Эта документация сгенерирована ChatGPT. 

        Параметры:
        - user_id (int): ID пользователя, чьи товары нужно искать.
        - category_id (int): ID категории товаров. По умолчанию 1.
        - pmin (int): Минимальная цена товаров.
        - pmax (int): Максимальная цена товаров.
        - title (str): Название товаров.
        - game (list[int]): Список ID игр, к которым относятся товары.
        - hours_played (dict[int, int]): Словарь, где ключ - ID игры, а значение - минимальное количество часов игры.
        - hours_played_max (dict[int, int]): Словарь, где ключ - ID игры, а значение - максимальное количество часов игры.
        - login (str): Логин пользователя, чьи товары нужно искать.
        - item_domain (str): Домен сайта, на котором продается товар.
        - points_min (int): Минимальное количество очков, заработанных пользователем.
        - points_max (int): Максимальное количество очков, заработанных пользователем.
        - lmin (int): Минимальный уровень аккаунта.
        - lmax (int): Максимальный уровень аккаунта.
        - friend_min (int): Минимальное количество друзей пользователя.
        - friend_max (int): Максимальное количество друзей пользователя.
        - relevant_gmin (int): Минимальное количество релевантных игр пользователя.
        - relevant_gmax (int): Максимальное количество релевантных игр пользователя.
        - gmin (int): Минимальное количество игр у пользователя.
        - gmax (int): Максимальное количество игр у пользователя.
        - eg (int): Количество игр, в которые играл пользователь.
        - daybreak (int): Количество дней, после которых аккаунт был заблокирован.
        - last_trans_date (int): Количество дней, прошедших с момента последней транзакции.
        - last_trans_date_period (str): Период времени, за который нужно проанализировать последнюю транзакцию. Если задан этот параметр, то параметр last_trans_date не учитывается.
        - last_trans_date_later (int): Количество дней, прошедших с момента последней транзакции, с которых нужно начинать поиск.
        - last_trans_date_period_later (str): Период времени, с которого нужно начинать поиск последней транзакции. Если задан этот параметр, то параметры last_trans_date и last_trans_date_period не учитываются.
        - mafile (int): Тип аккаунта на площадке.
        - limit (int): Максимальное количество товаров, которое нужно вернуть.
        - rt (int): Тип оплаты.
        - recently_hours_min (int): Минимальное количество часов игры за последнюю неделю.
        - recently_hours_max (int): Максимальное количество часов игры за последнюю неделю.
        - gift_min (int): Минимальное количество полученных подарков.
        - gift_max (int): Максимальное количество полученных подарков.
        - inv_game (int): ID игры, в которой нужно искать инвентарь пользователя.
        - inv_min (int): Минимальное количество предметов в инвентаре пользователя.
        - inv_max (int): Максимальное количество предметов в инвентаре пользователя.
        - balance_min (int): Минимальный баланс пользователя.
        - balance_max (int): Максимальный баланс пользователя.
        - reg (int): Количество дней, прошедших с момента регистрации пользователя.
        - reg_period (str): Прод времени, за который нужно проанализировать период регистрации. Если задан этот параметр, то параметр reg не учитывается.
        - win_count_min (int): Минимальное количество побед пользователя.
        - win_count_max (int): Максимальное количество побед пользователя.
        - rmin (int): Минимальный ранг пользователя.
        - rmax (int): Максимальный ранг пользователя.
        - wingman_rmin (int): Минимальный ранг пользователя в "Wingman".
        - wingman_rmax (int): Максимальный ранг пользователя в "Wingman".
        - csgo_profile_rank_min (int): Минимальный ранг в игре "CS:GO".
        - csgo_profile_rank_max (int): Максимальный ранг в игре "CS:GO".
        - medal_min (int): Минимальный уровень медали пользователя.
        - medal_max (int): Максимальный уровень медали пользователя.
        - faceit_lvl_min (int): Минимальный уровень в игре "FACEIT".
        - faceit_lvl_max (int): Максимальный уровень в игре "FACEIT".
        - mm_ban (int): Количество забаненных пользователей в игре "Matchmaking".
        - solommr_min (int): Минимальный рейтинг пользователя в игре "Solo Matchmaking".
        - solommr_max (int): Максимальный рейтинг пользователя в игре "Solo Matchmaking".
        - d2_game_count_min (int): Минимальное количество игр пользователя в игре "Dota 2".
        - d2_game_count_max (int): Максимальное количество игр пользователя в игре "Dota 2".
        - d2_win_count_min (int): Минимальное количество побед пользователя в игре "Dota 2".
        - d2_win_count_max (int): Максимальное количество побед пользователя в игре "Dota 2".
        - d2_behavior_min (int): Минимальное количество баллов поведения пользователя в игре "Dota 2".
        - d2_behavior_max (int): Максимальное количество баллов поведения пользователя в игре "Dota 2".
        - order_by (str): Параметр сортировки результатов поиска. По умолчанию "price_to_up"."""
        return await super().search(page, pmin, pmax, title, parse_sticky_items, parse_same_items, game, **kwargs)
