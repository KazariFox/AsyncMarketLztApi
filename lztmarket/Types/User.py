from pydantic import BaseModel


class Seller(BaseModel):
    user_id: int = None
    sold_items_count: int = None
    restore_data: str = None
    username: str = None
    avatar_date: int = None
    is_banned: int = None
    display_style_group_id: int = None
    uniq_username_css: str = None
    restore_percents: int | None = None
