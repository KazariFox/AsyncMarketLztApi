from typing import List

from ..Types.Category import *
from ..Types.Good import *
from ..Types.AccountManage import AccountManager


def response_to_accounts(wrapper, account_list: List) -> List[AccountManager]:
    result = []
    for acc in account_list:
        if not acc['category_id'] in CATEG_AND_ACCOUNT.keys():
            acc_module = Account.parse_obj(acc)
            acc_module.unfiltered_account_data = acc
            result.append(
                AccountManager(
                    wrapper,
                    acc['item_id'],
                    acc_module,
                ))
            continue
        result.append(
            AccountManager(
                wrapper,
                acc['item_id'],
                CATEG_AND_ACCOUNT[acc['category_id']].parse_obj(acc),
            )
        )
    return result


__all__ = ['response_to_accounts']
