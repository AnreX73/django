from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from smart.models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published',)
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class PricesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published',)
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class ExtraAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published',)
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class NavAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'annotations1', 'annotations2')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True


class ServicesAdminForm(forms.ModelForm):
    annotation = forms.CharField(label='Рекламное описание ', widget=CKEditorUploadingWidget())

    class Meta:
        model = Services
        fields = '__all__'


class ServicesAdmin(admin.ModelAdmin):
    form = ServicesAdminForm
    list_display = ('id', 'title', 'getHtmlPhoto', 'time_create', 'is_published', 'cat',)
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True

    def getHtmlPhoto(self, picture):
        if picture.menu_image:
            return mark_safe(f"<img src='{picture.menu_image.url}' width=50>")

    getHtmlPhoto.short_description = 'миниатюра'


admin.site.register(Services, ServicesAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Nav, NavAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Prices, PricesAdmin)
admin.site.register(Extra, ExtraAdmin)

admin.site.site_header = 'Smart studio'
