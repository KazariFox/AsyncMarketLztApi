# Async LZT market lib

#### Данная библиотека создана для взаимодействия с api lzt.market.
#### Документация: [*Клик*](https://docs.api.zelenka.guru/?market)


## Быстрое начало работы

### Импорт и авторизация

```python
from lztmarket import MarketClient

TOKEN = "TOKEN"

client = MarketClient(TOKEN)
```

### Получение информации о себе
```python
from lztmarket.Types.Profile import User
info: User = await client.Me.info()

```

### Платежи
#### История платежей

```python
from typing import List
from lztmarket.Types.PaymentModel import Payment

# Информацию о параметрах смотреть в документации в коде.
history: List[Payment] = await client.Payment.history()

```
#### Совершить перевод
```python
from lztmarket.Types import TimeValues
from lztmarket.Types import Currency

# Информацию о параметрах смотреть в документации в коде.
await client.Payment.make(
    amount=10,
    secret="secret",
    username="Лисица",
    currency=Currency.EUR,
    hold_length_value=1
    hold_length_option=TimeValues.HOUR
    )
```

### Поиск

#### Вывести аккаунты из топа
```python
accs = await client.Goods.last(page=3)
```

#### Вывести аккаунты по какой-либо игре
```python

# Информацию о параметрах смотреть в документации в коде.
# Кроме указанных параметров существуют параметры для каждой категории.
# Узнать их можно кинув запрос на /{categoryName}/params.
# Позже все доп. параметры будут добавлены в классы.

accs = client.Goods.GenshinImpact.search()
```

### Аккаунт

#### Получить по id
```python
good = await client.Good.get(123123)
```

#### Информция
```python
print (await good.get_info())
```
#### Покупка
```python
await good.buy()
```
#### Поднятие
```python
await good.bump()
```
#### Передать другому пользователю
```python
await good.change_owner("Лисица", "secret")
```
#### Подтвердить смену пароля. (табличка с безопасностью)
```python
print(await good.change_password())
```
#### Отклонить предложение безопасности
```python
print(await good.decline_safe_about_password())
```
#### Удалить
```python
await good.delete()
```
#### Получить код с почты
```python
await good.get_mail_code()
```
#### Получить код с гуарда
```python
await good.get_guard_code()
```
#### Скачать mafile
```python
await good.get_mafile()
```
#### Снять гарантию
```python
await good.refuse_guarantee()
```
#### Получить пароль временной почты
```python
password = await good.get_tempmail_password()
```
#### Отредактировать
```python
password = await good.edit(price=10, currency=Currency.RUB)
```
#### Добавить в избранное
```python
await good.favorite()
```
#### Убрать из избранного
```python
await good.unfavorite()
```
#### Закрепить аккаунт 
```python
await good.stick()
```
#### Убрать закреп
```python
await good.unstick()
```
