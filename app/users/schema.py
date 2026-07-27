import graphene
from graphene_django import DjangoObjectType
from .models import User, Subscription, UserSubscription, Transaction

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'

class SubscriptionType(DjangoObjectType):
    class Meta:
        model = Subscription
        fields = '__all__'

class UserSubscriptionType(DjangoObjectType):
    class Meta:
        model = UserSubscription
        fields = '__all__'

class TransactionType(DjangoObjectType):
    class Meta:
        model = Transaction
        fields = '__all__'

class UserQuery(graphene.ObjectType):
    user_by_id = graphene.Field(UserType, id=graphene.ID(required=True))
    all_users = graphene.List(UserType)
    user_transactions = graphene.List(TransactionType, user_id=graphene.ID(required=True))

    def resolve_user_by_id(root, info, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_user_transactions(root, info, user_id):
        return Transaction.objects.filter(user_id=user_id)