from django.contrib import admin
from .models import HomeImage,FeaturedImage,OM,OT
# Register your models here.
admin.site.register(HomeImage)
admin.site.register(FeaturedImage)

admin.site.register(OM)
admin.site.register(OT)