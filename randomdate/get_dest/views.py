from django.shortcuts import render
from get_dest.models import Dest,URLs

# Create your views here.



def top(request):
    pass
    

def get_dest(request):
    dest = Dest.objects.all()
    context = {'dest': dest}
    return render(request, 'get_dest/dest.html', context)
