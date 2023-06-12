from typing import List
from ....Types import Good
from ....Types import Good, Category
from ....Utils import Response


class BaseGame:

    def __init__(self, wrapper) -> None:
        self.__wrapper = wrapper
        self.name = None

    async def search(
        self,
        page: int = 1,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        parse_sticky_items: bool | None = None,
        parse_same_items: bool | None = None,
        game: list[int] | None = None,
        **kwargs
    ) -> list[Good.Account]:
        """Private method for execute search"""
        params = {}

        arg_types = {
            "page": int,
            "pmin": int,
            "pmax": int,
            "title": str,
            "parse_sticky_items": bool,
            "parse_same_items": bool,
            "game": list,
        }

        for arg_name, arg_type in arg_types.items():
            arg_value = locals()[arg_name]
            if arg_value is not None and not isinstance(arg_value, arg_type):
                raise TypeError(
                    f"{arg_name} must be {arg_type.__name__} or None!")

        if page < 1:
            raise ValueError("page must be equal to or bigger than 1")
        params['page'] = page

        if pmin is not None:
            params['pmin'] = pmin
        if pmax is not None:
            params['pmax'] = pmax
        if title is not None:
            params['title'] = title
        if parse_sticky_items is not None:
            params['parse_sticky_items'] = parse_sticky_items
        if parse_same_items is not None:
            params['parse_same_items'] = parse_same_items
        if game is not None:
            params['game'] = game

        for arg in kwargs.keys():
            params[arg] = kwargs[arg]
        response = await self.__wrapper._execute(
            f"/{self.name}",
            "get",
            params=params
        )

        return Response.response_to_accounts(self.__wrapper, response['items'])
