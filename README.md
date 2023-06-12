# Async LZT market lib

#### Данная библиотека создана для взаимодействия с api lzt.market.
#### Документация: [*Клик*](https://docs.api.zelenka.guru/?market)
#### Требуется httpx & pydantic
#### У маркета стоит ограничение на один запрос в секунду. Если вы попытаетесь его нарушить - вылетит ошибка. Благодаря этому вы не получите бан по ip. Стоит лишь её ловить)




## Быстрое начало работы

### Импорт и авторизация

```python
from lztmarket import MarketClient

TOKEN = "TOKEN"

client = MarketClient(TOKEN)

# Проверка лимита на отсылку запроса (анти бан по айпи).
print(client.can_send)
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
#### Генерация ссылки на оплату
```python
link = await m.Payment.generate_link("Лисица", 10, 'test', 'https://google.com')
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

#### Опубликовать
```python
from lztmarket.Types import Category, Currency, ItemOrigin, Guarantee

await acc = await client.Good.add(
        "Test", 
        1000,
        Category.VK.id,
        Currency.RUB,
        ItemOrigin.FIGHING,
        Guarantee.HOURS12,

        )
```
#### Добавить данные в новый лот
```python
await acc.check(login_password="skchlfpyuh@rambler.ru:1408945FHtwji")
```
#### Получить временную почту
```python
mail = await acc.add_to_unpublished()
```

#### Информция
```python
print (await good.get_info())
# Полный json ответ можно посмотреть по
data = await good.get_info()
print(data.unfiltered_account_data)
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

### Модели
```python
import lztmarket.Types as LZTMODELS
# Здесь описаны модели 
# Позже хаос будет устранён.
# Для каждого аккаунта в модуле Good будет создан свой датакласс.
# На данный момент там есть несколько для примера.
LZTMODELS.Good
LZTMODELS.Category
LZTMODELS.Currency
LZTMODELS.Guarantee
LZTMODELS.ItemOrigin
LZTMODELS.Mail
LZTMODELS.PaymentType
LZTMODELS.Profile
LZTMODELS.TimeValues
LZTMODELS.User
```
