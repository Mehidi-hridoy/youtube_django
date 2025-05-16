from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
# Dashboard view
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')
