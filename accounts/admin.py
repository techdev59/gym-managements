from django.contrib import admin

from .models import User, GymDetails
# Register your models here.


admin.site.register(User)
admin.site.register(GymDetails)