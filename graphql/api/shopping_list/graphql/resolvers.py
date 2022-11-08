from typing import Any

from fastapi import Depends

import strawberry

from .scalars import Product
from ..db.models import model_to_dict, Product as ProductModel
from ..db.services import ProductService, get_product_service
from ..db.schemas import (
    ProductCreate as ProductCreateSchema,
    ProductUpdate as ProductUpdateSchema
)


def exclude_unset(data: dict[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in data.items() if v is not strawberry.UNSET}


class ProductResolver:
    """Set of methods that work with the product service"""

    def __init__(self, product_service: ProductService):
        self.service = product_service

    async def get(self, id: int) -> Product:
        result = await self.service.get(id)
        return Product(**model_to_dict(result, ProductModel))

    async def list(self) -> list[Product]:
        result = await self.service.list()
        return [Product(**model_to_dict(x, ProductModel)) for x in result]
    
    async def create(self, **kwargs) -> Product:
        schema = ProductCreateSchema(**exclude_unset(kwargs))
        result = await self.service.create(schema)
        return Product(**model_to_dict(result, ProductModel))

    async def update(self, id: int, **kwargs) -> Product:
        schema = ProductUpdateSchema(**exclude_unset(kwargs))
        result = await self.service.update(id, schema)
        return Product(**model_to_dict(result, ProductModel))
    
    async def delete(self, id: int) -> None:
        await self.service.delete(id)


def get_product_resolver(
    product_service: ProductService = Depends(get_product_service)
) -> ProductResolver:
    return ProductResolver(product_service)
