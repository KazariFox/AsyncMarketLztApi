from ...Types.AccountManage import AccountManager


class Good:

    def __init__(self, wrapper) -> None:
        self.__wrapper = wrapper

    async def get(self, id: int, force: bool=False) -> AccountManager:
        """
        Получает аккаунт по id.

        :param id: идентификатор аккаунта.
        :force: информация об аккаунте не будет получена.
        Полезно, если требуется совершить многжество действий.
        К примеру, поднять несколько аккаунтов.
        :type id: int
        :return: экземпляр класса AccountManager.
        :rtype: AccountManager
        """
        am = AccountManager(self.__wrapper, id)
        if not force:
            await am.get_info()
        return am
