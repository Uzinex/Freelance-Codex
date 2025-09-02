import strawberry
import projects.schema
import bids.schema


@strawberry.type
class Query(projects.schema.Query, bids.schema.Query):
    hello: str = "world"


@strawberry.type
class Mutation(projects.schema.Mutation, bids.schema.Mutation):
    pass


schema = strawberry.Schema(query=Query, mutation=Mutation)
