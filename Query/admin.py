from django.contrib import admin
from .models import Query, ExtendedUser, Subscriber
# Register your models here.
admin.site.register(Query)
admin.site.register(ExtendedUser)
admin.site.register(Subscriber)
