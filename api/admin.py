from django.contrib import admin
from .models import TranSum
from django.contrib.auth.models import Group
# Register your models here.
admin.site.register(TranSum)
admin.site.unregister(Group)
