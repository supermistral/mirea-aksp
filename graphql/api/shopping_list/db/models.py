from datetime import datetime
from typing import Any, Type

import sqlalchemy as sa
from sqlalchemy.orm import validates
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


def model_to_dict(instance: Base, model_class: Type[Base]) -> dict[str, Any]:
    data: dict[str, Any] = {}
    for col in model_class.__table__.columns:
        try:
            data[col.name] = getattr(instance, col.name)
        except:
            pass
    return data


class Product(Base):
    __tablename__ = 'products'

    id: int = sa.Column(sa.Integer, primary_key=True, index=True)
    text: str = sa.Column(sa.String(127), nullable=False)
    quantity: int = sa.Column(sa.Integer, default=1, nullable=False)
    created_date = sa.Column(sa.DateTime(timezone=True), default=datetime.now, nullable=False)
    completed: bool = sa.Column(sa.Boolean, default=False, nullable=False)

    @validates('quantity')
    def validate_quantity(self, key: str, value: int) -> int:
        if value < 0:
            raise ValueError("Quantity must be a positive number")
        return value
