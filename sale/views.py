from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Property, City
from .filters import PropertyFilter
from django.http import HttpResponse

# Create your views here.

def home(request):
    pfilter = PropertyFilter()
    expensive_properties = Property.objects.all().order_by('-price')[:6]
    last_createds = Property.objects.all().order_by('-created')[:6]
    return render(request, 'sale/home.html', context={
        'pfilter': pfilter,
        'expensive_properties': expensive_properties,
        'last_createds': last_createds,
    })

def property_detail(request, pk, slug):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'sale/property-detail.html', context={'property': property})

def property_list(request):
    properties_filter = PropertyFilter(request.GET, queryset=Property.objects.all())
    properties = properties_filter.qs
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(properties, 4)
    page = paginator.page(page_number)
    return render(request, 'sale/property-list.html', context={
        'properties': page.object_list,
        'paginator': paginator,
        'page_object': page,
        'filter': PropertyFilter
    })
    
    
def example(request, file, extension):
    return HttpResponse(f'ad: {file}, uzanti: {extension}')