# pyrefly: ignore [missing-import]
import graphene
from graphene_django import DjangoObjectType
from .models import Book, Category, UserBookAccess, ReadingProgress

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = '__all__'

class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = '__all__'

class UserBookAccessType(DjangoObjectType):
    class Meta:
        model = UserBookAccess
        fields = '__all__'

class ReadingProgressType(DjangoObjectType):
    class Meta:
        model = ReadingProgress
        fields = '__all__'


class BooksQuery(graphene.ObjectType):
    all_books = graphene.List(BookType)
    all_categories = graphene.List(CategoryType)
    trending_books = graphene.List(BookType)
    latest_books = graphene.List(BookType)
    featured_books = graphene.List(BookType)
    search_books = graphene.List(BookType, query=graphene.String(required=True))
    book_by_id = graphene.Field(BookType, id=graphene.ID(required=True))


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
        return Book.objects.order_by('-created_at')[:10]

    def resolve_search_books(root, info, query):
        return Book.objects.filter(title__icontains=query)
 
    def book_count(self):
        return self.book_set.count()

    user_book_access = graphene.List(UserBookAccessType, user_id=graphene.ID(required=True))
    reading_progress = graphene.List(ReadingProgressType, user_id=graphene.ID(required=True))

    def resolve_user_book_access(root, info, user_id):
        return UserBookAccess.objects.filter(user_id=user_id)

    def resolve_reading_progress(root, info, user_id):
        return ReadingProgress.objects.filter(user_id=user_id)