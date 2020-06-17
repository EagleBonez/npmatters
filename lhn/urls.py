from django.urls import path
from . import views

urlpatterns = [
    path('', views.LocalAuthorityLHNListView.as_view(), name='lhn'),
    path('la/<int:pk>', views.LocalAuthorityLHNDetailView.as_view(), name='lhn-detail'),
    path('county/<int:pk>', views.CountyDetailView.as_view(), name='county-detail'),
]
