from typing import Optional

import strawberry
from strawberry.types import Info

from .scalars import Product
from ..context import Context


@strawberry.type
class Mutation:

    @strawberry.mutation
    async def add_product(self, info: Info[Context, None], text: str,
                          quantity: Optional[int] = strawberry.UNSET,
                          completed: Optional[bool] = strawberry.UNSET) -> Product:
        response = await info.context.product_resolver.create(
            text=text, quantity=quantity, completed=completed
        )
        return response

    @strawberry.mutation
    async def update_product(self, info: Info[Context, None], id: int,
                             text: Optional[str] = strawberry.UNSET,
                             quantity: Optional[int] = strawberry.UNSET,
                             completed: Optional[bool] = strawberry.UNSET) -> Product:
        response = await info.context.product_resolver.update(
            id, text=text, quantity=quantity, completed=completed
        )
        return response

    @strawberry.mutation
    async def delete_product(self, info: Info[Context, None], id: int) -> None:
        await info.context.product_resolver.delete(id)


@strawberry.type
class Query:

    @strawberry.field
    async def products(self, info: Info[Context, None]) -> list[Product]:
        response = await info.context.product_resolver.list()
        return response

    @strawberry.field
    async def product(self, info: Info[Context, None], id: int) -> Product:
        response = await info.context.product_resolver.get(id)
        return response
