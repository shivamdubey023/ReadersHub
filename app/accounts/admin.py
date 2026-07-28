from django.contrib import admin
from app.user.models import Subscription, User, Transaction, UserSubscription
# Register your models here.
admin.site.register(Subscription)
admin.site.register(User)
admin.site.register(Transaction)
admin.site.register(UserSubscription)