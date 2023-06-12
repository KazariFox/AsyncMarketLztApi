from ...ApiWrapper import Wrapper
from typing import List
from ...Types import Good, Category
from ...Utils import Response
from . import GamesModels



class Games():
    def __init__(self, wrapper: Wrapper):
        self.__wrapper = wrapper
        self.Steam = GamesModels.Steam(wrapper)
        self.Vk = GamesModels.VK(wrapper)
        self.Origin = GamesModels.Origin(wrapper)
        self.Warface = GamesModels.Warface(wrapper)
        self.Uplay = GamesModels.Uplay(wrapper)
        self.SocialClub = GamesModels.SocialClub(wrapper)
        self.Fortnite = GamesModels.Fortnite(wrapper)
        self.Instagram = GamesModels.Instagram(wrapper)
        self.Battlenet = GamesModels.Battlenet(wrapper)
        self.EpicGames = GamesModels.EpicGames(wrapper)
        self.Valorant = GamesModels.Valorant(wrapper)
        self.WorldOfTanks = GamesModels.WorldOfTanks(wrapper)
        self.Blitz = GamesModels.Blitz(wrapper)
        self.Supercell = GamesModels.Supercell(wrapper)
        self.GenshinImpact = GamesModels.GenshinImpact(wrapper)
        self.EscapeFromTarkov = GamesModels.EscapeFromTarkov(wrapper)
        self.Vpn = GamesModels.VPN(wrapper)
        self.TikTok = GamesModels.TikTok(wrapper)
        self.Discord = GamesModels.Discord(wrapper)
        self.Cinema = GamesModels.Cinema(wrapper)
        self.Telegram = GamesModels.Telegram(wrapper)
        self.YouTube = GamesModels.YouTube(wrapper)
        self.Spotify = GamesModels.Spotify(wrapper)
        self.WarThunder = GamesModels.WarThunder(wrapper)



    async def last(self, page: int = 1) -> List[Good.Account]:
        """Displays a list of latest accounts."""
        response = await self.__wrapper._execute(
            "/",
            "get",
            params={"page": page}
        )
        return Response.response_to_accounts(self.__wrapper, response['items'])
