from django.contrib import admin
from django.urls import path

from graphene_django.views import GraphQLView

from django.views.decorators.csrf import csrf_exempt

from graphql_app.schema import schema

from app.homepage.views import home


urlpatterns = [
    path('', home),

    path('admin/', admin.site.urls),

    path(
        'graphql_app/',
        csrf_exempt(
            GraphQLView.as_view(
                graphiql=True,
                schema=schema
            )
        ),
    ),
]