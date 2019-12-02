from django.shortcuts import render
from .models import Building, Toolbox
from django.shortcuts import get_object_or_404
# Create your views here.


def index(request):
    return render(request, 'base.html')


def building_list(request):
    buildings = Building.objects.all()
    context = {
            'buildings': buildings,
        }
    return render(request, 'toolbox/dashboard.html', context)

def building_toolbox(request, building_ID):
    building = get_object_or_404(Building, pk = building_ID)
    u = building.toolboxes.all()
    print(u)
    context = {
            'building': building,
        }
    return render(request, 'toolbox/building_toolbox.html', context )
