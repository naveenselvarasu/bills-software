from django.contrib import admin
from .models import Store_add

# Register your models here.


class data(admin.ModelAdmin):
    list = ["s_no", "data", "type_of_expenditure", "cost"]


admin.site.register(Store_add, data)
