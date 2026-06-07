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
    trending_books = graphene.List(BookType)
    latest_books = graphene.List(BookType)
    featured_books = graphene.List(BookType)
    search_books = graphene.List(BookType, query=graphene.String(require=True))


    def resolve_all_books(root, info):
        return Book.objects.all()

    def resolve_all_categories(root, info):
        return Category.objects.all()

    def resolve_book_by_id(root, info, id):
        return Book.objects.get(id=id)

    def resolve_featured_books(root, info):
        return Book.objects.all()[:5]

    def resolve_trending_books(root, info):
        return Book.objects.order_by('-views')[:10]

    def resolve_latest_books(root, info):
        return Book.objects.orderby('created_at')[:10]

    def resolve_search_books(root, info):
        return Book.object.filter(title__icontains=query)
