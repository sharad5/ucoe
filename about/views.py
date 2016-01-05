from django.shortcuts import render
from django.utils import timezone
from .models import Department

def about(request):
    about = Department.objects.all()
    print(about)
    return render(request, 'about/about.html', {'about':about})