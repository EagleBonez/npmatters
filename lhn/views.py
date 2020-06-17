from django.shortcuts import render
from django.views import generic
from .models import LocalAuthorityLHN, County
# Create your views here.

class LocalAuthorityLHNListView(generic.ListView):
    model = LocalAuthorityLHN
    template_name = 'lhn/local_authority_lhn_list.html'

class LocalAuthorityLHNDetailView(generic.DetailView):
    model = LocalAuthorityLHN
    template_name = 'lhn/local_authority_lhn_detail.html'

class CountyDetailView(generic.DetailView):
    model = County
    template_name = 'lhn/county_detail.html'
