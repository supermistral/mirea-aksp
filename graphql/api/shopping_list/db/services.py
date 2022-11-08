from typing import AsyncGenerator

from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from .session import get_session
from .models import Product
from .schemas import (
    ProductUpdate as ProductUpdateSchema,
    ProductCreate as ProductCreateSchema
)


class ProductService:
    """Product service containing ORM methods"""
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def get(self, id: int) -> Product:
        result = await self.db_session.execute(
            select(Product).filter(Product.id == id)
        )
        return result.one()[0]

    async def list(self) -> list[Product]:
        result = await self.db_session.execute(
            select(Product).order_by(Product.created_date.desc())
        )
        result_list = result.scalars().all()
        return result_list

    async def create(self, create_schema: ProductCreateSchema) -> Product:
        product = Product(**create_schema.dict(exclude_unset=True))

        self.db_session.add(product)
        await self.db_session.commit()

        return product
    
    async def update(self, id: int, update_schema: ProductUpdateSchema) -> Product:
        product = await self.get(id)

        for key, value in update_schema.dict(exclude_unset=True).items():
            setattr(product, key, value)

        await self.db_session.commit()

        return product
    
    async def delete(self, id: int) -> None:
        existing_product = await self.db_session.execute(
            select(Product).where(Product.id == id)
        )
        if existing_product.first() is not None:
            pass
        
        await self.db_session.execute(
            delete(Product).where(Product.id == id)
        )
        await self.db_session.commit()


async def get_product_service() -> AsyncGenerator[ProductService, None]:
    async with get_session() as session:
        yield ProductService(session)
