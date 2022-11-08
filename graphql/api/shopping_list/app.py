from fastapi import FastAPI

from strawberry import Schema as StrawberrySchema
from strawberry.fastapi import GraphQLRouter
from strawberry.schema.config import StrawberryConfig

from .graphql.schemas import Mutation, Query
from .context import get_context


schema = StrawberrySchema(
    query=Query,
    mutation=Mutation,
    config=StrawberryConfig(auto_camel_case=True),
)


def create_app() -> FastAPI:
    app = FastAPI(
        title="shopping_list",
        description="Shopping list app to store individual shopping wishes",
        version="1.0"
    )


    @app.get('/health')
    async def health() -> str:
        return "OK"


    graphql_app = GraphQLRouter(schema, context_getter=get_context)
    app.include_router(graphql_app, prefix='/graphql')

    return app
