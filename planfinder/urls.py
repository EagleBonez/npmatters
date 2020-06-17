from django.urls import path

from . import views

urlpatterns = [
    path('', views.planfinder_index, name='planfinder_index'), #change this to "planfinder/"
    path('<int:lpa_id>/', views.detail, name='detail'),
    path('search/', views.get_search_results, name='search_results') #change this to "planfinder/search"
]