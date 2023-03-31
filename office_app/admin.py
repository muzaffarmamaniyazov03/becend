from django.contrib import admin
from .models import *


@admin.register(Management)
class ManagementAdmin(admin.ModelAdmin):
    list_display = ('id', 'publish', 'created_at', 'updated_at')
    list_editable = ('publish',)


@admin.register(Regional)
class RegionalAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_uz', 'title_ru', 'created_at', 'updated_at', 'publish')
    list_editable = ('publish',)
    list_display_links = ('id', 'title_uz', 'title_ru')


@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_ru', 'name_uz', 'post_ru', 'post_uz', 'publish')
    list_editable = ('publish',)
    list_display_links = ('id', 'name_ru', 'name_uz')


admin.site.register(About)
admin.site.register(Organization)
admin.site.register(Director)
admin.site.register(News)
admin.site.register(Documents)
admin.site.register(OpenData)

