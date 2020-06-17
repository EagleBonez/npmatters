from django.shortcuts import render
# Create your views here.
from .models import Lpa, NeighbourhoodPlan

from django.db.models import Q

def planfinder_index(request):
    lpa_list = Lpa.objects.order_by('lpa_name')
    context = {
    'lpa_list': lpa_list,
    }
    return render(request, 'planfinder/index.html', context)

def detail(request, lpa_id):
    plans = NeighbourhoodPlan.objects.select_related('lpa').filter(lpa_id=lpa_id)
    return render(request, 'planfinder/detail.html', {'plans': plans})


def get_search_results(request):
    query = request.GET.get('q')
    query = query.strip()


    nplan_list = NeighbourhoodPlan.objects.filter(
        Q(plan_name__icontains=query, status=1) |
        Q(map_location__icontains=query, status=1) |
        Q(lpa__lpa_name__icontains=query, status=1) |
        Q(lpa__county__county_name__icontains=query, status=1) |
        Q(natpark__natpark_name__icontains=query, status=1) |
        Q(ref_date__icontains=query, status=1)
        )

    nplan_list = nplan_list.order_by('plan_name')
    return render(request, 'planfinder/search_results.html', {'nplan_list': nplan_list, 'query': query})
