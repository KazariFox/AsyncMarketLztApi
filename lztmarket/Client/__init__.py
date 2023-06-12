from ..ApiWrapper import Wrapper
from .Games import Games
from .Good import Good
from .Payment import Payment
from .Me import Me


class MarketClient(Wrapper):

    def __init__(self, api_key: str) -> None:
        """Args:
        api_key (str): the API key for authentication on the server.
        """

        super().__init__(api_key=api_key)
        self.Goods = Games(self)
        self.Good = Good(self)
        self.Payment = Payment(self)
        self.Me = Me(self)
