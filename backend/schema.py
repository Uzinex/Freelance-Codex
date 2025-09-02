import strawberry
import projects.schema
import bids.schema
import reviews.schema
import payments.schema


@strawberry.type
class Query(
    projects.schema.Query,
    bids.schema.Query,
    reviews.schema.Query,
    payments.schema.Query,
):
    hello: str = "world"


@strawberry.type
class Mutation(
    projects.schema.Mutation,
    bids.schema.Mutation,
    reviews.schema.Mutation,
    payments.schema.Mutation,
):
    pass


schema = strawberry.Schema(query=Query, mutation=Mutation)
