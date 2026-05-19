import graphene
from graphene_django import DjangoObjectType
from .models import Book, Category

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = '__all__'

class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = '__all__'


class BooksQuery(graphene.ObjectType):
    all_books = graphene.List(BookType)
    all_categories = graphene.List(CategoryType)

    def resolve_all_books(root, info):
        return Book.objects.all()

    def resolve_all_categories(root, info):
        return Category.objects.all()

    def resolve_book_by_id(root, info, id):
        return Book.objects.get(id=id)