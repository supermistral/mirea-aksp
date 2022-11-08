from datetime import datetime

import strawberry


@strawberry.type
class Product:
    id: int
    text: str
    quantity: int
    created_date: datetime
    completed: bool
