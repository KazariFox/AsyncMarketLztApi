from typing import NamedTuple
from enum import Enum


class Platform(NamedTuple):
    id: int
    name: str


STEAM = Platform(id=1, name="steam")
VK = Platform(id=2, name="vkontakte")
ORIGIN = Platform(id=3, name="origin")
WARFACE = Platform(id=4, name="warface")
UPLAY = Platform(id=5, name="uplay")
SOCIAL_CLUB = Platform(id=7, name="socialclub")
FORTNITE = Platform(id=9, name="fortnite")
INSTAGRAM = Platform(id=10, name="instagram")
BATTLENET = Platform(id=11, name="battlenet")
EPIC_GAMES = Platform(id=12, name="epicgames")
VALORANT = Platform(id=13, name="valorant")
WORLD_OF_TANKS = Platform(id=14, name="world-of-tanks")
SUPERCELL = Platform(id=15, name="supercell")
WORLD_OF_TANKS_BLITZ = Platform(id=16, name="wot-blitz")
GENSHIN_IMPACT = Platform(id=17, name="genshin-impact")
ESCAPE_FROM_TARKOV = Platform(id=18, name="escape-from-tarkov")
VPN = Platform(id=19, name="vpn")
TIKTOK = Platform(id=20, name="tiktok")
DISCORD = Platform(id=22, name="discord")
ONLINE_CINEMA = Platform(id=23, name="cinema")
TELEGRAM = Platform(id=24, name="telegram")
YOUTUBE = Platform(id=25, name="youtube")
SPOTIFY = Platform(id=26, name="spotify")
WAR_THUNDER = Platform(id=27, name="war-thunder")
