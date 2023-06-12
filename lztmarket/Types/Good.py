from typing import Dict, List, Optional, Any
from enum import Enum
from pydantic import BaseModel

from .Category import *

from .User import Seller


class Account(BaseModel):
    item_id: int
    category_id: int
    published_date: int
    title: str
    title_en: str
    item_origin: str
    price: int
    allow_ask_discount: int
    price_currency: str
    temp_email: str = None
    description: str
    view_count: int
    is_reserved: int
    item_domain: str = None
    seller: Seller
    cannotBuyItemError: str = None
    canStickItem: bool = False
    canUnstickItem: bool = False
    canBuyItem: bool = False
    canCloseItem: bool = False
    canOpenItem: bool = False
    canReportItem: bool = False
    canEditItem: bool = False
    canDeleteItem: bool = False
    canCancelConfirmedBuy: bool = False
    canViewItemHistory: bool = False
    faveCount: bool = False
    isVisibleItem: bool = False
    canViewLoginData: bool = False
    unfiltered_account_data: dict = None


class VkAccount(Account):
    vk_item_id: int
    vk_id: int = None
    vk_id_count: int = None
    vk_friend_count: int = None
    vk_follower_count: int = None
    vk_admin_groups: list = None
    vk_max_group_follower_count: int = None
    vk_vote_count: int = None
    vk_country: str = None
    vk_sex: str = None
    vk_mobile: str = None
    vk_register_date: int = None
    vk_age: int = None
    vk_city: str = None
    vk_email: int = None
    vk_mobile_country: int = None
    vk_tfa: int = None
    vk_is_closed: int = None
    vk_relation: int = None
    vk_count_conversations: int = None
    vk_mobile_country: str = None
    vk_sex_phrase: str = None
    vk_relation_phrase: str = None
    vk_token: str = None
    vk_ua: str = None


class SteamAccount(Account):
    steam_item_id: int = None
    account_country: str = None
    steam_register_date: int = None
    steam_last_activity: int = None
    account_full_games: dict = None
    account_community_ban: int = None
    steam_csgo_profile_rank: int = None
    account_balance: str = None
    account_csgo_rank_id: int = None
    last_update_time: int = None
    steam_is_limited: int = None
    steam_level: int = None
    steam_friend_count: int = None
    steam_csgo_last_activity: int = None
    steam_dota2_solo_mmr: int = None
    steam_dota2_party_mmr: int = None
    steam_csgo_ban_date: int = None
    steam_converted_balance: int = None
    steam_pubg_inv_value: int = None
    steam_csgo_inv_value: int = None
    steam_dota2_inv_value: int = None
    steam_tf2_inv_value: int = None
    steam_rust_inv_value: int = None
    steam_csgo_wingman_rank_id: int = None
    steam_game_count: int = None
    steam_steam_inv_value: int = None
    steam_inv_value: int = None
    steam_csgo_win_count: int = None
    steam_dota2_game_count: int = None
    steam_dota2_lose_count: int = None
    steam_dota2_win_count: int = None
    steam_hours_played_recently: float = None
    steam_faceit_level: int = None
    steam_points: int = None
    steam_last_transaction_date: int = None
    steam_relevant_game_count: int = None
    steam_gift_count: int = None
    steam_limit_spent: str = None
    steam_dota2_behavior: int = None
    steam_has_faceit: int = None
    steam_mfa: int = None
    steam_market: int = None
    steam_market_restrictions: str = None
    steam_market_ban_end_date: int = None
    steam_unturned_inv_value: int = None
    steam_csgo_last_launched: int = None
    steam_kf2_inv_value: int = None
    steam_dst_inv_value: int = None
    steamData: dict = None
    steamRelevantGameCount: int = None
    hasCsgo: bool = None
    isSmallExf: bool = None
    hasDota2: bool = None
    hasPubg: bool = None
    hasTf2: bool = None
    hasRust: bool = None
    inventoryValue: dict = None
    steamCsgoMedals: list = None
    steamTransactions: list = None
    canSteamPreviewProfile: bool = None
    canSteamPreviewGames: bool = None
    hasPossibleBanInDota2: bool = None
    chineseAccount: bool = None
    canViewAccountLink: bool = None


class OriginGame(BaseModel):
    game_id: str
    title: str
    last_activity: int
    total_played: int
    is_full: bool
    img: str


class OriginAccount(Account):
    ea_item_id: int
    ea_id: int
    ea_account_country: str
    ea_account_games: str
    ea_last_activity: int
    ea_al_level: int
    ea_al_rank: str
    ea_subscription: str
    ea_subscription_end_date: int
    ea_username: str
    ea_al_rank_group: str
    ea_skip_email_check: int
    ea_xbox_connected: int
    ea_steam_connected: int
    ea_account_full_games: Optional[Dict[str, OriginGame]] = None


class WarfaceItemInfo(BaseModel):
    id: int
    title: str
    itemid: str
    count: str
    duration: str
    duration_type: str
    consumable: str
    permanent: str
    regular: str
    priority: str
    tag: str
    type: str
    limit: str


class WarfaceGun(BaseModel):
    cartid: str
    csaid: str
    itemid: str
    itemcount: str
    last_update: str
    promoid: str
    tid: str
    iteminfo: WarfaceItemInfo


class WarfaceServer(BaseModel):
    id: int
    rank: int
    title: str


class WarfaceAccount(Account):
    wf_item_id: int
    wf_players: List[Any]
    wf_guns: Dict[str, List[WarfaceGun]]
    wf_server_1: int
    wf_server_2: int
    wf_server_3: int
    wf_mobile: int
    wf_bonus_rank: int
    wf_last_game_date: int
    wf_loan: Optional[Any]
    wf_active_loan: int
    wf_rank: int
    wf_gun_count: int = None
    wf_servers: List[WarfaceServer]
    domain: str

class UplayAccount(Account):
    uplay_item_id: int
    uplay_account_last_activity: int
    uplay_account_country: str
    uplay_account_created_date: int
    uplay_account_full_games: dict
    uplay_account_r6_level: int

class SocialClubAccount(Account):
    socialclub_item_id: int
    socialclub_id: str
    socialclub_level: int
    socialclub_cash: int
    socialclub_bank_cash: int
    socialclub_games: list
    socialclub_last_activity: int
    socialclub_has_gtav: int
    socialclub_has_rdr2: int




CATEG_AND_ACCOUNT = {
    STEAM.id: SteamAccount,
    VK.id: VkAccount,
    ORIGIN.id: OriginAccount,
    WARFACE.id: WarfaceAccount,
    UPLAY.id: UplayAccount,
    SOCIAL_CLUB.id: SocialClubAccount
}
