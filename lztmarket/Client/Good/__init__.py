from ...Types.AccountManage import AccountManager
from ...ApiWrapper import Wrapper

class Good:

    def __init__(self, wrapper: Wrapper) -> None:
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

    async def add(
            self,
            title: str,
            price: int,
            category_id: int,
            currency: str,
            item_origin: str,
            extended_guarantee: int,
            email_login_data: str=None,
            email_type: str=None,
            allow_ask_discount: bool=None,
            proxy_id: int=None,
            random_proxy: bool=None,
            description: str=None,
            information: str=None,
            has_email_login_data: bool=False,
            title_en: str=None,
            ) -> AccountManager:
        params = dict(
            title=title, 
            price=price, 
            category_id=category_id, 
            currency=currency,
            item_origin=item_origin, 
            extended_guarantee=extended_guarantee)
        
        if email_login_data is not None: params['email_login_data']=email_login_data
        if email_type is not None: params['email_type']=email_type
        if allow_ask_discount is not None: params['allow_ask_discount']=allow_ask_discount
        if proxy_id is not None: params['proxy_id']=proxy_id
        if random_proxy is not None: params['random_proxy']=random_proxy
        if description is not None: params['description']=description
        if information is not None: params['information']=information
        if has_email_login_data is not None: params['has_email_login_data']=has_email_login_data
        if title_en is not None: params['title_en']=title_en

        reponse = await self.__wrapper._execute(
            "/item/add",
            "post",
            params=params
        )

        return AccountManager(self.__wrapper, reponse['item']['item_id'])

    
