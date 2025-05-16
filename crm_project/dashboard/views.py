from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from lead.models import Lead
from client.models import Client
from teams.models import Team


@login_required
# Dashboard view
def dashboard(request):
    team = Team.objects.filter(created_by=request.user).first()
    lead=Lead.objects.filter(team=team).order_by("-created_at")[0:5]
    clients=Client.objects.filter(team=team).order_by("-created_at")[0:5]
    return render(request, 'dashboard/dashboard.html',{
        'lead': lead,
        'clients': clients,
    })
