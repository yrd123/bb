from django.shortcuts import render,redirect
from .models import Events
# Create your views here.
def index(request):
    events=Events.objects.all().order_by("-date")
    context={'events':events}
    
    return render(request,'events.html',context)
