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



