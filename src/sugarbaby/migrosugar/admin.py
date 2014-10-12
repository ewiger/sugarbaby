from django.contrib import admin

from sugarbaby.migrosugar.models import DiaryRecord, ProductInfo


class DiaryRecordInstanceAdmin(admin.ModelAdmin):
    pass

admin.site.register(ProductInfo)
admin.site.register(DiaryRecord, DiaryRecordInstanceAdmin)
