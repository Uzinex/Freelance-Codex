from django.contrib import admin
from django.urls import path, include
import strawberry
from strawberry.django.views import GraphQLView

@strawberry.type
class Query:
    hello: str = "world"

schema = strawberry.Schema(query=Query)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('graphql/', GraphQLView.as_view(schema=schema)),
]
