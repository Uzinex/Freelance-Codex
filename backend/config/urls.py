from django.contrib import admin
from django.urls import path, include
from strawberry.django.views import GraphQLView
from schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/auth/', include('accounts.urls')),
    path('graphql/', GraphQLView.as_view(schema=schema)),
]
