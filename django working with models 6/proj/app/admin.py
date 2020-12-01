from django.contrib import admin

# Register your models here.
from .models import notice


class noticeadmin(admin.ModelAdmin):
    list_display = ['subject', 'cr_date']
    search_fields = ['subject', 'msg']
    list_filter = ['cr_date']


admin.site.register(notice, noticeadmin)
