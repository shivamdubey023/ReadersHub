import graphene

from app.books.schema import BooksQuery

class Query(BooksQuery, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)