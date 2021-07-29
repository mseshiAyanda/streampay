from django.contrib import admin
from .models import User, Content, Membership, UserMembership, Subscription
# Register your models here.

admin.site.register(User)
admin.site.register(Content)
admin.site.register(UserMembership)
admin.site.register(Membership)
admin.site.register(Subscription)