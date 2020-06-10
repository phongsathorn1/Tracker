from django.contrib import admin
from result.models import Sheet
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(Sheet)
class Sheetadmin(ImportExportModelAdmin):
    pass
