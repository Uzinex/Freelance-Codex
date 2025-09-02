import strawberry
import projects.schema
import bids.schema
import reviews.schema


@strawberry.type
class Query(projects.schema.Query, bids.schema.Query, reviews.schema.Query):
    pass


@strawberry.type
class Mutation(
    projects.schema.Mutation, bids.schema.Mutation, reviews.schema.Mutation
):
    pass


schema = strawberry.Schema(query=Query, mutation=Mutation)
