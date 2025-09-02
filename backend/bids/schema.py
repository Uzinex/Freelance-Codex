import strawberry
import strawberry_django
from decimal import Decimal
from typing import List

from projects.models import Project
from projects.schema import ProjectType, UserType
from .models import Bid


@strawberry_django.type(Bid)
class BidType:
    id: strawberry.auto
    project: ProjectType
    freelancer: UserType
    amount: strawberry.auto
    message: strawberry.auto
    status: strawberry.auto
    created_at: strawberry.auto


@strawberry.type
class Query:
    @strawberry.field
    def bids(self, info, project_id: int) -> List[BidType]:
        return Bid.objects.filter(project_id=project_id)


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_bid(self, info, project_id: int, amount: Decimal, message: str) -> BidType:
        user = info.context.request.user
        if not user.is_authenticated:
            raise Exception("Authentication required")
        project = Project.objects.get(pk=project_id)
        bid = Bid.objects.create(
            project=project, freelancer=user, amount=amount, message=message
        )
        return bid

    @strawberry.mutation
    def accept_bid(self, info, id: int) -> BidType:
        user = info.context.request.user
        bid = Bid.objects.get(pk=id)
        if bid.project.owner != user:
            raise Exception("Not permitted")
        bid.status = "accepted"
        bid.save()
        return bid

    @strawberry.mutation
    def reject_bid(self, info, id: int) -> BidType:
        user = info.context.request.user
        bid = Bid.objects.get(pk=id)
        if bid.project.owner != user:
            raise Exception("Not permitted")
        bid.status = "rejected"
        bid.save()
        return bid
