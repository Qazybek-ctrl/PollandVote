from django.contrib import admin

from .models import Poll, Voted
# Register your models here.

admin.site.register(Poll)
admin.site.register(Voted)