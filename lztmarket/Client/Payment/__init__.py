from ...ApiWrapper import Wrapper
from ...Types import TimeValues, Currency, PaymentModel, PaymentType
from datetime import datetime


class Payment:

    def __init__(self, wrapper: Wrapper) -> None:
        self.__wrapper = wrapper

    async def make(
            self,
            amount: int,
            secret: str,
            currency: str = "rub",
            user_id: int = None,
            username: str = None,
            comment: str = None,
            hold_length_value: int = None,
            hold_length_option: str = None) -> None:
        """
    Создает перевод денежных средств на кошелек пользователя.

    - amount: Сумма перевода в копейках.
    - secret: Ответ на секретный вопрос пользователя.
    - currency: Валюта перевода. Допустимые значения: "cny", "usd", "rub", "eur", "uah", "kzt", "byn", "gbp".
    - user_id: Идентификатор пользователя.
    - username: Имя пользователя.
    - comment: Комментарий к переводу.
    - hold_length_value: Время удержания перевода.
    - hold_length_option: Единица измерения времени удержания перевода. Допустимые значения: "day", "hour", "month", "week", "year".
    """
        params = {}

        if user_id is None and username is None:
            raise ValueError("username or user_id must be specified !")

        if user_id:
            params['user_id'] = user_id
        elif username:
            params['username'] = username

        if secret is None:
            raise ValueError("secret must be specified !")
        params['secret_answer'] = secret

        if comment is not None:
            params['comment'] = comment

        if hold_length_value:
            if not hold_length_option in TimeValues.__dict__.values():
                raise ValueError(
                    f"Invalid hold_length_option: {hold_length_option}. Use 'from lztmarket.Types import TimeValues'")

            params['transfer_hold'] = True
            params['hold_length_value'] = hold_length_value
            params['hold_length_option'] = hold_length_option

        if not currency in Currency.__dict__.values():
            raise ValueError(
                f"Invalid currency: {currency}. Use 'from lztmarket.Types import Currency'")
        params['currency'] = currency

        params['amount'] = amount

        await self.__wrapper._execute(
            '/balance/transfer',
            'post',
            params=params
        )

    async def history(
            self,
            my_id: int,
            payment_type: str=None,
            pmin: int=None,
            pmax: int=None,
            receiver: int=None,
            sender: int=None,
            startDate: datetime.isoformat=None,
            endDate: datetime.isoformat=None,
            wallet: str=None,
            comment: str=None,
            is_hold: bool=None,
            start_by_operation_id: int=None
            ) -> list[PaymentModel.Payment]:
        
        params = {}
        """Получает список платежей для определенного пользователя.

        :param my_id: идентификатор пользователя.
        :type my_id: int
        :param payment_type: тип платежа, один из вариантов PaymentType.
        :type payment_type: str, optional
        :param pmin: минимальная сумма платежа.
        :type pmin: int, optional
        :param pmax: максимальная сумма платежа.
        :type pmax: int, optional
        :param receiver: идентификатор пользователя-получателя платежа.
        :type receiver: int, optional
        :param sender: идентификатор пользователя-отправителя платежа.
        :type sender: int, optional
        :param startDate: дата начала периода, за который запрашиваются платежи.
        :type startDate: datetime.isoformat, optional
        :param endDate: дата окончания периода, за который запрашиваются платежи.
        :type endDate: datetime.isoformat, optional
        :param wallet: кошелек, с которого был произведен платеж.
        :type wallet: str, optional
        :param comment: комментарий к платежу.
        :type comment: str, optional
        :param is_hold: флаг, указывающий является ли платеж замороженным.
        :type is_hold: bool, optional
        :param start_by_operation_id: идентификатор платежа, с которого начинать выборку.
        :type start_by_operation_id: int, optional
        :return: список платежей.
        :rtype: list[PaymentModel.Payment]
        :raises ValueError: если передан неверный тип платежа."""
        if not payment_type in PaymentType.__dict__.values():
            raise ValueError(f"Invalid value payment_type. Use 'from lztmarket.Types import PaymentType'")
        
        params['type'] = payment_type
        
        if pmin:
            params['pmin'] = pmin
        
        if pmax:
            params['pmax'] = pmax

        if receiver:
            params['receiver'] = receiver

        if sender:
            params['sender'] = sender

        if startDate:
            params['startDate'] = startDate
        
        if endDate:
            params['endDate'] = endDate

        if wallet:
            params['wallet'] = wallet

        if comment:
            comment['comment'] = comment

        if is_hold is not None:
            params['is_hold'] = int(is_hold)

        if start_by_operation_id:
            params['operation_id_lt'] = start_by_operation_id

        un_sorted_data = await self.__wrapper._execute(
            f"/user/{my_id}/payments",
            "get",
            params=params
        )

        result = []

        for payment in un_sorted_data['payments'].keys():
            print(payment)
            result.append(PaymentModel.Payment.parse_obj(un_sorted_data['payments'][payment]))
        
        return result