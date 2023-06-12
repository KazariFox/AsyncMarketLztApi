from ...ApiWrapper import Wrapper
from ...Types import Good, Currency
from .ManageExceptions import NotEnoughRights, NotTempMail, NoAccountInfo


class AccountManager:

    def __init__(self, wrapper: Wrapper, account_id: int, account_info: Good.Account = None) -> None:
        self.__wraper = wrapper
        self.__account_id = account_id
        self.__account_info = account_info

    async def __get_info(self) -> Good.Account:
        account_info_not_sorted = await self.__wraper._execute(
            f"/{self.__account_id}",
            "get"
        )

        return Good.CATEG_AND_ACCOUNT[account_info_not_sorted['item']['category_id']].parse_obj(account_info_not_sorted['item'])

    async def get_info(self, recheck: bool = False) -> Good.Account:
        """
        Возвращает информацию об аккаунте.

        :param recheck: флаг, указывающий нужно ли выполнить повторный запрос для получения информации об аккаунте.
        :type recheck: bool, optional
        :return: информация об аккаунте.
        :rtype: Good.Account
        """
        if not (self.__account_info and not recheck):
            self.__account_info = await self.__get_info()

        if not self.__account_id:
            self.__account_id = self.__account_info.item_id
        return self.__account_info

    # async def check(self) -> Good.Account:
    #     "OUTDATED"
    #     return

    #     data = await self.__wraper._execute(
    #         f"/{self.__account_id}/check-account",
    #         "post"
    #     )
    #     return Good.CATEG_AND_ACCOUNT[data['item']['category_id']].parse_obj(data['item'])

    async def delete(self, reason: str = "") -> None:
        """
        Удаляет аккаунт.

        :param reason: причина удаления аккаунта.
        :type reason: str, optional
        :raises NotEnoughRights: если у аккаунта нет прав на удаление.
        """
        if not self.__account_info.canDeleteItem:
            raise NotEnoughRights(
                f"Not enough rights to delete {self.__account_id}")
        self.__wraper._execute(
            f"/{self.__account_id}",
            "delete",
            params={"reason": reason}
        )

    async def get_mail_code(self, mail: str = None) -> str:
        """
        Получает код подтверждения для указанного временного адреса электронной почты.

        :param mail: временный адрес электронной почты. Если не указан, будет использован адрес, связанный с аккаунтом.
        :type mail: str, optional
        :return: код подтверждения.
        :rtype: str
        :raises NotTempMail: если аккаунт не имеет временного адреса электронной почты, а параметр `mail` не был передан.
        :raises NoAccountInfo: если нет информации об аккаунте.
        """
        params = {}
        if self.__account_info and not self.__account_info.temp_email and not mail:
            raise NotTempMail("The account does not have a temporary email.")
        elif not self.__account_info:
            raise NoAccountInfo("No information about account.")

        params['email'] = mail

        if self.__account_info.temp_email:
            params['email'] = self.__account_info.temp_email

        response = await self.__wraper._execute(
            f"/{self.__account_id}/email-code",
            'get',
            params=params
        )
        return response['codeData']['code']

    async def get_guard_code(self) -> str:
        """
        Получает код Guard для аккаунта.

        :return: код Guard.
        :rtype: str
        :raises NoAccountInfo: если нет информации об аккаунте.
        """
        if not self.__account_id:
            raise NoAccountInfo("No information about account.")

        response = await self.__wraper._execute(
            f"/{self.__account_id}/guard-code",
            'get',
        )
        return response['codeData']['code']

    async def get_mafile(self) -> dict:
        """
        Возвращает MA-файл для аккаунта.

        :return: MA-файл.
        :rtype: dict
        :raises NoAccountInfo: если нет информации об аккаунте.
        """
        if not self.__account_id:
            raise NoAccountInfo("No information about account.")

        return await self.__wraper._execute(
            f"/{self.__account_id}/mafile",
            'get',
        )

    async def refuse_guarantee(self) -> None:
        """
        Отменяет гарантию на аккаунт.
        """
        return await self.__wraper._execute(
            f"/{self.__account_id}/refuse-guarantee",
            'post',
        )

    async def decline_safe_about_password(self) -> None:
        """Отмена предложения сменить пароль.
        """
        return await self.__wraper._execute(
            f"/{self.__account_id}/change-password",
            'post',
            params={'_cancel': 1}
        )

    async def change_password(self) -> None:
        """Подтверждение рекомендаций безопасности.
        """
        return await self.__wraper._execute(
            f"/{self.__account_id}/change-password",
            'post'
        )

    async def get_tempmail_password(self) -> None:
        """Получить пароль от временной почты.
        """
        return (await self.__wraper._execute(
            f"/{self.__account_id}/temp-email-password",
            'get'
        ))['item']['tempEmailData']['password']
    "Purchasing"

    async def edit(
            self,
            currency: str=Currency.RUB,
            title: str=None,
            title_en: str=None,
            price: int=None,
            item_origin: str=None,
            description: str=None,
            information: str=None,
            has_email_login_data: bool=None,
            email_login_data: str=None,
            email_type: str=None,
            allow_ask_discount: bool=None,
            proxy_id: int=None
            ) -> None:
        """
        Обновление информации об аккаунте

        Параметры:
        - валюта (необязательно): Валюта, в которой указывается цена счета. Допустимые значения: "cny", "usd", "rub", "eur", "uah", "kzt", "byn" и "gbp". Значение по умолчанию - "rub".
        - title (необязательно): Название счета на русском языке.
        - title_en (необязательно): Название счета на английском языке.
        - price (необязательно): Цена счета в вашей валюте.
        - item_origin (необязательно): Происхождение счета.
        - description (необязательно): Публичное описание счета.
        - информация (необязательно): Закрытая информация об аккаунте, видимая покупателю только в случае покупки.
        - has_email_login_data (необязательно): Булево значение, указывающее, имеются ли данные для входа в систему по электронной почте.
        - email_login_data (необязательно): Данные для входа в систему по электронной почте в формате "логин:пароль".
        - email_type (необязательный): Тип электронной почты. Допустимые значения: "native" и "autoreg".
        - allow_ask_discount (необязательно): Булево значение, указывающее, могут ли пользователи просить скидку для этого аккаунта.
        - proxy_id (необязательно): Идентификатор прокси, который будет использоваться для проверки аккаунта. Список прокси можно получить или отредактировать с помощью конечной точки GET /account/market.

        Возвращает:
        - None
        """ 
        non_none_params = {k: v for k, v in locals().items() if v is not None and k != 'self'}
        params={}

        params['currency'] = non_none_params['currency']

        del non_none_params['currency']

        for param in non_none_params.keys():
            params[f'key_values[{param}]'] = non_none_params[param]

        return await self.__wraper._execute(
            f'/{self.__account_id}/edit',
            'put',
            params=params
        )
    
    async def bump(self) -> None:
        """Поднятие аккаунта
        """
        return await self.__wraper._execute(
            f'/{self.__account_id}/bump',
            'post'
        )

    async def favorite(self) -> None:
        """Добавить аккаунт в избранное
        """
        return await self.__wraper._execute(
            f'/{self.__account_id}/star',
            'post'
        )
    
    async def unfavorite(self) -> None:
        """Убрать аккаунт из избранного.
        """
        return await self.__wraper._execute(
            f'/{self.__account_id}/star',
            'delete'
        )

    async def stick(self) -> None:
        """Закрепить аккаунт
        """
        return await self.__wraper._execute(
            f'/{self.__account_id}/stick',
            'post'
        )
    
    async def unstick(self) -> None:
        """Закрепить аккаунт
        """
        return await self.__wraper._execute(
            f'/{self.__account_id}/stick',
            'delete'
        )
    
    async def change_owner(self, new_owner_username: str, secret: str):
        params = dict(username=new_owner_username, secret_answer=secret)
        return await self.__wraper._execute(
            f'/{self.__account_id}/change-owner',
            'post',
            params
        )


    # async def reserve(self, price=None) -> None:
    #     """
    #     (OutDated | NotWork) Резервирует аккаунт.

    #     :param price: цена резерва.
    #     :type price: int, optional
    #     """
    #     return
    #     if price is None:
    #         price = self.__account_info.price

    #     await self.__wraper._execute(
    #         f"/{self.__account_id}/reserve",
    #         "post",
    #         params={"price": price}
    #     )

    async def buy(self, price: int = None, no_checK: bool = False) -> Good.Account:
        """
        Покупает аккаунт.

        :param price: цена покупки.
        :type price: int, optional
        :param no_checK: флаг, указывающий на необходимость отключения проверки при покупке.
        :type no_checK: bool, optional
        :return: купленный аккаунт.
        :rtype: Good.Account
        """
        no_checK = 1 if no_checK else 0
        if price is None:
            price = self.__account_info.price
        data = await self.__wraper._execute(
            f"/{self.__account_id}/fast-buy",
            "post",
            params={"price": price}
        )
        return Good.CATEG_AND_ACCOUNT[data['item']['category_id']].parse_obj(data['item'])


# TODO Paymnet
# Уже сделал даты в TimeValues
