from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register
)

from .models import County, LocalAuthorityLHN

class CountyAdmin(ModelAdmin):
    model = County
    list_display = ('name',)
    search_fields = ['name']

class LocalAuthorityLHNAdmin(ModelAdmin):
    model = LocalAuthorityLHN
    list_display = ('la_code', 'la_area', 'county')
    search_fields = ['la_area']
    #list_filter = ('status')


class LhnGroup(ModelAdminGroup):
    menu_label = "Local Housing Need"
    menu_icon = "pick"
    items = (CountyAdmin, LocalAuthorityLHNAdmin)

modeladmin_register(LhnGroup)