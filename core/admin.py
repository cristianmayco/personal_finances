from django.contrib import admin
from core import models


@admin.register(models.Bill)
class BillAdmin(admin.ModelAdmin):
    ordering = ['created']
    list_display = ['type', 'description', 'due_date', 'payday', 'active', 'amount']
    list_filter = ['type', 'due_date', 'payday', 'active']
