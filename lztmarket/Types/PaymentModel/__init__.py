from pydantic import BaseModel
from typing import Dict


class Label(BaseModel):
    title: str


class User(BaseModel):
    user_id: int
    user_balance: int
    user_hold: int
    user_balance_with_hold: int


class Payment(BaseModel):
    operation_id: int = None
    operation_date: int = None
    operation_type: str = None
    outgoing_sum: int = None
    incoming_sum: int = None
    item_id: int = None
    wallet: str = None
    is_finished: int = None
    is_hold: int = None
    payment_system: str = None
    data: dict | bool = None
    hold_end_date: int = None
    api: int = None
    cancelled: int = None
    payment_status: str = None
    canCancelBalanceTransfer: bool = None
    canCancelBalancePayout: bool = None
    canFinishBalanceTransfer: bool = None
    canFinishBalancePayout: bool = None
    label: Label = None
    user: User = None
