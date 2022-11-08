from fastapi import Depends

from strawberry.fastapi import BaseContext

from .graphql.resolvers import ProductResolver, get_product_resolver


class Context(BaseContext):
    def __init__(self, product_resolver: ProductResolver):
        self.product_resolver = product_resolver


async def context_dependency(
    product_resolver: ProductResolver = Depends(get_product_resolver)
) -> Context:
    return Context(product_resolver=product_resolver)


async def get_context(
    context: Context = Depends(context_dependency)
) -> Context:
    return context
