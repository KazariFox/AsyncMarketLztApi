from typing import Any
from ...ApiWrapper import Wrapper
from ...Types.Profile import User
class Me:

    def __init__(self, wrapper: Wrapper) -> None:
        self.__wrapper = wrapper

    async def info(self) -> User:
        data = await self.__wrapper._execute(
            "/me",
            "get"
        )
        return User.parse_obj(data['user'])