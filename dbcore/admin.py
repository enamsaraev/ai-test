from django.contrib import admin

from dbcore.models import ApplicationData, ImportData, PredictData


@admin.register(ApplicationData)
class ApplicationDataAdmin(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(ImportData)
class ImportDataAdmin(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(PredictData)
class ImportDataAdmin(admin.ModelAdmin):
    list_display = ('import_data',)
