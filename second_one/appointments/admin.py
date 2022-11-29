from django.contrib import admin
from .models import Week, Gap, User #, CustomUser

admin.site.register(Week)
admin.site.register(Gap)
admin.site.register(User)
# admin.site.register(CustomUser)   # settings and models must be modified as well
