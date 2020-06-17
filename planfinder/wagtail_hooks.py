from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from wagtail.contrib.modeladmin.options import (
    ModelAdmin, 
    ModelAdminGroup, 
    modeladmin_register 
)

from .models import NeighbourhoodPlan, County, Lpa, NationalPark


class NPAdmin(ModelAdmin):
    model = NeighbourhoodPlan
    list_display = ('plan_name', 'ref_date', 'status')
    search_fields = ['plan_name']
    #list_filter = ('status')

class CountyAdmin(ModelAdmin):
    model = County

class LpaAdmin(ModelAdmin):
    model = Lpa

class NationalParkAdmin(ModelAdmin):
    model = NationalPark


class NPGroup(ModelAdminGroup):
    menu_label = "Neighbourhood Plans" 
    menu_icon = "pick"
    items = (NPAdmin, LpaAdmin, CountyAdmin, NationalParkAdmin)


modeladmin_register(NPGroup)