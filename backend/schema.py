import strawberry
import projects.schema


@strawberry.type
class Query(projects.schema.Query):
    hello: str = "world"


@strawberry.type
class Mutation(projects.schema.Mutation):
    pass


schema = strawberry.Schema(query=Query, mutation=Mutation)
