from pydantic import BaseModel
from typing import Optional


class SystemInfo(BaseModel):
    visitor_id: Optional[int]
    time: Optional[int]

class User(BaseModel):
    user_id: Optional[int]
    username: Optional[str]
    user_message_count: Optional[int]
    user_register_date: Optional[int]
    user_like_count: Optional[int]
    short_link: Optional[str]
    user_email: Optional[str]
    user_unread_notification_count: Optional[int]
    user_dob_day: Optional[int]
    user_dob_month: Optional[int]
    user_dob_year: Optional[int]
    user_title: Optional[str]
    user_last_seen_date: Optional[int]
    balance: Optional[int]
    hold: Optional[int]
    system_info: Optional[SystemInfo]