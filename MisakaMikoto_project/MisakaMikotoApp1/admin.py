from django.contrib import admin
from MisakaMikotoApp1.models import MisakaMikoto, Webpage, AccessRecord, users, UserProfileInfo

# Register your models here.

admin.site.register(MisakaMikoto)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(users)
admin.site.register(UserProfileInfo)