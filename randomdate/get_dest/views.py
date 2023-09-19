from django.shortcuts import render
from get_dest.models import Dest

# Create your views here.



def top(request):
    return render(request, 'top.html')
    
def dest(request,dest_id):
    dest_object = Dest.objects.get(pk=dest_id)
    return render(request, 'base.html', {'dest_object':dest_object})

