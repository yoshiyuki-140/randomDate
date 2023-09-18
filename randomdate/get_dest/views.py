from django.shortcuts import render,get_object_or_404
from get_dest.models import Dest,URLs

# Create your views here.



def top(request):
    return render(request, 'top.html')
    
def dest(request,dest_id):
    dest_object = Dest.objects.get(pk=dest_id)
    return render(request, 'dest.html', {'dest_object':dest_object})

